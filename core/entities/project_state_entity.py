from dataclasses import dataclass
from typing import Optional

@dataclass
class ProjectStateEntity:
    id: Optional[int]
    nombre: str
