from dataclasses import dataclass
from typing import Optional
from datetime import date, datetime

@dataclass
class ProyectoEntity:
    id: Optional[int]
    estudiante_id: int
    tutor_id: Optional[int]
    titulo: str
    descripcion: Optional[str] = None
    estado_id: Optional[int] = None
    fecha_inicio: Optional[date] = None
    fecha_fin: Optional[date] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    # Campos opcionales para GraphQL
    estudiante_nombre: Optional[str] = None
    tutor_nombre: Optional[str] = None
    estado_nombre: Optional[str] = None
