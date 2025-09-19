from dataclasses import dataclass
from typing import Optional

@dataclass
class ProyectoMiembroEntity:
    id: Optional[int]
    proyecto_id: int
    estudiante_id: int
    rol: Optional[str] = None
    es_lider: bool = False
