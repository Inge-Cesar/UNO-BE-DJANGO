import graphene
from application.use_cases.role_service import RoleService
from application.use_cases.auth.jwt_utils import admin_required
from infrastructure.graphql.types.role_type import RoleType

class RolesQuery(graphene.ObjectType):
    roles = graphene.List(RoleType, nombre=graphene.String())
    role = graphene.Field(RoleType, id=graphene.Int(), nombre=graphene.String())

    @admin_required
    def resolve_roles(self, info, nombre=None):
        qs = RoleService.list_roles()
        if nombre:
            qs = [r for r in qs if nombre.lower() in r.nombre.lower()]
        return qs
    
    @admin_required
    def resolve_role(self, info, id=None, nombre=None):
        qs = RoleService.list_roles()
        if id is not None:
            return next((r for r in qs if r.id == id), None)
        if nombre is not None:
            return next((r for r in qs if r.nombre.lower() == nombre.lower()), None)
        return None
