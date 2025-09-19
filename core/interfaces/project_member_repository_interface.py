from abc import ABC, abstractmethod
from typing import List
from core.entities.project_member_entity import ProyectoMiembroEntity

class ProjectMemberRepositoryInterface(ABC):

    @abstractmethod
    def create(self, member: ProyectoMiembroEntity) -> ProyectoMiembroEntity: pass

    @abstractmethod
    def list_by_project(self, project_id: int) -> List[ProyectoMiembroEntity]: pass
