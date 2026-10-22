from classes.Exportador import Exportador
import json

class ExportadorJSON(Exportador):
    def exportar(self, dados: list, nome_arquivo: str = "dados_financeiros.json"):
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
            
        print(f"Dados estruturados em JSON gerados: {nome_arquivo}")