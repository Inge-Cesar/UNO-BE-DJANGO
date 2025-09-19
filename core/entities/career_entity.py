from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class CareerEntity:
    id: Optional[int]
    codigo: Optional[str]
    nombre: str
    facultad_id: Optional[int]
    institucion: Optional[str]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
