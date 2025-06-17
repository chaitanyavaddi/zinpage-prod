from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from supabase import create_client
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")
supabase_url = "https://zkvkujdqklmtpcvnaxgz.supabase.co"
supabase_api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inprdmt1amRxa2xtdHBjdm5heGd6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDk4MjYyMzgsImV4cCI6MjA2NTQwMjIzOH0.Ql9kzHB4QJDA1NaDqhXXf2xXZBkIPt_pxfp1Id07AKE"

database = create_client(supabase_url, supabase_api_key)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/restaurants")
def get_restaurants():
    response = database.table('restaurants').select("*").execute()
    return response.data