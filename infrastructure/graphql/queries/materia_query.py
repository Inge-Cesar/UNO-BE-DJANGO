import graphene
from application.use_cases.materia_service import MateriaService
from application.use_cases.auth.jwt_utils import admin_required
from infrastructure.graphql.types.materia_type import MateriaType

class MateriasQuery(graphene.ObjectType):
    materias = graphene.List(MateriaType, nombre=graphene.String())
    materia = graphene.Field(MateriaType, id=graphene.Int())

    @admin_required
    def resolve_materias(self, info, nombre=None):
        return MateriaService.list_materias(nombre)

    @admin_required
    def resolve_materia(self, info, id):
        return MateriaService.get_materia(id)
