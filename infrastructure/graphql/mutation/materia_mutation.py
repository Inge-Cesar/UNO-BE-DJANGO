
import graphene
from application.use_cases.materia_service import MateriaService
from core.entities.materia_entity import MateriaEntity
from infrastructure.graphql.types.materia_type import MateriaType
from application.use_cases.auth.jwt_utils import admin_required

class CreateMateriaMutation(graphene.Mutation):
    class Arguments:
        carrera_id = graphene.Int(required=True)
        codigo = graphene.String(required=False)
        nombre = graphene.String(required=True)
        creditos = graphene.Int(required=False)
        semestreMateria = graphene.Int(required=False)

    success = graphene.Boolean()
    materia = graphene.Field(MateriaType)
    error = graphene.String()

    @admin_required
    def mutate(self, info, carrera_id, nombre, codigo=None, creditos=None, semestreMateria=None):
        try:
            materia = MateriaEntity(
                id=None,
                carrera_id=carrera_id,
                codigo=codigo,
                nombre=nombre,
                creditos=creditos,
                semestre_materia=semestreMateria
            )
            new_materia = MateriaService.create_materia(actor_id=info.context.user.id, materia=materia)
            return CreateMateriaMutation(success=True, materia=new_materia)
        except Exception as e:
            return CreateMateriaMutation(success=False, error=str(e))

class UpdateMateriaMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        carrera_id = graphene.Int(required=False)
        codigo = graphene.String(required=False)
        nombre = graphene.String(required=True)
        creditos = graphene.Int(required=False)
        semestreMateria = graphene.Int(required=False)

    success = graphene.Boolean()
    materia = graphene.Field(MateriaType)
    error = graphene.String()

    @admin_required
    def mutate(self, info, id, nombre, carrera_id=None, codigo=None, creditos=None, semestreMateria=None):
        try:
            materia = MateriaEntity(
                id=id,
                carrera_id=carrera_id,
                codigo=codigo,
                nombre=nombre,
                creditos=creditos,
                semestre_materia=semestreMateria
            )
            updated_materia = MateriaService.update_materia(actor_id=info.context.user.id, materia=materia)
            return UpdateMateriaMutation(success=True, materia=updated_materia)
        except Exception as e:
            return UpdateMateriaMutation(success=False, error=str(e))

class DeleteMateriaMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    @admin_required
    def mutate(self, info, id):
        try:
            MateriaService.delete_materia(actor_id=info.context.user.id, materia_id=id)
            return DeleteMateriaMutation(success=True)
        except Exception as e:
            return DeleteMateriaMutation(success=False, error=str(e))


