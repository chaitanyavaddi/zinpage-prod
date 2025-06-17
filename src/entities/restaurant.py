from dataclasses import dataclass
from typing import Optional

@dataclass
class Restaurant:
    id
    name: str = ""
    email: str = ""
    phone: str = ""
    username: str = ""
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    
