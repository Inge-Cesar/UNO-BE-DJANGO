
from core.entities.role_entity import RoleEntity
from core.interfaces.role_repository_interface import RoleRepositoryInterface
from infrastructure.models.role_model import Role

class RoleRepositoryImpl(RoleRepositoryInterface):
    def create(self, role_entity):
        role = Role.objects.create(nombre=role_entity.nombre, descripcion=role_entity.descripcion)
        role_entity.id = role.id
        return role_entity

    def update(self, role_entity):
        role = Role.objects.get(id=role_entity.id)
        role.nombre = role_entity.nombre
        role.descripcion = role_entity.descripcion
        role.save()
        return role_entity

    def delete(self, role_id):
        role = Role.objects.get(id=role_id)
        role.delete()

    def list(self):
        return [RoleEntity(r.nombre, r.descripcion, r.id) for r in Role.objects.all()]

    def get_by_id(self, role_id):
        r = Role.objects.get(id=role_id)
        return RoleEntity(r.nombre, r.descripcion, r.id)
