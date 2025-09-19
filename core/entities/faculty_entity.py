from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class FacultyEntity:
    id: Optional[int]
    nombre: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
