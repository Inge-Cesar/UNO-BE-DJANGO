from dataclasses import dataclass
from typing import Optional
from datetime import datetime, date

@dataclass
class StudentEntity:
    id: Optional[int]
    usuario_id: int
    nombre: str
    registro: Optional[str]
    carrera_id: int
    semestre: Optional[int]
    fecha_nacimiento: Optional[date]
    ppa: Optional[float]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
