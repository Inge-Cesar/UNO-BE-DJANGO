from typing import List, Optional
from core.entities.project_entity import ProyectoEntity
from core.interfaces.project_repository_interface import ProjectRepositoryInterface
from infrastructure.models.project_model import Proyecto

class ProjectRepository(ProjectRepositoryInterface):

    def create(self, project: ProyectoEntity) -> ProyectoEntity:
        p = Proyecto.objects.create(
            estudiante_id=project.estudiante_id,
            tutor_id=project.tutor_id,
            titulo=project.titulo,
            descripcion=project.descripcion,
            estado_id=project.estado_id,
            fecha_inicio=project.fecha_inicio,
            fecha_fin=project.fecha_fin
        )
        return ProyectoEntity(
            id=p.id,
            estudiante_id=p.estudiante_id,
            tutor_id=p.tutor_id,
            titulo=p.titulo,
            descripcion=p.descripcion,
            estado_id=p.estado_id,
            fecha_inicio=p.fecha_inicio,
            fecha_fin=p.fecha_fin,
            created_at=p.created_at,
            updated_at=p.updated_at
        )

    def update(self, project: ProyectoEntity) -> ProyectoEntity:
        p = Proyecto.objects.get(id=project.id)
        p.titulo = project.titulo
        p.descripcion = project.descripcion
        p.tutor_id = project.tutor_id
        p.estado_id = project.estado_id
        p.fecha_inicio = project.fecha_inicio
        p.fecha_fin = project.fecha_fin
        p.save()
        return ProyectoEntity(
            id=p.id,
            estudiante_id=p.estudiante_id,
            tutor_id=p.tutor_id,
            titulo=p.titulo,
            descripcion=p.descripcion,
            estado_id=p.estado_id,
            fecha_inicio=p.fecha_inicio,
            fecha_fin=p.fecha_fin,
            created_at=p.created_at,
            updated_at=p.updated_at
        )

    def delete(self, project_id: int) -> None:
        Proyecto.objects.get(id=project_id).delete()

    def get(self, project_id: int) -> Optional[ProyectoEntity]:
        try:
            p = Proyecto.objects.get(id=project_id)
            return ProyectoEntity(
                id=p.id,
                estudiante_id=p.estudiante_id,
                tutor_id=p.tutor_id,
                titulo=p.titulo,
                descripcion=p.descripcion,
                estado_id=p.estado_id,
                fecha_inicio=p.fecha_inicio,
                fecha_fin=p.fecha_fin,
                created_at=p.created_at,
                updated_at=p.updated_at
            )
        except Proyecto.DoesNotExist:
            return None

    def list(self) -> List[ProyectoEntity]:
        qs = Proyecto.objects.all()
        return [
            ProyectoEntity(
                id=p.id,
                estudiante_id=p.estudiante_id,
                tutor_id=p.tutor_id,
                titulo=p.titulo,
                descripcion=p.descripcion,
                estado_id=p.estado_id,
                fecha_inicio=p.fecha_inicio,
                fecha_fin=p.fecha_fin,
                created_at=p.created_at,
                updated_at=p.updated_at
            ) for p in qs
        ]
