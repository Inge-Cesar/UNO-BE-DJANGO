# infrastructure/graphql/mutation/teacher_mutation.py
import graphene
from application.use_cases.teacher_service import TeacherService
from core.entities.teacher_entity import TeacherEntity
from infrastructure.graphql.types.teacher_type import TeacherType
from application.use_cases.auth.jwt_utils import admin_required

class CreateTeacherMutation(graphene.Mutation):
    class Arguments:
        usuario_id = graphene.Int(required=True)
        nombre = graphene.String(required=True)
        especialidad = graphene.String(required=False)
        facultad = graphene.String(required=False)

    success = graphene.Boolean()
    teacher = graphene.Field(TeacherType)
    error = graphene.String()

    @admin_required
    def mutate(self, info, usuario_id, nombre, especialidad=None, facultad=None):
        actor_id = getattr(info.context, "user_id", None)
        try:
            teacher = TeacherEntity(
                id=None,
                usuario_id=usuario_id,
                nombre=nombre,
                especialidad=especialidad,
                facultad=facultad
            )
            new_teacher = TeacherService.create_teacher(actor_id, teacher)
            return CreateTeacherMutation(success=True, teacher=new_teacher)
        except Exception as e:
            return CreateTeacherMutation(success=False, error=str(e))

class UpdateTeacherMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        usuario_id = graphene.Int(required=False)
        nombre = graphene.String(required=True)
        especialidad = graphene.String(required=False)
        facultad = graphene.String(required=False)

    success = graphene.Boolean()
    teacher = graphene.Field(TeacherType)
    error = graphene.String()

    @admin_required
    def mutate(self, info, id, nombre, usuario_id=None, especialidad=None, facultad=None):
        actor_id = getattr(info.context, "user_id", None)
        try:
            teacher = TeacherEntity(
                id=id,
                usuario_id=usuario_id,
                nombre=nombre,
                especialidad=especialidad,
                facultad=facultad
            )
            updated_teacher = TeacherService.update_teacher(actor_id, teacher)
            return UpdateTeacherMutation(success=True, teacher=updated_teacher)
        except Exception as e:
            return UpdateTeacherMutation(success=False, error=str(e))

class DeleteTeacherMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    @admin_required
    def mutate(self, info, id):
        actor_id = getattr(info.context, "user_id", None)
        try:
            TeacherService.delete_teacher(actor_id, id)
            return DeleteTeacherMutation(success=True)
        except Exception as e:
            return DeleteTeacherMutation(success=False, error=str(e))

