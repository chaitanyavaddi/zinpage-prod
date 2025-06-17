from dataclasses import dataclass
from typing import Optional

@dataclass
class Dish:
    id
    name: str = ""
    description: str = ""
    price: int = ""
    image: str = ""
    is_available: int = 1
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    
