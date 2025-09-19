from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class UserEntity:
    id: Optional[int]
    username: str
    email: str
    rol_id: int
    activo: bool = True
    ultimo_login: Optional[datetime] = None
    created_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
