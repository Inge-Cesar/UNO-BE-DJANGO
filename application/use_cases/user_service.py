# application/use_cases/user_service.py
from core.entities.user_entity import UserEntity
from infrastructure.orm.user_repository_impl import UserRepositoryImpl
from application.use_cases.auditoria.audit_service import AuditService
from typing import List, Optional

class UserService:
    repo = UserRepositoryImpl()

    @staticmethod
    def create_user(actor_id: int, username: str, password: str, email: str, rol_id: int) -> UserEntity:
        # Validaciones simples (puedes ampliar)
        entity = UserEntity(id=None, username=username, email=email, rol_id=rol_id)
        created = UserService.repo.create(entity, password)
        AuditService.log(
            actor_id,
            "CREATE",
            "Usuarios",
            created.id,
            detalles={"username": created.username, "email": created.email, "rol_id": created.rol_id, "activo": created.activo}
        )
        return created

    @staticmethod
    def update_user(actor_id: int, user_id: int, username: Optional[str] = None,
                    password: Optional[str] = None, email: Optional[str] = None,
                    rol_id: Optional[int] = None, activo: Optional[bool] = None) -> UserEntity:
        existing = UserService.repo.get_by_id(user_id)
        if existing is None:
            raise ValueError("Usuario no encontrado")

        # preparar entidad con nuevos valores
        existing.username = username or existing.username
        existing.email = email or existing.email
        existing.rol_id = rol_id if rol_id is not None else existing.rol_id
        existing.activo = activo if activo is not None else existing.activo

        before = {
            "username": existing.username,
            "email": existing.email,
            "rol_id": existing.rol_id,
            "activo": existing.activo
        }

        updated = UserService.repo.update(existing, password=password)
        AuditService.log(
            actor_id,
            "UPDATE",
            "Usuarios",
            updated.id,
            detalles={"antes": before, "despues": {"username": updated.username, "email": updated.email, "rol_id": updated.rol_id, "activo": updated.activo}}
        )
        return updated

    @staticmethod
    def delete_user(actor_id: int, user_id: int) -> None:
        existing = UserService.repo.get_by_id(user_id)
        if existing is None:
            raise ValueError("Usuario no encontrado")
        # registrar datos antes de borrar
        before = {"username": existing.username, "email": existing.email, "rol_id": existing.rol_id, "activo": existing.activo}
        UserService.repo.delete(user_id)
        AuditService.log(actor_id, "DELETE", "Usuarios", user_id, detalles=before)

    @staticmethod
    def list_users() -> List[UserEntity]:
        return UserService.repo.list()

    @staticmethod
    def get_user_by_id(user_id: int) -> Optional[UserEntity]:
        return UserService.repo.get_by_id(user_id)

    @staticmethod
    def get_user_by_username(username: str) -> Optional[UserEntity]:
        return UserService.repo.get_by_username(username)
