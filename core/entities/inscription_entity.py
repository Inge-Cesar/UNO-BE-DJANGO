from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class InscriptionEntity:
    id: Optional[int]
    estudiante_id: int
    materia_id: int
    fecha_inscripcion: Optional[datetime] = None
