import graphene
from graphene import relay
from graphene.types.datetime import Date
from graphene.types.generic import GenericScalar

class ProyectoType(graphene.ObjectType):
    id = graphene.Int()
    estudiante_id = graphene.Int()
    tutor_id = graphene.Int()
    titulo = graphene.String()
    descripcion = graphene.String()
    estado_id = graphene.Int()
    fecha_inicio = Date()
    fecha_fin = Date()
    created_at = Date()
    updated_at = Date()

    # Campos para los nombres, llenados desde ProjectService
    estudiante_nombre = graphene.String()
    tutor_nombre = graphene.String()
    estado_nombre = graphene.String()

class ProyectoMiembroType(graphene.ObjectType):
    id = graphene.Int()
    proyecto_id = graphene.Int()
    estudiante_id = graphene.Int()
    rol = graphene.String()
    es_lider = graphene.Boolean()
