from typing import List, Optional
from core.entities.faculty_entity import FacultyEntity
from core.interfaces.faculty_repository_interface import FacultyRepositoryInterface
from infrastructure.models.faculty_model import Faculty

class FacultyRepository(FacultyRepositoryInterface):

    def create(self, faculty: FacultyEntity) -> FacultyEntity:
        f = Faculty.objects.create(nombre=faculty.nombre)
        return FacultyEntity(id=f.id, nombre=f.nombre, created_at=f.created_at, updated_at=f.updated_at)

    def update(self, faculty: FacultyEntity) -> FacultyEntity:
        f = Faculty.objects.get(id=faculty.id)
        f.nombre = faculty.nombre
        f.save()
        return FacultyEntity(id=f.id, nombre=f.nombre, created_at=f.created_at, updated_at=f.updated_at)

    def delete(self, faculty_id: int) -> None:
        f = Faculty.objects.get(id=faculty_id)
        f.delete()

    def get(self, faculty_id: int) -> Optional[FacultyEntity]:
        try:
            f = Faculty.objects.get(id=faculty_id)
            return FacultyEntity(id=f.id, nombre=f.nombre, created_at=f.created_at, updated_at=f.updated_at)
        except Faculty.DoesNotExist:
            return None

    def list(self, nombre: str = None) -> List[FacultyEntity]:
        qs = Faculty.objects.all()
        if nombre:
            qs = qs.filter(nombre__icontains=nombre)
        return [FacultyEntity(id=f.id, nombre=f.nombre, created_at=f.created_at, updated_at=f.updated_at) for f in qs]
