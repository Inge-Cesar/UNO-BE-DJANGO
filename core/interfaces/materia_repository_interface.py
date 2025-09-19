from typing import List, Optional
from core.entities.materia_entity import MateriaEntity

class MateriaRepositoryInterface:

    def create(self, materia: MateriaEntity) -> MateriaEntity:
        raise NotImplementedError

    def update(self, materia: MateriaEntity) -> MateriaEntity:
        raise NotImplementedError

    def delete(self, materia_id: int) -> None:
        raise NotImplementedError

    def get(self, materia_id: int) -> Optional[MateriaEntity]:
        raise NotImplementedError

    def list(self, nombre: str = None) -> List[MateriaEntity]:
        raise NotImplementedError
