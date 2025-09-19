import graphene
from application.use_cases.inscription_service import InscriptionService
from infrastructure.graphql.types.inscription_type import InscriptionType
from application.use_cases.auth.jwt_utils import admin_required

class InscriptionsQuery(graphene.ObjectType):
    inscriptions = graphene.List(InscriptionType)
    inscription = graphene.Field(InscriptionType, id=graphene.Int(required=True))

    @admin_required
    def resolve_inscriptions(self, info):
        return InscriptionService.list_inscriptions()

    @admin_required
    def resolve_inscription(self, info, id):
        return InscriptionService.get_inscription(id)
