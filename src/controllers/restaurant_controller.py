from fastapi import APIRouter, FastAPI
from ..services.restaurant_service import RestaurantService

router = APIRouter()

# service = RestaurantService()

@router.post("/restaurants/create")
def create_restaurant():
    service = RestaurantService()
    pass