from infrastructure.orm.faculty_repository_impl import FacultyRepository
from application.use_cases.auditoria.audit_service import AuditService
from core.entities.faculty_entity import FacultyEntity

faculty_repo = FacultyRepository()

class FacultyService:

    @staticmethod
    def create_faculty(actor_id: int, nombre: str) -> FacultyEntity:
        faculty = FacultyEntity(id=None, nombre=nombre)
        created = faculty_repo.create(faculty)
        AuditService.log(actor_id, "CREATE", "Faculties", created.id, {"nombre": created.nombre})
        return created

    @staticmethod
    def update_faculty(actor_id: int, faculty_id: int, nombre: str) -> FacultyEntity:
        faculty = FacultyEntity(id=faculty_id, nombre=nombre)
        updated = faculty_repo.update(faculty)
        AuditService.log(actor_id, "UPDATE", "Faculties", updated.id, {"nombre": updated.nombre})
        return updated

    @staticmethod
    def delete_faculty(actor_id: int, faculty_id: int) -> None:
        faculty_repo.delete(faculty_id)
        AuditService.log(actor_id, "DELETE", "Faculties", faculty_id, {})

    @staticmethod
    def get_faculty(faculty_id: int) -> FacultyEntity:
        return faculty_repo.get(faculty_id)

    @staticmethod
    def list_faculties(nombre: str = None):
        return faculty_repo.list(nombre)
