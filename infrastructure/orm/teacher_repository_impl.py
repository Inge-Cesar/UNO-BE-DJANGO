# infrastructure/orm/teacher_repository_impl.py
from typing import List, Optional
from core.entities.teacher_entity import TeacherEntity
from core.interfaces.teacher_repository_interface import TeacherRepositoryInterface
from infrastructure.models.teacher_model import Teacher

class TeacherRepository(TeacherRepositoryInterface):

    def create(self, teacher: TeacherEntity) -> TeacherEntity:
        t = Teacher.objects.create(
            usuario_id=teacher.usuario_id,
            nombre=teacher.nombre,
            especialidad=teacher.especialidad,
            facultad=teacher.facultad
        )
        return TeacherEntity(
            id=t.id,
            usuario_id=t.usuario_id,
            nombre=t.nombre,
            especialidad=t.especialidad,
            facultad=t.facultad,
            created_at=t.created_at,
            updated_at=t.updated_at
        )

    def update(self, teacher: TeacherEntity) -> TeacherEntity:
        t = Teacher.objects.get(id=teacher.id)
        t.nombre = teacher.nombre
        t.especialidad = teacher.especialidad
        t.facultad = teacher.facultad
        t.save()
        return TeacherEntity(
            id=t.id,
            usuario_id=t.usuario_id,
            nombre=t.nombre,
            especialidad=t.especialidad,
            facultad=t.facultad,
            created_at=t.created_at,
            updated_at=t.updated_at
        )

    def delete(self, teacher_id: int) -> None:
        t = Teacher.objects.get(id=teacher_id)
        t.delete()

    def get(self, teacher_id: int) -> Optional[TeacherEntity]:
        try:
            t = Teacher.objects.get(id=teacher_id)
            return TeacherEntity(
                id=t.id,
                usuario_id=t.usuario_id,
                nombre=t.nombre,
                especialidad=t.especialidad,
                facultad=t.facultad,
                created_at=t.created_at,
                updated_at=t.updated_at
            )
        except Teacher.DoesNotExist:
            return None

    def list(self, nombre: str = None) -> List[TeacherEntity]:
        qs = Teacher.objects.all()
        if nombre:
            qs = qs.filter(nombre__icontains=nombre)
        return [
            TeacherEntity(
                id=t.id,
                usuario_id=t.usuario_id,
                nombre=t.nombre,
                especialidad=t.especialidad,
                facultad=t.facultad,
                created_at=t.created_at,
                updated_at=t.updated_at
            )
            for t in qs
        ]
