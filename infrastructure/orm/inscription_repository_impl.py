from typing import List, Optional
from core.entities.inscription_entity import InscriptionEntity
from infrastructure.models.inscription_model import Inscription

class InscriptionRepository:

    def create(self, inscription: InscriptionEntity) -> InscriptionEntity:
        i = Inscription.objects.create(
            estudiante_id=inscription.estudiante_id,
            materia_id=inscription.materia_id
        )
        return InscriptionEntity(
            id=i.id,
            estudiante_id=i.estudiante_id,
            materia_id=i.materia_id,
            fecha_inscripcion=i.fecha_inscripcion
        )

    def update(self, inscription: InscriptionEntity) -> InscriptionEntity:
        i = Inscription.objects.get(id=inscription.id)
        i.estudiante_id = inscription.estudiante_id
        i.materia_id = inscription.materia_id
        i.save()
        return InscriptionEntity(
            id=i.id,
            estudiante_id=i.estudiante_id,
            materia_id=i.materia_id,
            fecha_inscripcion=i.fecha_inscripcion
        )

    def delete(self, inscription_id: int) -> None:
        i = Inscription.objects.get(id=inscription_id)
        i.delete()

    def get(self, inscription_id: int) -> Optional[InscriptionEntity]:
        try:
            i = Inscription.objects.get(id=inscription_id)
            return InscriptionEntity(
                id=i.id,
                estudiante_id=i.estudiante_id,
                materia_id=i.materia_id,
                fecha_inscripcion=i.fecha_inscripcion
            )
        except Inscription.DoesNotExist:
            return None

    def list(self) -> List[InscriptionEntity]:
        qs = Inscription.objects.all()
        return [
            InscriptionEntity(
                id=i.id,
                estudiante_id=i.estudiante_id,
                materia_id=i.materia_id,
                fecha_inscripcion=i.fecha_inscripcion
            ) for i in qs
        ]
