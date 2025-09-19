# infrastructure/graphql/queries/user_queries.py
import graphene
from application.use_cases.user_service import UserService
from application.use_cases.auth.jwt_utils import admin_required
from infrastructure.graphql.types.user_type import UserType

class UsersQuery(graphene.ObjectType):
    users = graphene.List(UserType, username=graphene.String(), email=graphene.String())
    user = graphene.Field(UserType, id=graphene.Int(), username=graphene.String())

    @admin_required
    def resolve_users(self, info, username=None, email=None):
        qs = UserService.list_users()
        # qs es lista de UserEntity; filtramos en Python
        if username:
            qs = [u for u in qs if username.lower() in u.username.lower()]
        if email:
            qs = [u for u in qs if email.lower() in u.email.lower()]
        return qs
    
    @admin_required
    def resolve_user(self, info, id=None, username=None):
        qs = UserService.list_users()
        if id is not None:
            return next((u for u in qs if u.id == id), None)
        if username is not None:
            return next((u for u in qs if u.username.lower() == username.lower()), None)
        return None
