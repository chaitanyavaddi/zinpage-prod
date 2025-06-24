from fastapi import APIRouter, FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
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


@router.get('/login')
def get_login_page(request: Request):
    return  templates.TemplateResponse("login.html", {"request": request})



@router.get('/signup')
def get_signup_page(request: Request):
    return  templates.TemplateResponse("signup.html", {"request": request})



@router.post('/api/signup')
def make_signup(request: Request, 
               email: str = Form(...), 
               password: str = Form(...)):
   try:
    res_service =  RestaurantService()
    response = res_service.signup_restaurant(email, password)
    return templates.TemplateResponse("signup.html", {"request": request, "message": "Signup successful"})
   except Exception as e:
      return templates.TemplateResponse("signup.html", {"request": request, "message": e.hint})

@router.post('/api/login')
def make_login(request: Request, 
               email: str = Form(...), 
               password: str = Form(...)):
    
    print(email)
    print(password)


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