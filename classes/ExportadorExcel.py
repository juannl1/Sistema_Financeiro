from classes.Exportador import Exportador
import pandas as pd

class ExportadorExcel(Exportador):
    def exportar(self, dados: list, nome_arquivo: str = "relatorio_financeiro.xlsx"):
        df = pd.DataFrame(dados)

        with pd.ExcelWriter(nome_arquivo, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='Planilha Financeira', index=False)
            estilizar_coluna = writer.sheets['Planilha Financeira']

            for col in estilizar_coluna.columns:
                max_len = max(len(str(cell.value or '')) for cell in col)
                letra_da_coluna = col[0].column_letter
                estilizar_coluna.column_dimensions[letra_da_coluna].width = max(max_len + 3, 12)
                
        print(f"Planilha Excel gerada: {nome_arquivo}")