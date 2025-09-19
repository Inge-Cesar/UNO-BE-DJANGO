import datetime
import jwt
from django.conf import settings
from infrastructure.models.user_model import User
from django.contrib.auth.hashers import check_password, make_password

class AuthService:
    @staticmethod
    def login(username: str, password: str):
        """
        Intenta autenticar un usuario y devuelve JWT si es correcto.
        Siempre retorna diccionario con success, user_id, token y error.
        """
        try:
            user = User.objects.get(username=username, activo=True)
        except User.DoesNotExist:
            return {"success": False, "user_id": None, "token": None, "error": "Usuario no encontrado"}

        if not check_password(password, user.password):
            return {"success": False, "user_id": None, "token": None, "error": "Contraseña incorrecta"}

        # Actualizar último login
        user.ultimo_login = datetime.datetime.now()
        user.save()

        # Crear token JWT
        payload = {
            "user_id": user.id,
            "rol": user.rol.nombre if user.rol else None,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=8)
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")

        return {"success": True, "user_id": user.id, "token": token, "error": None}

    @staticmethod
    def create_user(username: str, password: str, email: str, rol_id: int):
        """
        Crea un nuevo usuario con password encriptada.
        """
        hashed_password = make_password(password)
        user = User.objects.create(
            username=username,
            password=hashed_password,
            email=email,
            rol_id=rol_id,
            activo=True
        )
        return user
