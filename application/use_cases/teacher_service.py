# application/use_cases/teacher_service.py
from typing import List, Optional
from core.entities.teacher_entity import TeacherEntity
from infrastructure.orm.teacher_repository_impl import TeacherRepository
from application.use_cases.auditoria.audit_service import AuditService

class TeacherService:
    repo = TeacherRepository()

    @staticmethod
    def create_teacher(actor_id: int, teacher: TeacherEntity) -> TeacherEntity:
        created = TeacherService.repo.create(teacher)
        AuditService.log(
            actor_id,
            "CREATE",
            "Docentes",
            created.id,
            detalles={"nombre": created.nombre, "especialidad": created.especialidad}
        )
        return created

    @staticmethod
    def update_teacher(actor_id: int, teacher: TeacherEntity) -> TeacherEntity:
        old = TeacherService.repo.get(teacher.id)
        updated = TeacherService.repo.update(teacher)
        AuditService.log(
            actor_id,
            "UPDATE",
            "Docentes",
            updated.id,
            detalles={
                "antes": {"nombre": old.nombre, "especialidad": old.especialidad},
                "despues": {"nombre": updated.nombre, "especialidad": updated.especialidad}
            }
        )
        return updated

    @staticmethod
    def delete_teacher(actor_id: int, teacher_id: int) -> None:
        old = TeacherService.repo.get(teacher_id)
        TeacherService.repo.delete(teacher_id)
        AuditService.log(
            actor_id,
            "DELETE",
            "Docentes",
            teacher_id,
            detalles={"nombre": old.nombre, "especialidad": old.especialidad}
        )

    @staticmethod
    def get_teacher(teacher_id: int) -> Optional[TeacherEntity]:
        return TeacherService.repo.get(teacher_id)

    @staticmethod
    def list_teachers(nombre: str = None) -> List[TeacherEntity]:
        return TeacherService.repo.list(nombre)
