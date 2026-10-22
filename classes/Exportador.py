from abc import ABC, abstractmethod

class Exportador(ABC):
    @abstractmethod
    def exportar(self, dados: list, nome_arquivo: str):
        pass