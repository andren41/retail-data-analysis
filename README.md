Mini-Projeto Avaliativo — Análise de Dados com Python [T2]
Módulo 1 - Semana 07 | Curso: Análise de Dados com Python | SCTEC

Sobre o Projeto

Análise Exploratória de Dados (AED) aplicada à base "Varejo", contendo registros reais de compras (datas, clientes, produtos e categorias) de um supermercado ao longo de 4 anos (2019–2022).

O objetivo é transformar dados brutos em informações úteis por meio de carregamento, verificação de qualidade, limpeza, estatísticas descritivas e análise de padrões de agrupamento.

Estrutura do Repositório

Miniprojeto_AndreNicolaiPopadiuk_T2/
miniprojeto.py (Script principal de análise)
Base Varejo.csv (Base de dados necessária para execução)
README.md (Este arquivo com reflexão teórica e insights)
README_AndreNicolaiPopadiuk_T2.md (Instruções de execução)

Como Executar

Consulte o arquivo README_AndreNicolaiPopadiuk_T2.md para o passo a passo completo.

Resumo rápido (VsCode):
pip install pandas numpy
python miniprojeto.py

Tecnologias Utilizadas

csv (nativo): Leitura estruturada do CSV com DictReader
datetime (nativo): Conversão e validação de datas
pandas: Manipulação e análise de dados
numpy: Suporte a estatísticas

Reflexão Teórica — ETL e Qualidade de Dados

O que é ETL?

ETL (Extract, Transform, Load) é o processo fundamental de engenharia de dados que consiste em três etapas:

1. Extract (Extração): coleta de dados de uma ou mais fontes brutas (arquivos CSV, bancos de dados, APIs, etc.).
2. Transform (Transformação): limpeza, padronização, enriquecimento e reestruturação dos dados para torná-los confiáveis e utilizáveis.
3. Load (Carregamento): entrega dos dados transformados a um destino final (Data Warehouse, dashboard, modelo de ML, etc.).

Aplicação neste Projeto

Extract — Extração
Utilizamos csv.DictReader (Python nativo) para ler o arquivo Base Varejo.csv com separador de ponto e vírgula. Cada linha é extraída como um dicionário (coluna: valor), garantindo rastreabilidade e controle antes de qualquer transformação. Em seguida, convertemos para um DataFrame pandas para facilitar as operações analíticas.

Transform — Transformação
4 colunas sem nome (Unnamed) foram removidas por serem artefatos sem valor analítico.
A coluna DATA como string foi convertida com datetime.strptime, permitindo análise temporal correta.
Valores #N/D em PR_CAT e PR_NOME foram substituídos por 'Sem Categoria' e 'Sem Nome' via if/else, preservando os dados válidos do registro.
Nulos em CL_FHL (filhos) foram imputados com 0, indicando a ausência de filho registrado.
Registros com DATA inválida foram removidos, pois não é possível imputar datas de compra.
Linhas duplicadas foram removidas para evitar dupla contagem nas análises.
Valores nulos ou negativos em CO_ID foram removidos por violar a regra de negócio do identificador.

Load — Carregamento
O DataFrame limpo fica disponível em memória para todas as análises subsequentes. Pode ser exportado com df.to_csv("varejo_limpo.csv") para alimentar dashboards ou modelos de Machine Learning.

Qualidade de Dados

Dados de qualidade precisam satisfazer cinco dimensões:
Completude: sem nulos em campos críticos.
Consistência: sem valores inválidos como #N/D.
Unicidade: sem linhas duplicadas.
Validade: respeitando regras de negócio (exemplo: identificador positivo).
Pontualidade: datas convertidas e validadas.

A base Varejo apresentava problemas nas cinco dimensões, todos tratados no Sprint 3 do script.

Principais Insights da Análise

1. Qualidade: Aproximadamente 3.650 registros inválidos (0,44% da base) foram identificados e tratados antes das análises.
2. Categoria mais vendida: ALIMENTOS lidera isoladamente, seguida por HIGIENE e LIMPEZA, um padrão típico de supermercado de bairro.
3. Perfil por gênero: Clientes do sexo Feminino realizaram mais compras do que os do sexo Masculino em todas as categorias.
4. Número de filhos: A moda é 0 filhos, sendo este o público que mais compra disparado. Entre os clientes com filhos, o volume de compras se mantém estável para quem tem 1, 2 ou 3 filhos (média de 90 mil compras cada), caindo de forma mais acentuada apenas para famílias com 4 filhos.
5. Segmento social: O segmento B concentra o maior volume de compras no período analisado.
6. Consistência suspeita: As proporções entre variáveis são uniformes demais ao longo de 4 anos, sugerindo possível inflação artificial dos dados. Recomenda-se validação com a fonte primária.

Autor

André Nicolai Popadiuk — Turma T2 | SCTEC | 2026