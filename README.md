# 📊 Sistema de Gerenciamento Financeiro (Finan-as)

Um sistema backend em Python desenvolvido com foco em **Programação Orientada a Objetos (POO)** e boas práticas de arquitetura de software para consolidação, cálculo de tributação e exportação de relatórios financeiros corporativos.

---

## 🛠️ Arquitetura e Padrões de Projeto

O projeto utiliza conceitos fundamentais de POO para garantir manutenibilidade, extensibilidade e desacoplamento de código:

- **Abstração & Interfaces (Classes Abstratas):**
  - `ControleFinanceiro`: Define a interface padrão para movimentações financeiras (`calcular_imposto`, `calcular_liquido`, `obter_data`).
  - `Exportador`: Define o contrato para serviços de exportação de relatórios.
- **Polimorfismo:** Trata `Receita` e `Despesa` de maneira uniforme via a interface `ControleFinanceiro`, além de permitir diferentes implementações para o formato de exportação de dados.
- **Princípio Aberto/Fechado (OCP - SOLID):** Novos formatos de exportação (ex: CSV, PDF) podem ser adicionados implementando a interface `Exportador`, sem alterar a regra de negócio central.

---

## ⚙️ Regras de Negócio e Funcionalidades

1. **Gestão de Transações:**
   - **Receitas:** Registra entradas brutas, associando ao setor e calculando automaticamente o imposto e o valor líquido.
   - **Despesas:** Registra saídas financeiras associadas ao setor responsável.
2. **Cálculo Progressivo de Impostos (Tributação):**
   - **Até R$ 6.000,00:** Alíquota de **8%**
   - **De R$ 6.000,01 a R$ 29.999,99:** Alíquota de **24%**
   - **A partir de R$ 30.000,00:** Alíquota de **35%**
3. **Exportação Multi-formato:**
   - **Excel (`.xlsx`):** Formatação automática de colunas para melhor leitura e legibilidade.
   - **JSON (`.json`):** Exportação estruturada no padrão UTF-8.
4. **Interface CLI Interativa:** Menu dinâmico via terminal para inserção de transações e geração de relatórios em tempo real.

---

## 📂 Estrutura do Projeto

```text
.
├── classes/
│   ├── ControleFinanceiro.py   # Classe abstrata base para transações
│   ├── Receita.py              # Classe para receitas e regras de imposto
│   ├── Despesa.py              # Classe para despesas
│   ├── GerenciadorFinanceiro.py # Classe responsável pelo acúmulo e balanço
│   ├── Exportador.py           # Classe abstrata base para exportação
│   ├── ExportadorExcel.py      # Implementação para exportação em Excel
│   └── ExportadorJSON.py       # Implementação para exportação em JSON
├── main.py                     # Ponto de entrada do sistema (CLI / Testes)
├── requirements.txt            # Dependências do projeto
└── README.md                   # Documentação do projeto
```

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

- **Python 3.8** ou superior instalado.

### 1. Clonar o Repositório

```bash
git clone https://github.com/juannl1/finan-as.git
cd finan-as
```

### 2. Configurar o Ambiente Virtual (Opcional, mas recomendado)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / MacOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar as Dependências

```bash
pip install -r requirements.txt
```

### 4. Executar a Aplicação

```bash
python main.py
```

---

## 📊 Exemplo da Estrutura do Relatório Gerado (JSON)

```json
[
    {
        "data": "21/10/2026 às 21:00",
        "tipo": "Receita",
        "setor": "TI",
        "valor_bruto": 10000.0,
        "valor_imposto": 2400.0,
        "valor_liquido": 7600.0
    },
    {
        "data": "21/10/2026 às 21:05",
        "tipo": "Despesa",
        "setor": "Infraestrutura",
        "valor_saida": -2500.0
    },
    {
        "lucro": 5100.0
    }
]
```

---

## ✒️ Autor

Desenvolvido por **[Juan](https://github.com/juannl1)**.