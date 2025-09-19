import graphene
from .auth_mutation import LoginMutation
from .role_mutation import CreateRoleMutation, UpdateRoleMutation, DeleteRoleMutation
from .user_mutation import CreateUserMutation, UpdateUserMutation, DeleteUserMutation
from .faculty_mutation import CreateFacultyMutation, UpdateFacultyMutation, DeleteFacultyMutation
from .career_mutation import CreateCareerMutation, UpdateCareerMutation, DeleteCareerMutation
from .student_mutation import CreateStudentMutation, UpdateStudentMutation, DeleteStudentMutation
from .teacher_mutation import CreateTeacherMutation, UpdateTeacherMutation, DeleteTeacherMutation
from .materia_mutation import CreateMateriaMutation, UpdateMateriaMutation, DeleteMateriaMutation
from .inscription_mutation import CreateInscriptionMutation, UpdateInscriptionMutation, DeleteInscriptionMutation
from .project_mutations import CreateProjectMutation, UpdateProjectMutation, DeleteProjectMutation, AddProjectMemberMutation


class Mutation(graphene.ObjectType):
    # Auth
    login = LoginMutation.Field()

    # Roles
    create_role = CreateRoleMutation.Field()
    update_role = UpdateRoleMutation.Field()
    delete_role = DeleteRoleMutation.Field()

    # Usuarios
    create_user = CreateUserMutation.Field()
    update_user = UpdateUserMutation.Field()
    delete_user = DeleteUserMutation.Field()
    
    # Facultades
    create_faculty = CreateFacultyMutation.Field()
    update_faculty = UpdateFacultyMutation.Field()
    delete_faculty = DeleteFacultyMutation.Field()
    
    # Carreras
    create_career = CreateCareerMutation.Field()
    update_career = UpdateCareerMutation.Field()
    delete_career = DeleteCareerMutation.Field()
    
    # Estudiantes
    create_student = CreateStudentMutation.Field()
    update_student = UpdateStudentMutation.Field()
    delete_student = DeleteStudentMutation.Field()
    
    # Profesores
    create_teacher = CreateTeacherMutation.Field()
    update_teacher = UpdateTeacherMutation.Field()
    delete_teacher = DeleteTeacherMutation.Field()
    
    # Materias
    create_materia = CreateMateriaMutation.Field()
    update_materia = UpdateMateriaMutation.Field()
    delete_materia = DeleteMateriaMutation.Field()
    
    # Inscripciones
    create_inscription = CreateInscriptionMutation.Field()
    update_inscription = UpdateInscriptionMutation.Field()
    delete_inscription = DeleteInscriptionMutation.Field()
    
    
    # Proyectos
    create_project = CreateProjectMutation.Field()
    update_project = UpdateProjectMutation.Field()
    delete_project = DeleteProjectMutation.Field()
    add_project_member = AddProjectMemberMutation.Field()
    
    
    
    
    
