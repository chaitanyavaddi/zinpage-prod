from fastapi import APIRouter, FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi import status
from ..services.restaurant_service import RestaurantService
from ..entities.restaurant import Restaurant
from ..utils.encyption import encode_password
from supabase import create_client

router = APIRouter()
# service = RestaurantService()

templates = Jinja2Templates(directory="templates")

# @router.get("/", response_class=HTMLResponse)
# def home(request: Request):
#   return templates.TemplateResponse("index.html", {"request": request})



def get_loggedin_user(request: Request):
    token = request.cookies.get('user_session')
    res_service =  RestaurantService()
    user = res_service.get_current_user(token)
    if user:
        return user
    return None

# UI HTML ENDPOINTS

@router.get('/login')
def get_login_page(request: Request):
    user = get_loggedin_user(request)
    if user:
        return RedirectResponse(
            url="/dashboard",
            status_code=status.HTTP_303_SEE_OTHER
            
        )
    return templates.TemplateResponse("login.html", {"request": request})


@router.get('/signup')
def get_signup_page(request: Request):
    user = get_loggedin_user(request)
    if user:
        response = RedirectResponse(
        url="/dashboard",
        status_code=status.HTTP_303_SEE_OTHER
        
        )
        return response
    return  templates.TemplateResponse("signup.html", {"request": request})


@router.get('/dashboard')
def get_dashboard_page(request: Request):
    user = get_loggedin_user(request)
    if user:
        return templates.TemplateResponse('dashboard.html', {"request": request})
    else:
        return RedirectResponse(
        url="/login",
        status_code=status.HTTP_303_SEE_OTHER
    )


## APIS

@router.post('/api/signup')
def make_signup(request: Request, 
               email: str = Form(...), 
               password: str = Form(...)):
   try:
    res_service =  RestaurantService()
    user = res_service.signup_restaurant(email, password)
    if user:
        res = res_service.login_restaurant(email, password)
        details = {
            "name": "",
            "email": email,
            "phone": "",
            "username": "",
            "password": "",
            "user_id": res.user.id
        }
        restaurant = res_service.create_restaurant(details)
       
    return templates.TemplateResponse("signup.html", {"request": request, "message": "Signup successful"})
   except Exception as e:
      return templates.TemplateResponse("signup.html", {"request": request, "message": e.hint})

@router.post('/api/login')
def make_login(request: Request, 
               email: str = Form(...), 
               password: str = Form(...)):
    
    res_service =  RestaurantService()
    user = res_service.login_restaurant(email, password)

    response = RedirectResponse(
        url="/dashboard",
        status_code=status.HTTP_303_SEE_OTHER
    )

    response.set_cookie(
         key="user_session",
            value=user.session.access_token,
            httponly=True,
            secure=True,
            samesite='lax',
            max_age=3600
    )

    return response

@router.get("/api/logout")
async def logout():
    response = RedirectResponse(
        url="/",
        status_code=status.HTTP_303_SEE_OTHER
    )
    response.delete_cookie("user_session")
    return response


@router.post("/restaurants/create")
def create_restaurant(details: dict):
    encrypted_pass = encode_password(details["password"])
    details["password"] = encrypted_pass
    service = RestaurantService()
    res = service.create_restaurant(details)
    return res

@router.get("/restaurants", response_class=HTMLResponse)
def get_all_restaurants(request: Request):
    service = RestaurantService()
    res = service.get_restaurants()
    return templates.TemplateResponse("index.html", {"request": request, "data":res})