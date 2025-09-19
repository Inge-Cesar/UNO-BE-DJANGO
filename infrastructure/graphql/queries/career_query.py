import graphene
from application.use_cases.career_service import CareerService
from infrastructure.graphql.types.career_type import CareerType
from application.use_cases.auth.jwt_utils import admin_required

class CareersQuery(graphene.ObjectType):
    careers = graphene.List(CareerType, nombre=graphene.String())
    career = graphene.Field(CareerType, id=graphene.Int())

    @admin_required
    def resolve_careers(self, info, nombre=None):
        return CareerService.list_careers(nombre)

    @admin_required
    def resolve_career(self, info, id=None):
        return CareerService.get_career(id)
