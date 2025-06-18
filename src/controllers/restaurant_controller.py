from fastapi import APIRouter, FastAPI, Request
from ..services.restaurant_service import RestaurantService
from ..entities.restaurant import Restaurant
from ..utils.encyption import encode_password

router = APIRouter()
# service = RestaurantService()

@router.post("/restaurants/create")
def create_restaurant(details: dict):
    encrypted_pass = encode_password(details["password"])
    details["password"] = encrypted_pass
    service = RestaurantService()
    res = service.create_restaurant(details)
    return res

@router.get("/restaurants")
def get_all_restaurants():
    service = RestaurantService()
    res = service.get_restaurants()
    return res