
import graphene
from application.use_cases.role_service import RoleService
from application.use_cases.auth.jwt_utils import admin_required

class CreateRoleMutation(graphene.Mutation):
    class Arguments:
        nombre = graphene.String(required=True)
        descripcion = graphene.String()

    success = graphene.Boolean()
    role_id = graphene.Int()
    error = graphene.String()

    @admin_required
    def mutate(self, info, nombre, descripcion=None):
        try:
            role = RoleService.create_role(info, nombre, descripcion)
            return CreateRoleMutation(success=True, role_id=role.id)
        except Exception as e:
            return CreateRoleMutation(success=False, error=str(e))

class UpdateRoleMutation(graphene.Mutation):
    class Arguments:
        role_id = graphene.Int(required=True)
        nombre = graphene.String()
        descripcion = graphene.String()

    success = graphene.Boolean()
    error = graphene.String()

    @admin_required
    def mutate(self, info, role_id, nombre=None, descripcion=None):
        try:
            RoleService.update_role(info, role_id, nombre, descripcion)
            return UpdateRoleMutation(success=True)
        except Exception as e:
            return UpdateRoleMutation(success=False, error=str(e))

class DeleteRoleMutation(graphene.Mutation):
    class Arguments:
        role_id = graphene.Int(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    @admin_required
    def mutate(self, info, role_id):
        try:
            RoleService.delete_role(info, role_id)
            return DeleteRoleMutation(success=True)
        except Exception as e:
            return DeleteRoleMutation(success=False, error=str(e))
