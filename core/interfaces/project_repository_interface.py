from abc import ABC, abstractmethod
from typing import List, Optional
from core.entities.project_entity import ProyectoEntity

class ProjectRepositoryInterface(ABC):

    @abstractmethod
    def create(self, project: ProyectoEntity) -> ProyectoEntity: pass

    @abstractmethod
    def update(self, project: ProyectoEntity) -> ProyectoEntity: pass

    @abstractmethod
    def delete(self, project_id: int) -> None: pass

    @abstractmethod
    def get(self, project_id: int) -> Optional[ProyectoEntity]: pass

    @abstractmethod
    def list(self) -> List[ProyectoEntity]: pass
