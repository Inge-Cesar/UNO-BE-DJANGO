from abc import ABC, abstractmethod
from typing import List, Optional
from core.entities.student_entity import StudentEntity

class StudentRepositoryInterface(ABC):

    @abstractmethod
    def create(self, student: StudentEntity) -> StudentEntity: ...
    
    @abstractmethod
    def update(self, student: StudentEntity) -> StudentEntity: ...
    
    @abstractmethod
    def delete(self, student_id: int) -> None: ...
    
    @abstractmethod
    def get(self, student_id: int) -> Optional[StudentEntity]: ...
    
    @abstractmethod
    def list(self, nombre: Optional[str] = None) -> List[StudentEntity]: ...
