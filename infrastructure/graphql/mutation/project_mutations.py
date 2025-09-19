from datetime import datetime
import graphene
from application.use_cases.project_service import ProjectService
from core.entities.project_entity import ProyectoEntity
from core.entities.project_member_entity import ProyectoMiembroEntity
from infrastructure.graphql.types.project_type import ProyectoType, ProyectoMiembroType
from application.use_cases.auth.jwt_utils import admin_required
from infrastructure.models.student_model import Student
from infrastructure.models.teacher_model import Teacher
from infrastructure.models.project_state_model import ProjectState


class CreateProjectMutation(graphene.Mutation):
    class Arguments:
        estudiante_nombre = graphene.String(required=True)
        tutor_nombre = graphene.String()
        titulo = graphene.String(required=True)
        descripcion = graphene.String()
        estado_nombre = graphene.String()
        fecha_inicio = graphene.String()
        fecha_fin = graphene.String()

    success = graphene.Boolean()
    project = graphene.Field(ProyectoType)
    error = graphene.String()

    @admin_required
    def mutate(self, info, estudiante_nombre, titulo, tutor_nombre=None, descripcion=None,
               estado_nombre=None, fecha_inicio=None, fecha_fin=None):
        try:
            # Buscar registros en la base por nombre
            estudiante = Student.objects.filter(nombre=estudiante_nombre).first()
            tutor = Teacher.objects.filter(nombre=tutor_nombre).first() if tutor_nombre else None
            estado = ProjectState.objects.filter(nombre=estado_nombre).first() if estado_nombre else None

            if not estudiante:
                return CreateProjectMutation(success=False, error=f"Estudiante '{estudiante_nombre}' no encontrado")

            # Convertir strings de fecha a datetime.date
            fecha_inicio_date = datetime.strptime(fecha_inicio, "%Y-%m-%d").date() if fecha_inicio else None
            fecha_fin_date = datetime.strptime(fecha_fin, "%Y-%m-%d").date() if fecha_fin else None

            # Crear entidad
            project = ProyectoEntity(
                id=None,
                estudiante_id=estudiante.id,
                tutor_id=tutor.id if tutor else None,
                estado_id=estado.id if estado else None,
                titulo=titulo,
                descripcion=descripcion,
                fecha_inicio=fecha_inicio_date,
                fecha_fin=fecha_fin_date
            )

            new_project = ProjectService.create_project(actor_id=info.context.user.id, project=project)
            return CreateProjectMutation(success=True, project=new_project)

        except Exception as e:
            return CreateProjectMutation(success=False, error=str(e))

class UpdateProjectMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        tutor_nombre = graphene.String()
        titulo = graphene.String(required=True)
        descripcion = graphene.String()
        estado_nombre = graphene.String()
        fecha_inicio = graphene.String()
        fecha_fin = graphene.String()

    success = graphene.Boolean()
    project = graphene.Field(ProyectoType)
    error = graphene.String()

    @admin_required
    def mutate(self, info, id, titulo, tutor_nombre=None, descripcion=None,
               estado_nombre=None, fecha_inicio=None, fecha_fin=None):
        try:
            tutor = Teacher.objects.filter(nombre=tutor_nombre).first() if tutor_nombre else None
            estado = ProjectState.objects.filter(nombre=estado_nombre).first() if estado_nombre else None

            project = ProyectoEntity(
                id=id,
                estudiante_id=None,  # No se actualiza el creador
                tutor_id=tutor.id if tutor else None,
                estado_id=estado.id if estado else None,
                titulo=titulo,
                descripcion=descripcion,
                fecha_inicio=fecha_inicio,
                fecha_fin=fecha_fin
            )
            updated_project = ProjectService.update_project(actor_id=info.context.user.id, project=project)
            return UpdateProjectMutation(success=True, project=updated_project)
        except Exception as e:
            return UpdateProjectMutation(success=False, error=str(e))


class DeleteProjectMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    @admin_required
    def mutate(self, info, id):
        try:
            ProjectService.delete_project(actor_id=info.context.user.id, project_id=id)
            return DeleteProjectMutation(success=True)
        except Exception as e:
            return DeleteProjectMutation(success=False, error=str(e))


# ---------------------------
# Miembros
# ---------------------------
class AddProjectMemberMutation(graphene.Mutation):
    class Arguments:
        proyecto_id = graphene.Int(required=True)
        estudiante_nombre = graphene.String(required=True)
        rol = graphene.String()
        es_lider = graphene.Boolean()

    success = graphene.Boolean()
    member = graphene.Field(ProyectoMiembroType)
    error = graphene.String()

    @admin_required
    def mutate(self, info, proyecto_id, estudiante_nombre, rol=None, es_lider=False):
        try:
            estudiante = Student.objects.filter(nombre=estudiante_nombre).first()
            if not estudiante:
                return AddProjectMemberMutation(success=False, error=f"Estudiante '{estudiante_nombre}' no encontrado")

            member = ProyectoMiembroEntity(
                id=None,
                proyecto_id=proyecto_id,
                estudiante_id=estudiante.id,
                rol=rol,
                es_lider=es_lider
            )
            created_member = ProjectService.add_member(actor_id=info.context.user.id, member=member)
            return AddProjectMemberMutation(success=True, member=created_member)
        except Exception as e:
            return AddProjectMemberMutation(success=False, error=str(e))
