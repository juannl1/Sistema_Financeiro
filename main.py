from classes.GerenciadorFinanceiro import GerenciadorFinanceiro
from classes.Receita import Receita
from classes.Despesa import Despesa
from classes.ExportadorExcel import ExportadorExcel
from classes.ExportadorJSON import ExportadorJSON
import os

#EMOJIS: 📊✅❌⚠️
    
os.system("cls")

def testar_sistema():
    dados = [
        Receita(3500.00, "Marketing - Consultoria SEO"),
        Receita(5200.00, "Vendas - Licença de Software PME"),
        Receita(4800.00, "Suporte - Contrato de Manutenção"),
        Receita(6000.00, "RH - Workshop de Capacitação"),
        Receita(4500.00, "Design - Criação de Identidade Visual"),
        Receita(12500.00, "TI - Desenvolvimento de App Mobile"),
        Receita(8900.00, "Marketing - Campanha de Tráfego Pago"),
        Receita(14200.00, "Vendas - Lote de Equipamentos"),
        Receita(11000.00, "Infraestrutura - Migração para Nuvem"),
        Receita(15000.00, "Diretoria - Consultoria Estratégica"),
        Receita(7500.00, "Suporte - SLA Premium Mensal"),
        Receita(13000.00, "TI - Estruturação de Banco de Dados"),
        Receita(105000.00, "TI - Desenvolvimento de Software Enterprise"),
        Receita(75000.00, "Vendas - Contrato Anual de Distribuição"),
        Receita(45000.00, "Marketing - Assessoria de Marca Anual"),
        Receita(120000.00, "Diretoria - Joint Venture / Parceria Comercial"),
        Receita(62000.00, "TI - Auditoria e Segurança de Sistemas"),
        Receita(88000.00, "Vendas - Renovação de Franquias"),
        Receita(55000.00, "Infraestrutura - Cabeamento Estruturado Predial"),
        Receita(42000.00, "TI - Implantação de IA e Analytics"),

        Despesa(4000.00, "Financeiro - Taxas Bancárias e Tarifa"),
        Despesa(25000.00, "RH - Folha de Pagamento Interna"),
        Despesa(8500.00, "TI - Servidores AWS e Cloud Computing"),
        Despesa(12000.00, "Marketing - Ferramentas de Automação e CRM"),
        Despesa(6800.00, "Administrativo - Aluguel do Escritório"),
        Despesa(3500.00, "Jurídico - Honorários de Assessoria"),
        Despesa(4200.00, "RH - Benefícios e Seguro Saúde"),
        Despesa(1500.00, "TI - Licenças de Software (IDE, Office)"),
        Despesa(9300.00, "Vendas - Comissões da Equipe Comercial"),
        Despesa(5100.00, "Operações - Fretes e Entregas"),
        Despesa(2200.00, "Administrativo - Conta de Luz e Internet"),
        Despesa(15000.00, "Marketing - Compra de Mídia Adwords/Meta"),
        Despesa(1800.00, "Financeiro - Certificado Digital e Contador"),
        Despesa(3100.00, "Suporte - Telefonia e Central de Atendimento"),
        Despesa(5000.00, "RH - Compra de Cursos para Equipe")
    ]

    gerenciador = GerenciadorFinanceiro()

    for transacao in dados:
        gerenciador.adicionar_transacao(transacao)

    gerar_planilha = ExportadorExcel()
    gerar_JSON = ExportadorJSON()

    print("\n")
    gerar_planilha.exportar(gerenciador.dados_relatorio())
    gerar_JSON.exportar(gerenciador.dados_relatorio())
    print("\n")
    print("Sistema executado com sucesso !!")

def executar_sistema_usuario():

    gerenciador = GerenciadorFinanceiro()

    while True:
        print("\n" + "="*40)
        print("📊 SISTEMA DE GERENCIAMENTO FINANCEIRO 📊")
        print("="*40)
        print("1. Adicionar Receita")
        print("2. Adicionar Despesa")
        print("3. Exportar Relatórios (Excel e JSON)")
        print("0. Sair do Sistema")
        print("="*40)

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            try:
                valor_bruto = float(input("Digite o valor bruto da Receita: R$ "))

                if valor_bruto < 0:
                    raise ValueError("Valor negativo")

                setor = str(input("Digite o setor da Receita (ex: TI, Marketing): ")).title().strip()

                nova_receita = Receita(valor_bruto, setor)
                gerenciador.adicionar_transacao(nova_receita)
                print(f"\nReceita de R$ {valor_bruto:.2f} adicionada com sucesso ao setor '{setor}'!")
            except ValueError:
                print("\n❌ Erro: Por favor, insira um valor numérico válido para a receita.")

        elif opcao == '2':
            try:
                valor_saida = float(input("Digite o valor da Despesa: R$ "))

                if valor_bruto < 0:
                    raise ValueError
                
                setor = input("Digite o setor da Despesa (ex: Financeiro, RH): ")
                
                nova_despesa = Despesa(valor_saida, setor)
                gerenciador.adicionar_transacao(nova_despesa)
                print(f"\nDespesa de R$ {valor_saida:.2f} adicionada com sucesso ao setor '{setor}'!")
            except ValueError:
                print("\n❌ Erro: Por favor, insira um valor numérico válido para a despesa.")

        elif opcao == '3':
            dados_relatorio = gerenciador.dados_relatorio()

            if not dados_relatorio:
                print("\n⚠️  Não há transações cadastradas para exportar. Adicione receitas ou despesas primeiro.")
                continue
                
            try:
                gerar_planilha = ExportadorExcel()
                gerar_JSON = ExportadorJSON()
                
                gerar_planilha.exportar(dados_relatorio)
                gerar_JSON.exportar(dados_relatorio)
                print("\n✅ Relatórios exportados com sucesso! Verifique os arquivos gerados.")
                break
            except Exception as erro:
                print(f"\n❌ Ocorreu um erro ao exportar os arquivos: {erro}")

        elif opcao == '0':
            print("\nEncerrando o sistema financeiro. Até logo!\n")
            break

        else:
            print("\n❌ Opção inválida. Por favor, escolha um número entre 0 e 3.")


#testar_sistema()
executar_sistema_usuario() # Programa principal