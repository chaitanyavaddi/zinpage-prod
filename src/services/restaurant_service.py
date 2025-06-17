from ..repositories.restaurant_repository import RestaurantRepository

class RestaurantService():

    def __init__(self):
        self._repository = RestaurantRepository()

    
    def create_restaurant(self, restuarant_details):
        self._repository.create_restaurant(restuarant_details)