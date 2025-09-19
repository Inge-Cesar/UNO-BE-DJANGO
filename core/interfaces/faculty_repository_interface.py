from abc import ABC, abstractmethod
from typing import List, Optional
from core.entities.faculty_entity import FacultyEntity

class FacultyRepositoryInterface(ABC):

    @abstractmethod
    def create(self, faculty: FacultyEntity) -> FacultyEntity:
        pass

    @abstractmethod
    def update(self, faculty: FacultyEntity) -> FacultyEntity:
        pass

    @abstractmethod
    def delete(self, faculty_id: int) -> None:
        pass

    @abstractmethod
    def get(self, faculty_id: int) -> Optional[FacultyEntity]:
        pass

    @abstractmethod
    def list(self, nombre: str = None) -> List[FacultyEntity]:
        pass
