import graphene

class MateriaType(graphene.ObjectType):
    id = graphene.Int()
    carrera_id = graphene.Int()
    codigo = graphene.String()
    nombre = graphene.String()
    creditos = graphene.Int()
    semestre_materia = graphene.Int()
    created_at = graphene.String()
    updated_at = graphene.String()
