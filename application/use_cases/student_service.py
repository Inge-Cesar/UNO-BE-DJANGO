from typing import List, Optional
from core.entities.student_entity import StudentEntity
from infrastructure.orm.student_repository_impl import StudentRepository
from application.use_cases.auditoria.audit_service import AuditService

def serialize_student(student: StudentEntity):
    return {
        "usuario_id": student.usuario_id,
        "nombre": student.nombre,
        "registro": student.registro,
        "carrera_id": student.carrera_id,
        "semestre": student.semestre,
        "fecha_nacimiento": student.fecha_nacimiento.isoformat() if student.fecha_nacimiento else None,
        "ppa": float(student.ppa) if student.ppa is not None else None
    }

class StudentService:
    repo = StudentRepository()

    @staticmethod
    def create_student(actor_id: int, **kwargs) -> StudentEntity:
        student = StudentEntity(id=None, **kwargs)
        created = StudentService.repo.create(student)
        AuditService.log(actor_id, "CREATE", "Estudiantes", created.id, detalles=serialize_student(created))
        return created

    @staticmethod
    def update_student(actor_id: int, student_id: int, **kwargs) -> StudentEntity:
        current = StudentService.repo.get(student_id)
        if not current:
            raise Exception("Estudiante no encontrado")
        old_data = serialize_student(current)
        for key, value in kwargs.items():
            if hasattr(current, key) and value is not None:
                setattr(current, key, value)
        updated = StudentService.repo.update(current)
        AuditService.log(actor_id, "UPDATE", "Estudiantes", updated.id,
                         detalles={"antes": old_data, "despues": serialize_student(updated)})
        return updated

    @staticmethod
    def delete_student(actor_id: int, student_id: int) -> None:
        old = StudentService.repo.get(student_id)
        if not old:
            raise Exception("Estudiante no encontrado")
        StudentService.repo.delete(student_id)
        AuditService.log(actor_id, "DELETE", "Estudiantes", student_id, detalles=serialize_student(old))

    # ---------------------------------------------
    # Métodos necesarios para consultas en GraphQL
    # ---------------------------------------------
    @staticmethod
    def get_student(student_id: int) -> Optional[StudentEntity]:
        return StudentService.repo.get(student_id)

    @staticmethod
    def list_students(nombre: str = None, registro: str = None) -> List[StudentEntity]:
        students = StudentService.repo.list(nombre)
        if registro:
            students = [s for s in students if s.registro and registro.lower() in s.registro.lower()]
        return students
