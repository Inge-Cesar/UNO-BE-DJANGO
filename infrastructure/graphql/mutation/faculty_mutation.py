import graphene
from application.use_cases.faculty_service import FacultyService
from infrastructure.graphql.types.faculty_type import FacultyType
from application.use_cases.auth.jwt_utils import admin_required

class CreateFacultyMutation(graphene.Mutation):
    class Arguments:
        nombre = graphene.String(required=True)

    faculty = graphene.Field(FacultyType)
    success = graphene.Boolean()
    error = graphene.String()

    @admin_required
    def mutate(self, info, nombre):
        actor_id = getattr(info.context, "user_id", None)
        try:
            faculty = FacultyService.create_faculty(actor_id, nombre)
            return CreateFacultyMutation(faculty=faculty, success=True)
        except Exception as e:
            return CreateFacultyMutation(faculty=None, success=False, error=str(e))

class UpdateFacultyMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        nombre = graphene.String(required=True)

    faculty = graphene.Field(FacultyType)
    success = graphene.Boolean()
    error = graphene.String()

    @admin_required
    def mutate(self, info, id, nombre):
        actor_id = getattr(info.context, "user_id", None)
        try:
            faculty = FacultyService.update_faculty(actor_id, id, nombre)
            return UpdateFacultyMutation(faculty=faculty, success=True)
        except Exception as e:
            return UpdateFacultyMutation(faculty=None, success=False, error=str(e))

class DeleteFacultyMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    @admin_required
    def mutate(self, info, id):
        actor_id = getattr(info.context, "user_id", None)
        try:
            FacultyService.delete_faculty(actor_id, id)
            return DeleteFacultyMutation(success=True)
        except Exception as e:
            return DeleteFacultyMutation(success=False, error=str(e))
