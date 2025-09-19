import graphene

class CareerType(graphene.ObjectType):
    id = graphene.Int()
    codigo = graphene.String()
    nombre = graphene.String()
    facultad_id = graphene.Int()
    institucion = graphene.String()
    created_at = graphene.DateTime()
    updated_at = graphene.DateTime()
