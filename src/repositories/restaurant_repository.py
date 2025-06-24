from supabase import create_client
import os
from ..entities.restaurant import Restaurant
from dotenv import load_dotenv

class RestaurantRepository:

    def __init__(self):
        load_dotenv()
        
        self.supabase = create_client(
            os.getenv("SUPABASE_URL"),
            os.getenv("SUPABASE_KEY")
        )

        self._table_name = "restaurants"

    def signup_restaurant(self, email, password):
        user = self.supabase.auth.sign_up({'email': email, 'password': password})
        return user
    
    def create_restaurant(self, restaurant):
        result = self.supabase.table(self._table_name).insert(restaurant).execute()
        return result.data
    
    def get_all(self):
        result = self.supabase.table(self._table_name).select("id,name,email,username,phone").execute()
        # self.supabase.storage()
        return result.data