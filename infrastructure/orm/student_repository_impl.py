from typing import List, Optional
from core.entities.student_entity import StudentEntity
from core.interfaces.student_repository_interface import StudentRepositoryInterface
from infrastructure.models.student_model import Student

class StudentRepository(StudentRepositoryInterface):

    def create(self, student: StudentEntity) -> StudentEntity:
        s = Student.objects.create(
            usuario_id=student.usuario_id,
            nombre=student.nombre,
            registro=student.registro,
            carrera_id=student.carrera_id,
            semestre=student.semestre,
            fecha_nacimiento=student.fecha_nacimiento,
            ppa=student.ppa
        )
        return StudentEntity(
            id=s.id, usuario_id=s.usuario_id, nombre=s.nombre, registro=s.registro,
            carrera_id=s.carrera_id, semestre=s.semestre, fecha_nacimiento=s.fecha_nacimiento,
            ppa=s.ppa, created_at=s.created_at, updated_at=s.updated_at
        )

    def update(self, student: StudentEntity) -> StudentEntity:
        s = Student.objects.get(id=student.id)
        s.usuario_id = student.usuario_id
        s.nombre = student.nombre
        s.registro = student.registro
        s.carrera_id = student.carrera_id
        s.semestre = student.semestre
        s.fecha_nacimiento = student.fecha_nacimiento
        s.ppa = student.ppa
        s.save()
        return StudentEntity(
            id=s.id, usuario_id=s.usuario_id, nombre=s.nombre, registro=s.registro,
            carrera_id=s.carrera_id, semestre=s.semestre, fecha_nacimiento=s.fecha_nacimiento,
            ppa=s.ppa, created_at=s.created_at, updated_at=s.updated_at
        )

    def delete(self, student_id: int) -> None:
        Student.objects.get(id=student_id).delete()

    def get(self, student_id: int) -> Optional[StudentEntity]:
        try:
            s = Student.objects.get(id=student_id)
            return StudentEntity(
                id=s.id, usuario_id=s.usuario_id, nombre=s.nombre, registro=s.registro,
                carrera_id=s.carrera_id, semestre=s.semestre, fecha_nacimiento=s.fecha_nacimiento,
                ppa=s.ppa, created_at=s.created_at, updated_at=s.updated_at
            )
        except Student.DoesNotExist:
            return None

    def list(self, nombre: str = None) -> List[StudentEntity]:
        qs = Student.objects.all()
        if nombre:
            qs = qs.filter(nombre__icontains=nombre)
        return [
            StudentEntity(
                id=s.id, usuario_id=s.usuario_id, nombre=s.nombre, registro=s.registro,
                carrera_id=s.carrera_id, semestre=s.semestre, fecha_nacimiento=s.fecha_nacimiento,
                ppa=s.ppa, created_at=s.created_at, updated_at=s.updated_at
            ) for s in qs
        ]
