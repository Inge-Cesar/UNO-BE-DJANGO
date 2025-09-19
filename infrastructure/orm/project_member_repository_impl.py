from typing import List
from core.entities.project_member_entity import ProyectoMiembroEntity
from core.interfaces.project_member_repository_interface import ProjectMemberRepositoryInterface
from infrastructure.models.project_member_model import ProyectoMiembro

class ProjectMemberRepository(ProjectMemberRepositoryInterface):

    def create(self, member: ProyectoMiembroEntity) -> ProyectoMiembroEntity:
        m = ProyectoMiembro.objects.create(
            proyecto_id=member.proyecto_id,
            estudiante_id=member.estudiante_id,
            rol=member.rol,
            es_lider=member.es_lider
        )
        return ProyectoMiembroEntity(
            id=m.id,
            proyecto_id=m.proyecto_id,
            estudiante_id=m.estudiante_id,
            rol=m.rol,
            es_lider=m.es_lider
        )

    def list_by_project(self, project_id: int) -> List[ProyectoMiembroEntity]:
        qs = ProyectoMiembro.objects.filter(proyecto_id=project_id)
        return [
            ProyectoMiembroEntity(
                id=m.id,
                proyecto_id=m.proyecto_id,
                estudiante_id=m.estudiante_id,
                rol=m.rol,
                es_lider=m.es_lider
            ) for m in qs
        ]
