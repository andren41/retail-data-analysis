Instruções de Execução — Mini-Projeto Varejo
Aluno: André Nicolai Popadiuk | Turma: T2 | Disciplina: Análise de Dados com Python

Pré-requisitos

* Python 3.8 ou superior instalado
* pip

Instalação das Dependências

Abra o terminal e execute:
pip install pandas numpy

Nota: As bibliotecas csv e datetime são nativas do Python, portanto não precisam de instalação.

Execução no VsCode (recomendado)

1. Clone ou baixe este repositório.
2. Abra a pasta Miniprojeto_AndreNicolaiPopadiuk_T2 no VsCode.
3. Confirme que o arquivo Base Varejo.csv está na mesma pasta que miniprojeto.py.
4. Abra o terminal integrado e execute:
python miniprojeto.py

Execução no Google Colab

1. Acesse colab.research.google.com
2. Crie um novo notebook (+ Novo notebook).
3. Na célula inicial, faça o upload do CSV executando o seguinte código:

from google.colab import files
files.upload() (selecione 'Base Varejo.csv')

4. Cole o conteúdo de miniprojeto.py nas células seguintes.
5. Ajuste a variável CAMINHO_CSV no script para:

CAMINHO_CSV = "/content/Base Varejo.csv"

6. Execute todas as células (Ctrl + F9).

Saída Esperada

O script imprime no terminal:
Sprint 1 -> Confirmação de leitura (registros e colunas)
Sprint 2 -> Tipos de dados antes e após conversão
Sprint 3 -> Relatório de qualidade (nulos, duplicatas, inconsistências)
Sprint 4 -> Tabela de estatísticas descritivas (CL_FHL)
Sprint 5 -> 5 tabelas de agrupamento (groupby e pivot_table)
Sprint 6 -> 6 insights principais da análise

Tempo de execução estimado: 1 a 3 minutos (base com aproximadamente 830.000 linhas).

Arquivo de Dados

A base Base Varejo.csv está disponível em:

* Este repositório (pasta raiz)
* Kaggle: [https://www.kaggle.com/datasets/namespaiva/base-varejo/data](https://www.kaggle.com/datasets/namespaiva/base-varejo/data)