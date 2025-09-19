# core/interfaces/user_repository_interface.py
from abc import ABC, abstractmethod
from core.entities.user_entity import UserEntity
from typing import List, Optional

class UserRepositoryInterface(ABC):

    @abstractmethod
    def create(self, user_entity: UserEntity, password: str) -> UserEntity:
        raise NotImplementedError

    @abstractmethod
    def update(self, user_entity: UserEntity, password: Optional[str] = None) -> UserEntity:
        raise NotImplementedError

    @abstractmethod
    def delete(self, user_id: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[UserEntity]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[UserEntity]:
        raise NotImplementedError

    @abstractmethod
    def get_by_username(self, username: str) -> Optional[UserEntity]:
        raise NotImplementedError
