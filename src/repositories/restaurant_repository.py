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
    
    def login_restaurant(self, email, password):
        user = self.supabase.auth.sign_in_with_password({
            'email': email,
            'password': password
        })
        return user
    
    def create_restaurant(self, restaurant):
        result = self.supabase.table(self._table_name).insert(restaurant).execute()
        return result.data
    
    def get_restaurant(self, user_id):
        result = self.supabase.table(self._table_name).select('*').eq('user_id', user_id).execute()
        return result.data
    
    def update_restaurant(self, restaurant):
        result = self.supabase.table(self._table_name).update(restaurant).eq('user_id', restaurant.get('user_id')).execute()
        return result.data
    
    def get_all(self):
        result = self.supabase.table(self._table_name).select("id,name,email,username,phone").execute()
        # self.supabase.storage()
        return result.data
    
    def get_dishes(self, res_id):
        result = self.supabase.table('dishes').select('*').eq('restaurant_id', res_id).execute()
        return result.data
    
    def get_current_user(self, session_token):
        try:
            user = self.supabase.auth.get_user(session_token)
            return user
        except Exception:
            return None