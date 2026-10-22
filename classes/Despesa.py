from datetime import datetime
from classes.ControleFinanceiro import ControleFinanceiro

class Despesa(ControleFinanceiro):
    def __init__(self, valor_saida: float, setor: str):
        self.valor_saida = valor_saida
        self.setor = setor
        self.data = self.obter_data()

    def calcular_imposto(self) -> float:
        return 0.0

    def calcular_liquido(self) -> float:
        return -self.valor_saida

    def obter_data(self) -> str:
        return datetime.now().strftime('%d/%m/%Y às %H:%M')