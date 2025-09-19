import graphene
from graphene.types.datetime import Date
from application.use_cases.student_service import StudentService
from infrastructure.graphql.types.student_type import StudentType
from application.use_cases.auth.jwt_utils import admin_required


class CreateStudentMutation(graphene.Mutation):
    class Arguments:
        usuario_id = graphene.Int(required=True)
        nombre = graphene.String(required=True)
        registro = graphene.String()
        carrera_id = graphene.Int(required=True)
        semestre = graphene.Int()
        fecha_nacimiento = Date()  # ✅ ahora es un Date en vez de String
        ppa = graphene.Float()

    student = graphene.Field(StudentType)
    success = graphene.Boolean()
    error = graphene.String()

    @admin_required
    def mutate(
        self, info, usuario_id, nombre, carrera_id,
        registro=None, semestre=None, fecha_nacimiento=None, ppa=None
    ):
        actor_id = getattr(info.context, "user_id", None)
        try:
            student = StudentService.create_student(
                actor_id,
                usuario_id=usuario_id,
                nombre=nombre,
                registro=registro,
                carrera_id=carrera_id,
                semestre=semestre,
                fecha_nacimiento=fecha_nacimiento,  # ya viene como date
                ppa=ppa
            )
            return CreateStudentMutation(student=student, success=True)
        except Exception as e:
            return CreateStudentMutation(student=None, success=False, error=str(e))


class UpdateStudentMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        usuario_id = graphene.Int()
        nombre = graphene.String()
        registro = graphene.String()
        carrera_id = graphene.Int()
        semestre = graphene.Int()
        fecha_nacimiento = Date()  # ✅ cambiado a Date
        ppa = graphene.Float()

    student = graphene.Field(StudentType)
    success = graphene.Boolean()
    error = graphene.String()

    @admin_required
    def mutate(self, info, id, **kwargs):
        actor_id = getattr(info.context, "user_id", None)
        try:
            student = StudentService.update_student(actor_id, id, **kwargs)
            return UpdateStudentMutation(student=student, success=True)
        except Exception as e:
            return UpdateStudentMutation(student=None, success=False, error=str(e))


class DeleteStudentMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    @admin_required
    def mutate(self, info, id):
        actor_id = getattr(info.context, "user_id", None)
        try:
            StudentService.delete_student(actor_id, id)
            return DeleteStudentMutation(success=True)
        except Exception as e:
            return DeleteStudentMutation(success=False, error=str(e))
