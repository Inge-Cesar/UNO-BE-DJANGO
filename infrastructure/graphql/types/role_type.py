# infrastructure/graphql/types/role_type.py
import graphene

class RoleType(graphene.ObjectType):
    id = graphene.Int()
    nombre = graphene.String()
    descripcion = graphene.String()
