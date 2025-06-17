from supabase import create_client
import os
from ..entities.restaurant import Restaurant

class RestaurantRepository:

    def __init__(self):
        self.supabase = create_client(
            os.getenv("SUPABASE_URL"),
            os.getenv("SUPABASE_KEY")
        )

    def create_restaurant(self, restaurant):
        result = self.supabase.table("restaurants").insert(restaurant).execute()
        return result.data