import graphene
from application.use_cases.project_service import ProjectService
from application.use_cases.auth.jwt_utils import admin_required
from infrastructure.graphql.types.project_type import ProyectoType, ProyectoMiembroType
from infrastructure.models.student_model import Student
from infrastructure.models.teacher_model import Teacher
from infrastructure.models.project_state_model import ProjectState

# ---------------------------
# Tipos estáticos para selects
# ---------------------------
class ProjectStudentType(graphene.ObjectType):
    id = graphene.Int()
    nombre = graphene.String()

class ProjectTutorType(graphene.ObjectType):
    id = graphene.Int()
    nombre = graphene.String()

class ProjectStatusType(graphene.ObjectType):
    id = graphene.Int()
    nombre = graphene.String()

# ---------------------------
# Proyectos
# ---------------------------
class ProjectsQuery(graphene.ObjectType):
    proyectos = graphene.List(
        ProyectoType,
        estudianteId=graphene.Int(required=False),
        activo=graphene.Boolean(required=False)
    )
    proyecto = graphene.Field(
        ProyectoType,
        id=graphene.Int(required=True)
    )
    project_members = graphene.List(
        ProyectoMiembroType,
        proyectoId=graphene.Int(required=True)
    )

    @admin_required
    def resolve_proyectos(self, info, estudianteId=None, activo=None):
        try:
            proyectos = ProjectService.list_projects(
                estudiante_id=estudianteId,
                activo=activo
            )
            return proyectos
        except Exception as e:
            print(f"[Error resolve_proyectos] {e}")
            return []

    @admin_required
    def resolve_proyecto(self, info, id):
        try:
            return ProjectService.get_project(id)
        except Exception as e:
            print(f"[Error resolve_proyecto] {e}")
            return None

    @admin_required
    def resolve_project_members(self, info, proyectoId):
        try:
            return ProjectService.list_members(proyectoId)
        except Exception as e:
            print(f"[Error resolve_project_members] {e}")
            return []

# ---------------------------
# Estudiantes para selects
# ---------------------------
class ProjectStudentsQuery(graphene.ObjectType):
    projectEstudiantes = graphene.List(ProjectStudentType)

    @admin_required
    def resolve_projectEstudiantes(self, info):
        try:
            return list(Student.objects.all())
        except Exception as e:
            print(f"[Error resolve_projectEstudiantes] {e}")
            return []

# ---------------------------
# Tutores para selects
# ---------------------------
class ProjectTutorsQuery(graphene.ObjectType):
    projectTutores = graphene.List(ProjectTutorType)

    @admin_required
    def resolve_projectTutores(self, info):
        try:
            return list(Teacher.objects.all())
        except Exception as e:
            print(f"[Error resolve_projectTutores] {e}")
            return []

# ---------------------------
# Estados de proyecto para selects
# ---------------------------
class ProjectStatusQuery(graphene.ObjectType):
    projectEstados = graphene.List(ProjectStatusType)

    @admin_required
    def resolve_projectEstados(self, info):
        try:
            return list(ProjectState.objects.all())
        except Exception as e:
            print(f"[Error resolve_projectEstados] {e}")
            return []

