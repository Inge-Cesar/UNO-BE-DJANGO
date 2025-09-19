# infrastructure/graphql/types/teacher_type.py
import graphene

class TeacherType(graphene.ObjectType):
    id = graphene.Int()
    usuario_id = graphene.Int()
    nombre = graphene.String()
    especialidad = graphene.String()
    facultad = graphene.String()
