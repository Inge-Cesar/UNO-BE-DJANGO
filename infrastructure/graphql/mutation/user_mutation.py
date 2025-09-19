# infrastructure/graphql/mutation/user_mutation.py
import graphene
from application.use_cases.user_service import UserService
from application.use_cases.auth.jwt_utils import admin_required
from infrastructure.graphql.types.user_type import UserType

class CreateUserMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
        rol_id = graphene.Int(required=True)

    user = graphene.Field(UserType)
    success = graphene.Boolean()
    error = graphene.String()

    @admin_required
    def mutate(self, info, username, password, email, rol_id):
        actor_id = getattr(info.context, "user_id", None)
        try:
            user = UserService.create_user(actor_id, username, password, email, rol_id)
            return CreateUserMutation(user=user, success=True)
        except Exception as e:
            return CreateUserMutation(user=None, success=False, error=str(e))


class UpdateUserMutation(graphene.Mutation):
    class Arguments:
        user_id = graphene.Int(required=True)
        username = graphene.String()
        password = graphene.String()
        email = graphene.String()
        rol_id = graphene.Int()
        activo = graphene.Boolean()

    user = graphene.Field(UserType)
    success = graphene.Boolean()
    error = graphene.String()

    @admin_required
    def mutate(self, info, user_id, username=None, password=None, email=None, rol_id=None, activo=None):
        actor_id = getattr(info.context, "user_id", None)
        try:
            user = UserService.update_user(
                actor_id, user_id,
                username=username,
                password=password,
                email=email,
                rol_id=rol_id,
                activo=activo
            )
            return UpdateUserMutation(user=user, success=True)
        except Exception as e:
            return UpdateUserMutation(user=None, success=False, error=str(e))


class DeleteUserMutation(graphene.Mutation):
    class Arguments:
        user_id = graphene.Int(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    @admin_required
    def mutate(self, info, user_id):
        actor_id = getattr(info.context, "user_id", None)
        try:
            UserService.delete_user(actor_id, user_id)
            return DeleteUserMutation(success=True)
        except Exception as e:
            return DeleteUserMutation(success=False, error=str(e))
