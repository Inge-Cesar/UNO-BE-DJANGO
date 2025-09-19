from typing import List, Optional
from core.entities.materia_entity import MateriaEntity
from infrastructure.models.materia_model import Materia

class MateriaRepository:

    def create(self, materia: MateriaEntity) -> MateriaEntity:
        m = Materia.objects.create(
            carrera_id=materia.carrera_id,
            codigo=materia.codigo,
            nombre=materia.nombre,
            creditos=materia.creditos,
            semestre_materia=materia.semestre_materia
        )
        return self._map_to_entity(m)

    def update(self, materia: MateriaEntity) -> MateriaEntity:
        m = Materia.objects.get(id=materia.id)
        m.carrera_id = materia.carrera_id
        m.codigo = materia.codigo
        m.nombre = materia.nombre
        m.creditos = materia.creditos
        m.semestre_materia = materia.semestre_materia
        m.save()
        return self._map_to_entity(m)

    def delete(self, materia_id: int) -> None:
        Materia.objects.filter(id=materia_id).delete()

    def get(self, materia_id: int) -> Optional[MateriaEntity]:
        try:
            m = Materia.objects.get(id=materia_id)
            return self._map_to_entity(m)
        except Materia.DoesNotExist:
            return None

    def list(self, nombre: str = None) -> List[MateriaEntity]:
        qs = Materia.objects.all()
        if nombre:
            qs = qs.filter(nombre__icontains=nombre)
        return [self._map_to_entity(m) for m in qs]

    def _map_to_entity(self, m: Materia) -> MateriaEntity:
        return MateriaEntity(
            id=m.id,
            carrera_id=m.carrera_id,
            codigo=m.codigo,
            nombre=m.nombre,
            creditos=m.creditos,
            semestre_materia=m.semestre_materia,
            created_at=m.created_at,
            updated_at=m.updated_at
        )
