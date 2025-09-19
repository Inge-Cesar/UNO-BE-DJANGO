from typing import List, Optional
from core.entities.career_entity import CareerEntity
from core.interfaces.career_repository_interface import CareerRepositoryInterface
from infrastructure.models.career_model import Career

class CareerRepository(CareerRepositoryInterface):

    def create(self, career: CareerEntity) -> CareerEntity:
        c = Career.objects.create(
            codigo=career.codigo,
            nombre=career.nombre,
            facultad_id=career.facultad_id,
            institucion=career.institucion
        )
        return CareerEntity(
            id=c.id,
            codigo=c.codigo,
            nombre=c.nombre,
            facultad_id=c.facultad_id,
            institucion=c.institucion,
            created_at=c.created_at,
            updated_at=c.updated_at
        )

    def update(self, career: CareerEntity) -> CareerEntity:
        c = Career.objects.get(id=career.id)
        c.codigo = career.codigo
        c.nombre = career.nombre
        c.facultad_id = career.facultad_id
        c.institucion = career.institucion
        c.save()
        return CareerEntity(
            id=c.id,
            codigo=c.codigo,
            nombre=c.nombre,
            facultad_id=c.facultad_id,
            institucion=c.institucion,
            created_at=c.created_at,
            updated_at=c.updated_at
        )

    def delete(self, career_id: int) -> None:
        Career.objects.filter(id=career_id).delete()

    def get(self, career_id: int) -> Optional[CareerEntity]:
        try:
            c = Career.objects.get(id=career_id)
            return CareerEntity(
                id=c.id,
                codigo=c.codigo,
                nombre=c.nombre,
                facultad_id=c.facultad_id,
                institucion=c.institucion,
                created_at=c.created_at,
                updated_at=c.updated_at
            )
        except Career.DoesNotExist:
            return None

    def list(self, nombre: str = None) -> List[CareerEntity]:
        qs = Career.objects.all()
        if nombre:
            qs = qs.filter(nombre__icontains=nombre)
        return [
            CareerEntity(
                id=c.id,
                codigo=c.codigo,
                nombre=c.nombre,
                facultad_id=c.facultad_id,
                institucion=c.institucion,
                created_at=c.created_at,
                updated_at=c.updated_at
            )
            for c in qs
        ]
