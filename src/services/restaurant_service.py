from ..repositories.restaurant_repository import RestaurantRepository

class RestaurantService():

    def __init__(self):
        self._repository = RestaurantRepository()

    def signup_restaurant(self, email, password):
        return self._repository.signup_restaurant(email, password)
    
    def login_restaurant(self, email, password):
        return self._repository.login_restaurant(email, password)
    
    def get_restaurant(self, user_id):
        return self._repository.get_restaurant(user_id)

    def create_restaurant(self, restuarant_details):
        return self._repository.create_restaurant(restuarant_details)
    
    def update_restaurant(self, restuarant_details):
        return self._repository.update_restaurant(restuarant_details)
    
    def get_restaurants(self):
        return self._repository.get_all()
    

    def get_current_user(self, session_token):
        return self._repository.get_current_user(session_token)