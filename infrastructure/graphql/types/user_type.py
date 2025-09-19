# infrastructure/graphql/types/user_type.py
import graphene

class UserType(graphene.ObjectType):
    id = graphene.Int()
    username = graphene.String()
    email = graphene.String()
    rol_id = graphene.Int()
    activo = graphene.Boolean()
