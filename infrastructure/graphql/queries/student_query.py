import graphene
from application.use_cases.student_service import StudentService
from application.use_cases.auth.jwt_utils import admin_required
from infrastructure.graphql.types.student_type import StudentType

class StudentsQuery(graphene.ObjectType):
    students = graphene.List(
        StudentType, nombre=graphene.String(), registro=graphene.String()
    )
    student = graphene.Field(
        StudentType, id=graphene.Int(), registro=graphene.String()
    )

    @admin_required
    def resolve_students(self, info, nombre=None, registro=None):
        qs = StudentService.list_students()
        # filtramos en Python igual que en usuarios
        if nombre:
            qs = [s for s in qs if nombre.lower() in s.nombre.lower()]
        if registro:
            qs = [s for s in qs if s.registro and registro.lower() in s.registro.lower()]
        return qs

    @admin_required
    def resolve_student(self, info, id=None, registro=None):
        qs = StudentService.list_students()
        if id is not None:
            return next((s for s in qs if s.id == id), None)
        if registro is not None:
            return next((s for s in qs if s.registro and s.registro.lower() == registro.lower()), None)
        return None
