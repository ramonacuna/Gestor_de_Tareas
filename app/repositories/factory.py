from app.repositories.base import InterfazRepositorio
from app.repositories.in_memory import MemoriaRepositorio

class RepositoryFactory:
    @staticmethod
    def create_repository() -> InterfazRepositorio:
        return MemoriaRepositorio()
