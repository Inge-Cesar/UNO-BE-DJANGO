# infrastructure/graphql/mutation/career_mutation.py
import graphene
from application.use_cases.career_service import CareerService
from core.entities.career_entity import CareerEntity
from infrastructure.graphql.types.career_type import CareerType
from application.use_cases.auth.jwt_utils import admin_required

class CreateCareerMutation(graphene.Mutation):
    class Arguments:
        codigo = graphene.String(required=False)
        nombre = graphene.String(required=True)
        facultad_id = graphene.Int(required=False)
        institucion = graphene.String(required=False)

    success = graphene.Boolean()
    career = graphene.Field(CareerType)
    error = graphene.String()

    @admin_required
    def mutate(self, info, nombre, codigo=None, facultad_id=None, institucion=None):
        actor_id = getattr(info.context, "user_id", None)
        try:
            career = CareerEntity(
                id=None,
                codigo=codigo,
                nombre=nombre,
                facultad_id=facultad_id,
                institucion=institucion
            )
            new_career = CareerService.create_career(actor_id, career)
            return CreateCareerMutation(success=True, career=new_career)
        except Exception as e:
            return CreateCareerMutation(success=False, error=str(e))

class UpdateCareerMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        codigo = graphene.String(required=False)
        nombre = graphene.String(required=True)
        facultad_id = graphene.Int(required=False)
        institucion = graphene.String(required=False)

    success = graphene.Boolean()
    career = graphene.Field(CareerType)
    error = graphene.String()

    @admin_required
    def mutate(self, info, id, nombre, codigo=None, facultad_id=None, institucion=None):
        actor_id = getattr(info.context, "user_id", None)
        try:
            career = CareerEntity(
                id=id,
                codigo=codigo,
                nombre=nombre,
                facultad_id=facultad_id,
                institucion=institucion
            )
            updated_career = CareerService.update_career(actor_id, career)
            return UpdateCareerMutation(success=True, career=updated_career)
        except Exception as e:
            return UpdateCareerMutation(success=False, error=str(e))

class DeleteCareerMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    @admin_required
    def mutate(self, info, id):
        actor_id = getattr(info.context, "user_id", None)
        try:
            CareerService.delete_career(actor_id, id)
            return DeleteCareerMutation(success=True)
        except Exception as e:
            return DeleteCareerMutation(success=False, error=str(e))


