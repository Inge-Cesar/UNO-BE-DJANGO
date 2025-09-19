import graphene

class FacultyType(graphene.ObjectType):
    id = graphene.Int()
    nombre = graphene.String()
