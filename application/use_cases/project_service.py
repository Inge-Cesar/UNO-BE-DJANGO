from typing import List, Optional
from core.entities.project_entity import ProyectoEntity
from core.entities.project_member_entity import ProyectoMiembroEntity
from infrastructure.orm.project_repository_impl import ProjectRepository
from infrastructure.orm.project_member_repository_impl import ProjectMemberRepository
from application.use_cases.auditoria.audit_service import AuditService
from infrastructure.models.student_model import Student
from infrastructure.models.teacher_model import Teacher
from infrastructure.models.project_state_model import ProjectState

class ProjectService:
    repo = ProjectRepository()
    member_repo = ProjectMemberRepository()

    @staticmethod
    def create_project(actor_id: int, project: ProyectoEntity) -> ProyectoEntity:
        created = ProjectService.repo.create(project)
        AuditService.log(
            actor_id,
            "CREATE",
            "Proyectos",
            created.id,
            detalles={
                "titulo": created.titulo,
                "estudiante_id": created.estudiante_id,
                "tutor_id": created.tutor_id,
                "estado_id": created.estado_id
            }
        )
        # Agregar al creador como líder automáticamente
        leader = ProyectoMiembroEntity(
            id=None,
            proyecto_id=created.id,
            estudiante_id=created.estudiante_id,
            rol="Líder",
            es_lider=True
        )
        ProjectService.member_repo.create(leader)
        # Llenar nombres y estado para GraphQL
        created.estudiante_nombre = ProjectService._get_student_name(created.estudiante_id)
        created.tutor_nombre = ProjectService._get_teacher_name(created.tutor_id)
        created.estado_nombre = ProjectService._get_state_name(created.estado_id)
        return created

    @staticmethod
    def update_project(actor_id: int, project: ProyectoEntity) -> ProyectoEntity:
        old = ProjectService.repo.get(project.id)
        updated = ProjectService.repo.update(project)
        AuditService.log(
            actor_id,
            "UPDATE",
            "Proyectos",
            updated.id,
            detalles={
                "antes": {"titulo": old.titulo, "estado_id": old.estado_id},
                "despues": {"titulo": updated.titulo, "estado_id": updated.estado_id}
            }
        )
        # Llenar nombres y estado para GraphQL
        updated.estudiante_nombre = ProjectService._get_student_name(updated.estudiante_id)
        updated.tutor_nombre = ProjectService._get_teacher_name(updated.tutor_id)
        updated.estado_nombre = ProjectService._get_state_name(updated.estado_id)
        return updated

    @staticmethod
    def delete_project(actor_id: int, project_id: int) -> None:
        old = ProjectService.repo.get(project_id)
        ProjectService.repo.delete(project_id)
        AuditService.log(
            actor_id,
            "DELETE",
            "Proyectos",
            project_id,
            detalles={"titulo": old.titulo}
        )

    @staticmethod
    def get_project(project_id: int) -> Optional[ProyectoEntity]:
        project = ProjectService.repo.get(project_id)
        if project:
            project.estudiante_nombre = ProjectService._get_student_name(project.estudiante_id)
            project.tutor_nombre = ProjectService._get_teacher_name(project.tutor_id)
            project.estado_nombre = ProjectService._get_state_name(project.estado_id)
        return project

    @staticmethod
    def list_projects(estudiante_id: Optional[int] = None, activo: Optional[bool] = None) -> List[ProyectoEntity]:
        qs = ProjectService.repo.list()

        # Filtrar por estudiante creador
        if estudiante_id is not None:
            qs = [p for p in qs if p.estudiante_id == estudiante_id]

        # Filtrar por proyectos activos (ejemplo: estado_id == 1 es ACTIVO)
        if activo:
            qs = [p for p in qs if p.estado_id == 1]

        # Llenar nombres y estado para GraphQL
        for p in qs:
            p.estudiante_nombre = ProjectService._get_student_name(p.estudiante_id)
            p.tutor_nombre = ProjectService._get_teacher_name(p.tutor_id)
            p.estado_nombre = ProjectService._get_state_name(p.estado_id)

        return qs

    @staticmethod
    def add_member(actor_id: int, member: ProyectoMiembroEntity) -> ProyectoMiembroEntity:
        created = ProjectService.member_repo.create(member)
        AuditService.log(
            actor_id,
            "CREATE",
            "ProyectosMiembros",
            created.id,
            detalles={
                "proyecto_id": created.proyecto_id,
                "estudiante_id": created.estudiante_id,
                "rol": created.rol,
                "es_lider": created.es_lider
            }
        )
        return created

    @staticmethod
    def list_members(project_id: int) -> List[ProyectoMiembroEntity]:
        return ProjectService.member_repo.list_by_project(project_id)

    # ----------------------
    # Métodos auxiliares
    # ----------------------
    @staticmethod
    def _get_student_name(estudiante_id: int) -> Optional[str]:
        if not estudiante_id:
            return None
        student = Student.objects.filter(id=estudiante_id).first()
        return student.nombre if student else None

    @staticmethod
    def _get_teacher_name(tutor_id: Optional[int]) -> Optional[str]:
        if not tutor_id:
            return None
        teacher = Teacher.objects.filter(id=tutor_id).first()
        return teacher.nombre if teacher else None

    @staticmethod
    def _get_state_name(estado_id: Optional[int]) -> Optional[str]:
        if not estado_id:
            return None
        state = ProjectState.objects.filter(id=estado_id).first()
        return state.nombre if state else None
