# infrastructure/orm/user_repository_impl.py
from typing import List, Optional
from core.entities.user_entity import UserEntity
from core.interfaces.user_repository_interface import UserRepositoryInterface
from infrastructure.models.user_model import User as UserModel
from django.contrib.auth.hashers import make_password

class UserRepositoryImpl(UserRepositoryInterface):

    def _to_entity(self, u: UserModel) -> UserEntity:
        return UserEntity(
            id=u.id,
            username=u.username,
            email=u.email,
            rol_id=(u.rol.id if u.rol else None),
            activo=u.activo,
            ultimo_login=u.ultimo_login,
            created_at=u.created_at,
            deleted_at=u.deleted_at
        )

    def create(self, user_entity: UserEntity, password: str) -> UserEntity:
        user = UserModel.objects.create(
            username=user_entity.username,
            password=make_password(password),
            email=user_entity.email,
            rol_id=user_entity.rol_id,
            activo=user_entity.activo
        )
        user_entity.id = user.id
        user_entity.created_at = user.created_at
        return user_entity

    def update(self, user_entity: UserEntity, password: Optional[str] = None) -> UserEntity:
        user = UserModel.objects.get(id=user_entity.id)
        user.username = user_entity.username
        user.email = user_entity.email
        user.rol_id = user_entity.rol_id
        user.activo = user_entity.activo
        if password:
            user.password = make_password(password)
        user.save()
        return self._to_entity(user)

    def delete(self, user_id: int) -> None:
        user = UserModel.objects.get(id=user_id)
        user.delete()

    def list(self) -> List[UserEntity]:
        qs = UserModel.objects.select_related('rol').all()
        return [self._to_entity(u) for u in qs]

    def get_by_id(self, user_id: int) -> Optional[UserEntity]:
        try:
            u = UserModel.objects.select_related('rol').get(id=user_id)
            return self._to_entity(u)
        except UserModel.DoesNotExist:
            return None

    def get_by_username(self, username: str) -> Optional[UserEntity]:
        try:
            u = UserModel.objects.select_related('rol').get(username=username)
            return self._to_entity(u)
        except UserModel.DoesNotExist:
            return None
