from abc import ABC, abstractmethod


class ControleFinanceiro(ABC):
    @abstractmethod
    def calcular_imposto(self) -> float:
        pass

    @abstractmethod
    def calcular_liquido(self) -> float:
        pass

    @abstractmethod
    def obter_data(self) -> str:
        pass