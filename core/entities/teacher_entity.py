# core/entities/teacher_entity.py
from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class TeacherEntity:
    id: Optional[int]
    usuario_id: int
    nombre: str
    especialidad: Optional[str] = None
    facultad: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
