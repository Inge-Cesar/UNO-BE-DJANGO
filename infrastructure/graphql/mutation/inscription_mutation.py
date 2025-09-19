import graphene
from application.use_cases.inscription_service import InscriptionService
from core.entities.inscription_entity import InscriptionEntity
from infrastructure.graphql.types.inscription_type import InscriptionType
from application.use_cases.auth.jwt_utils import admin_required

class CreateInscriptionMutation(graphene.Mutation):
    class Arguments:
        estudiante_id = graphene.Int(required=True)
        materia_id = graphene.Int(required=True)

    success = graphene.Boolean()
    inscription = graphene.Field(InscriptionType)
    error = graphene.String()

    @admin_required
    def mutate(self, info, estudiante_id, materia_id):
        try:
            inscription = InscriptionEntity(
                id=None,
                estudiante_id=estudiante_id,
                materia_id=materia_id
            )
            new_inscription = InscriptionService.create_inscription(
                actor_id=info.context.user.id,
                inscription=inscription
            )
            return CreateInscriptionMutation(success=True, inscription=new_inscription)
        except Exception as e:
            return CreateInscriptionMutation(success=False, error=str(e))

class UpdateInscriptionMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        estudiante_id = graphene.Int(required=True)
        materia_id = graphene.Int(required=True)

    success = graphene.Boolean()
    inscription = graphene.Field(InscriptionType)
    error = graphene.String()

    @admin_required
    def mutate(self, info, id, estudiante_id, materia_id):
        try:
            inscription = InscriptionEntity(
                id=id,
                estudiante_id=estudiante_id,
                materia_id=materia_id
            )
            updated_inscription = InscriptionService.update_inscription(
                actor_id=info.context.user.id,
                inscription=inscription
            )
            return UpdateInscriptionMutation(success=True, inscription=updated_inscription)
        except Exception as e:
            return UpdateInscriptionMutation(success=False, error=str(e))

class DeleteInscriptionMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    @admin_required
    def mutate(self, info, id):
        try:
            InscriptionService.delete_inscription(actor_id=info.context.user.id, inscription_id=id)
            return DeleteInscriptionMutation(success=True)
        except Exception as e:
            return DeleteInscriptionMutation(success=False, error=str(e))

