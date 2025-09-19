from infrastructure.models.auditoria_model import Auditoria
import json

class AuditService:
    @staticmethod
    def log(usuario_id, accion, tabla, registro_id=None, detalles=None):
        """
        Guarda un registro de auditoría en la base de datos.
        detalles: diccionario o string con info adicional sobre el cambio.
        """
        # Si recibimos un diccionario, convertimos a JSON string
        if isinstance(detalles, dict):
            detalles = json.dumps(detalles)

        Auditoria.objects.create(
            usuario_id=usuario_id,
            accion=accion,
            tabla=tabla,
            registro_id=registro_id,
            detalles=detalles
        )
