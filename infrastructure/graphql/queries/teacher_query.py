# infrastructure/graphql/queries/teacher_query.py
import graphene
from application.use_cases.teacher_service import TeacherService
from infrastructure.graphql.types.teacher_type import TeacherType
from application.use_cases.auth.jwt_utils import admin_required

class TeachersQuery(graphene.ObjectType):
    teachers = graphene.List(TeacherType, nombre=graphene.String())
    teacher = graphene.Field(TeacherType, id=graphene.Int(required=True))

    @admin_required
    def resolve_teachers(self, info, nombre=None):
        return TeacherService.list_teachers(nombre)

    @admin_required
    def resolve_teacher(self, info, id):
        return TeacherService.get_teacher(id)
