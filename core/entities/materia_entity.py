from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class MateriaEntity:
    id: Optional[int]
    carrera_id: Optional[int]
    codigo: Optional[str]
    nombre: str
    creditos: Optional[int] = None
    semestre_materia: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
