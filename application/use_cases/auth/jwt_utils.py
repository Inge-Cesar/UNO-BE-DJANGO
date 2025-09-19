import jwt
from django.conf import settings
from functools import wraps
from graphql import GraphQLError
from infrastructure.models.user_model import User

def admin_required(func):
    """
    Decorador para GraphQL mutations que solo permite usuarios Admin.
    Debe recibir token JWT en `info.context.headers['Authorization']`.
    """
    @wraps(func)
    def wrapper(self, info, *args, **kwargs):
        auth_header = info.context.headers.get('Authorization')
        if not auth_header:
            raise GraphQLError("No se proporcionó token de autenticación.")

        try:
            token_type, token = auth_header.split()
            if token_type.lower() != "bearer":
                raise GraphQLError("Formato de token inválido. Debe ser 'Bearer <token>'.")
            
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id = payload.get("user_id")
            rol = payload.get("rol")
            if rol != "Admin":
                raise GraphQLError("No tienes permisos para realizar esta acción.")
            
            # Guardamos info del usuario en context si se necesita
            info.context.user_id = user_id
            info.context.rol = rol

        except jwt.ExpiredSignatureError:
            raise GraphQLError("Token expirado. Por favor, inicia sesión nuevamente.")
        except jwt.InvalidTokenError:
            raise GraphQLError("Token inválido.")

        return func(self, info, *args, **kwargs)
    
    return wrapper
