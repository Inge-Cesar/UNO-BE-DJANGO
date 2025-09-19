import graphene
from application.use_cases.faculty_service import FacultyService
from infrastructure.graphql.types.faculty_type import FacultyType
from application.use_cases.auth.jwt_utils import admin_required

class FacultiesQuery(graphene.ObjectType):
    # Lista de facultades con filtro opcional
    faculties = graphene.List(FacultyType, nombre=graphene.String())
    # Facultad única por id o nombre
    faculty = graphene.Field(FacultyType, id=graphene.Int(), nombre=graphene.String())

    @admin_required
    def resolve_faculties(self, info, nombre=None):
        return FacultyService.list_faculties(nombre)

    @admin_required
    def resolve_faculty(self, info, id=None, nombre=None):
        # Llamamos al service para obtener todas y filtramos en Python
        qs = FacultyService.list_faculties()
        if id is not None:
            return next((f for f in qs if f.id == id), None)
        if nombre is not None:
            return next((f for f in qs if f.nombre.lower() == nombre.lower()), None)
        return None
