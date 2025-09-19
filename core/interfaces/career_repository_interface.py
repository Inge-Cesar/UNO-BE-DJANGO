from typing import List, Optional
from core.entities.career_entity import CareerEntity

class CareerRepositoryInterface:
    def create(self, career: CareerEntity) -> CareerEntity:
        raise NotImplementedError
    
    def update(self, career: CareerEntity) -> CareerEntity:
        raise NotImplementedError
    
    def delete(self, career_id: int) -> None:
        raise NotImplementedError
    
    def get(self, career_id: int) -> Optional[CareerEntity]:
        raise NotImplementedError
    
    def list(self, nombre: Optional[str] = None) -> List[CareerEntity]:
        raise NotImplementedError
