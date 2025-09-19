from typing import List, Optional
from core.entities.career_entity import CareerEntity
from infrastructure.orm.career_repository_impl import CareerRepository
from application.use_cases.auditoria.audit_service import AuditService

class CareerService:
    repo = CareerRepository()

    @staticmethod
    def create_career(actor_id: int, career: CareerEntity) -> CareerEntity:
        created = CareerService.repo.create(career)
        AuditService.log(
            actor_id,
            "CREATE",
            "Carreras",
            created.id,
            detalles={
                "nombre": created.nombre,
                "codigo": getattr(created, "codigo", None),
                "facultad_id": getattr(created, "facultad_id", None),
                "institucion": getattr(created, "institucion", None)
            }
        )
        return created

    @staticmethod
    def update_career(actor_id: int, career: CareerEntity) -> CareerEntity:
        old = CareerService.repo.get(career.id)
        updated = CareerService.repo.update(career)
        AuditService.log(
            actor_id,
            "UPDATE",
            "Carreras",
            updated.id,
            detalles={
                "antes": {
                    "nombre": old.nombre,
                    "codigo": getattr(old, "codigo", None),
                    "facultad_id": getattr(old, "facultad_id", None),
                    "institucion": getattr(old, "institucion", None)
                },
                "despues": {
                    "nombre": updated.nombre,
                    "codigo": getattr(updated, "codigo", None),
                    "facultad_id": getattr(updated, "facultad_id", None),
                    "institucion": getattr(updated, "institucion", None)
                }
            }
        )
        return updated

    @staticmethod
    def delete_career(actor_id: int, career_id: int) -> None:
        old = CareerService.repo.get(career_id)
        CareerService.repo.delete(career_id)
        AuditService.log(
            actor_id,
            "DELETE",
            "Carreras",
            career_id,
            detalles={
                "nombre": old.nombre,
                "codigo": getattr(old, "codigo", None),
                "facultad_id": getattr(old, "facultad_id", None),
                "institucion": getattr(old, "institucion", None)
            }
        )

    @staticmethod
    def get_career(career_id: int) -> Optional[CareerEntity]:
        return CareerService.repo.get(career_id)

    @staticmethod
    def list_careers(nombre: str = None) -> List[CareerEntity]:
        return CareerService.repo.list(nombre)
