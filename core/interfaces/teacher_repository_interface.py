# core/interfaces/teacher_repository_interface.py
from abc import ABC, abstractmethod
from typing import List, Optional
from core.entities.teacher_entity import TeacherEntity

class TeacherRepositoryInterface(ABC):

    @abstractmethod
    def create(self, teacher: TeacherEntity) -> TeacherEntity:
        pass

    @abstractmethod
    def update(self, teacher: TeacherEntity) -> TeacherEntity:
        pass

    @abstractmethod
    def delete(self, teacher_id: int) -> None:
        pass

    @abstractmethod
    def get(self, teacher_id: int) -> Optional[TeacherEntity]:
        pass

    @abstractmethod
    def list(self, nombre: str = None) -> List[TeacherEntity]:
        pass
