from typing import List, Optional
from core.entities.materia_entity import MateriaEntity
from infrastructure.orm.materia_repository_impl import MateriaRepository
from application.use_cases.auditoria.audit_service import AuditService

class MateriaService:
    repo = MateriaRepository()

    @staticmethod
    def create_materia(actor_id: int, materia: MateriaEntity) -> MateriaEntity:
        created = MateriaService.repo.create(materia)
        AuditService.log(
            actor_id,
            "CREATE",
            "Materias",
            created.id,
            detalles={
                "nombre": created.nombre,
                "codigo": created.codigo,
                "carrera_id": created.carrera_id
            }
        )
        return created

    @staticmethod
    def update_materia(actor_id: int, materia: MateriaEntity) -> MateriaEntity:
        old = MateriaService.repo.get(materia.id)
        updated = MateriaService.repo.update(materia)
        AuditService.log(
            actor_id,
            "UPDATE",
            "Materias",
            updated.id,
            detalles={
                "antes": {
                    "nombre": old.nombre,
                    "codigo": old.codigo,
                    "carrera_id": old.carrera_id
                },
                "despues": {
                    "nombre": updated.nombre,
                    "codigo": updated.codigo,
                    "carrera_id": updated.carrera_id
                }
            }
        )
        return updated

    @staticmethod
    def delete_materia(actor_id: int, materia_id: int) -> None:
        old = MateriaService.repo.get(materia_id)
        MateriaService.repo.delete(materia_id)
        AuditService.log(
            actor_id,
            "DELETE",
            "Materias",
            materia_id,
            detalles={
                "nombre": old.nombre,
                "codigo": old.codigo,
                "carrera_id": old.carrera_id
            }
        )

    @staticmethod
    def get_materia(materia_id: int) -> Optional[MateriaEntity]:
        return MateriaService.repo.get(materia_id)

    @staticmethod
    def list_materias(nombre: str = None) -> List[MateriaEntity]:
        return MateriaService.repo.list(nombre)
