from classes.ControleFinanceiro import ControleFinanceiro
from classes.Receita import Receita
from classes.Despesa import Despesa

class GerenciadorFinanceiro:
    def __init__(self):
        self.transacoes = []
    
    def adicionar_transacao(self, transacao: ControleFinanceiro):
        self.transacoes.append(transacao)
    
    def dados_relatorio(self) -> list:
        dados = []
        total_despesas = 0
        total_liquido = 0
        
        for objeto in self.transacoes:
            if isinstance(objeto, Despesa):
                despesa = {
                    "data": objeto.data,
                    "tipo": "Despesa",
                    "setor": objeto.setor,
                    "valor_saida": objeto.calcular_liquido()
                }
                dados.append(despesa)
                total_despesas += despesa["valor_saida"]

            elif isinstance(objeto, Receita):
                receita = {
                    "data": objeto.data,
                    "tipo": "Receita",
                    "setor": objeto.setor,
                    "valor_bruto": objeto.valor_bruto,
                    "valor_imposto": objeto.calcular_imposto(),
                    "valor_liquido": objeto.calcular_liquido()
                }
                dados.append(receita)
                total_liquido += receita["valor_liquido"]

            else:
                print("ERRO: Tipo de transação desconhecida.")
        
        if len(dados) > 0:
            lucro = {
                "lucro": total_despesas + total_liquido
            }
            dados.append(lucro)

        return dados