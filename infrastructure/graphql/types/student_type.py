import graphene

class StudentType(graphene.ObjectType):
    id = graphene.Int()
    usuario_id = graphene.Int()
    nombre = graphene.String()
    registro = graphene.String()
    carrera_id = graphene.Int()
    semestre = graphene.Int()
    fecha_nacimiento = graphene.String()
    ppa = graphene.Float()
    created_at = graphene.String()
    updated_at = graphene.String()
