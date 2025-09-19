import graphene

class InscriptionType(graphene.ObjectType):
    id = graphene.Int()
    estudiante_id = graphene.Int()
    materia_id = graphene.Int()
    fecha_inscripcion = graphene.DateTime()
