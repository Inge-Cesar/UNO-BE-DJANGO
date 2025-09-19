from typing import List, Optional
from core.entities.inscription_entity import InscriptionEntity
from infrastructure.orm.inscription_repository_impl import InscriptionRepository
from application.use_cases.auditoria.audit_service import AuditService

class InscriptionService:
    repo = InscriptionRepository()

    @staticmethod
    def create_inscription(actor_id: int, inscription: InscriptionEntity) -> InscriptionEntity:
        created = InscriptionService.repo.create(inscription)
        AuditService.log(
            actor_id,
            "CREATE",
            "Inscripciones",
            created.id,
            detalles={"estudiante_id": created.estudiante_id, "materia_id": created.materia_id}
        )
        return created

    @staticmethod
    def update_inscription(actor_id: int, inscription: InscriptionEntity) -> InscriptionEntity:
        old = InscriptionService.repo.get(inscription.id)
        updated = InscriptionService.repo.update(inscription)
        AuditService.log(
            actor_id,
            "UPDATE",
            "Inscripciones",
            updated.id,
            detalles={
                "antes": {"estudiante_id": old.estudiante_id, "materia_id": old.materia_id},
                "despues": {"estudiante_id": updated.estudiante_id, "materia_id": updated.materia_id}
            }
        )
        return updated

    @staticmethod
    def delete_inscription(actor_id: int, inscription_id: int) -> None:
        old = InscriptionService.repo.get(inscription_id)
        InscriptionService.repo.delete(inscription_id)
        AuditService.log(
            actor_id,
            "DELETE",
            "Inscripciones",
            inscription_id,
            detalles={"estudiante_id": old.estudiante_id, "materia_id": old.materia_id}
        )

    @staticmethod
    def get_inscription(inscription_id: int) -> Optional[InscriptionEntity]:
        return InscriptionService.repo.get(inscription_id)

    @staticmethod
    def list_inscriptions() -> List[InscriptionEntity]:
        return InscriptionService.repo.list()
