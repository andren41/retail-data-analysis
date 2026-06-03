# André Nicolai Popadiuk - Turma T2
# Mini-projeto Avaliativo - Módulo 1 / Semana 7
# Data: 02/06/2026


# IMPORTAÇÕES

import csv                      # leitura nativa de CSV
from datetime import datetime   # conversão de datas

import numpy as np              # estatísticas
import pandas as pd             # manipulação de dados

# Para gráficos (OPCIONAL — descomente as 2 linhas abaixo se quiser plotar):
# import matplotlib.pyplot as plt
# import seaborn as sns


#  SPRINT 1 — IMPORTAÇÃO DOS DADOS

SEPARADOR = "=" * 65

print("\n" + SEPARADOR)
print("  SPRINT 1 — IMPORTAÇÃO DOS DADOS")
print(SEPARADOR)

# Ajuste o caminho conforme o ambiente
CAMINHO_CSV = "Base Varejo.csv"   # VsCode: caminho relativo
# CAMINHO_CSV = "/content/Base Varejo.csv"   # Google Colab

registros: list[dict] = []
cabecalho: list[str]  = []

try:
    with open(CAMINHO_CSV, encoding="utf-8", newline="") as arquivo:
        leitor = csv.DictReader(arquivo, delimiter=";")
        cabecalho = list(leitor.fieldnames or [])
        for linha in leitor:
            registros.append(dict(linha))   # cada linha → dicionário Python

    print(f"'{CAMINHO_CSV}' lido com csv.DictReader.")
    print(f"    Registros carregados : {len(registros):,}")
    print(f"    Colunas encontradas  : {cabecalho}")

except FileNotFoundError:
    print(f"Arquivo '{CAMINHO_CSV}' não encontrado.")
    print("    Ajuste a variável CAMINHO_CSV no início do script.")
    raise SystemExit(1)

# Conversão para DataFrame pandas
df = pd.DataFrame(registros)
print(f"\nDataFrame criado: {df.shape[0]:,} linhas × {df.shape[1]} colunas")
print("\nTipos de dados ANTES da limpeza:")
print(df.dtypes.to_string())


#  SPRINT 2 — TRANSFORMAÇÃO DE TIPOS DE DADOS

print("\n" + SEPARADOR)
print("  SPRINT 2 — TRANSFORMAÇÃO DE TIPOS DE DADOS")
print(SEPARADOR)

# 2.1 Remover colunas sem nome (artefatos do CSV)
colunas_lixo = [c for c in df.columns if "Unnamed" in str(c) or not str(c).strip()]
if colunas_lixo:
    df.drop(columns=colunas_lixo, inplace=True)
    print(f"Colunas inválidas removidas: {colunas_lixo}")
else:
    print("Nenhuma coluna inválida ('Unnamed') encontrada.")

# 2.2 Converter coluna DATA com o módulo datetime

def converter_data(valor_str: str):
    """
    Converte 'dd/mm/aaaa' para objeto datetime.
    Retorna None para valores inválidos ou ausentes.
    """
    try:
        return datetime.strptime(str(valor_str).strip(), "%d/%m/%Y")
    except (ValueError, TypeError):
        return None

df["DATA"] = df["DATA"].apply(converter_data)
invalidas = df["DATA"].isna().sum()
print(f"Coluna DATA → datetime (módulo datetime). Datas inválidas: {invalidas:,}")

# Colunas auxiliares para análise temporal
df["ano"] = df["DATA"].apply(lambda d: d.year  if d is not None else None)
df["mes"] = df["DATA"].apply(lambda d: d.month if d is not None else None)

# 2.3 Converter colunas que devem ser numéricas
COLUNAS_NUM = ["CO_ID", "CL_ID", "CL_EC", "CL_FHL", "PR_ID"]
for col in COLUNAS_NUM:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

print(f"Colunas numéricas convertidas: {COLUNAS_NUM}")
print("\nTipos de dados APÓS conversão:")
print(df.dtypes.to_string())


#  SPRINT 3 — LIMPEZA DE NULOS E DUPLICATAS

print("\n" + SEPARADOR)
print("  SPRINT 3 — VERIFICAÇÃO E LIMPEZA DE DADOS")
print(SEPARADOR)

# PROBLEMA 1 — Valores nulos por coluna
print("\n[PROBLEMA 1] Contagem de valores nulos por coluna:")
nulos = df.isnull().sum()
for col, qtd in nulos.items():
    alerta = "  ← requer atenção" if qtd > 0 else ""
    print(f"    {col:<14}: {qtd:>8,}{alerta}")

# PROBLEMA 2 — Linhas completamente duplicadas
dup_total = df.duplicated().sum()
print(f"\n[PROBLEMA 2] Linhas completamente duplicadas: {dup_total:,}")

# PROBLEMA 3 — Inconsistências nas colunas de categoria
INVALIDOS = {"#N/D", "", " ", "nan", "None"}
inv_cat  = df["PR_CAT"].apply(lambda v: pd.isna(v) or str(v).strip() in INVALIDOS).sum()
inv_nome = df["PR_NOME"].apply(lambda v: pd.isna(v) or str(v).strip() in INVALIDOS).sum()
print(f"\n[PROBLEMA 3] Valores '#N/D' ou vazios em PR_CAT  : {inv_cat:,}")
print(f"             Valores '#N/D' ou vazios em PR_NOME : {inv_nome:,}")


#  LIMPEZA 1 — Tratar categorias inválidas com lógica if/else

def tratar_categoria(valor) -> str:
    """Substitui categorias inválidas por 'Sem Categoria' (if/else)."""
    if pd.isna(valor) or str(valor).strip() in INVALIDOS:   # condição inválida
        return "Sem Categoria"
    else:
        return str(valor).strip()                            # valor válido

def tratar_nome_produto(valor) -> str:
    """Substitui nomes de produto inválidos por 'Sem Nome' (if/else)."""
    if pd.isna(valor) or str(valor).strip() in INVALIDOS:   # condição inválida
        return "Sem Nome"
    else:
        return str(valor).strip()                            # valor válido

df["PR_CAT"]  = df["PR_CAT"].apply(tratar_categoria)
df["PR_NOME"] = df["PR_NOME"].apply(tratar_nome_produto)

print(f"\nPR_CAT : inválidos → 'Sem Categoria'")
print(f"PR_NOME: inválidos → 'Sem Nome'")
print(f"    Categorias únicas após tratamento: {sorted(df['PR_CAT'].unique())}")


#  LIMPEZA 2 — Imputar nulos em CL_FHL (dimensão numérica)

nulos_fhl = df["CL_FHL"].isna().sum()
if nulos_fhl > 0:
    df["CL_FHL"] = df["CL_FHL"].fillna(0)
    print(f"\n{nulos_fhl:,} nulos em CL_FHL imputados com 0 (sem filhos).")
else:
    print("\nCL_FHL: nenhum nulo encontrado.")


#  LIMPEZA 3 — Remover linhas com DATA nula/inválida

antes = df.shape[0]
df.dropna(subset=["DATA"], inplace=True)
removidas_data = antes - df.shape[0]
print(f"{removidas_data:,} linhas removidas por DATA inválida/nula.")


#  LIMPEZA 4 — Eliminar duplicatas

antes = df.shape[0]
df.drop_duplicates(inplace=True)
removidas_dup = antes - df.shape[0]
print(f"{removidas_dup:,} linhas duplicadas removidas.")

# Removendo linhas onde o ID da compra (CO_ID) é nulo ou negativo

mask_invalido = df["CO_ID"].isna() | (df["CO_ID"] < 0)
inv_coid = mask_invalido.sum()
if inv_coid > 0:
    df = df[~mask_invalido].copy()
    print(f"{inv_coid:,} registros com CO_ID inválido (nulo ou negativo) removidos.")
else:
    print("CO_ID: todos os registros têm identificador válido.")

print(f"\n{'─' * 65}")
print(f"  BASE LIMPA: {df.shape[0]:,} linhas × {df.shape[1]} colunas")
print(f"{'─' * 65}")


#  SPRINT 4 — ESTATÍSTICAS DESCRITIVAS: CL_FHL (Número de Filhos)

print("\n" + SEPARADOR)
print("  SPRINT 4 — ESTATÍSTICAS DESCRITIVAS: CL_FHL (Nº de Filhos)")
print(SEPARADOR)

col_fhl = df["CL_FHL"]

media         = col_fhl.mean()
mediana       = col_fhl.median()
desvio_padrao = col_fhl.std()
moda          = col_fhl.mode()[0]
maximo        = col_fhl.max()
minimo        = col_fhl.min()
contagem      = int(col_fhl.count())
q1            = col_fhl.quantile(0.25)
q3            = col_fhl.quantile(0.75)

print(f"Média: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Desvio Padrão: {desvio_padrao:.2f}")
print(f"Moda: {moda:.2f}")
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")
print(f"Contagem: {contagem}")
print(f"1º Quartil (Q1): {q1:.2f}")
print(f"3º Quartil (Q3): {q3:.2f}")


#  SPRINT 5 — PADRÕES DE AGRUPAMENTO

print("\n" + SEPARADOR)
print("  SPRINT 5 — PADRÕES DE AGRUPAMENTO")
print(SEPARADOR)

# Agrupamento 1 — Compras por Gênero (groupby)
print("\n[AGRUPAMENTO 1] Total de compras por Gênero do Cliente:")
ag_genero = (
    df.groupby("CL_GENERO")["CO_ID"]
    .count()
    .reset_index(name="Total de Compras")
)
ag_genero["Gênero"] = ag_genero["CL_GENERO"].map({"F": "Feminino", "M": "Masculino"})
ag_genero = (
    ag_genero[["Gênero", "Total de Compras"]]
    .sort_values("Total de Compras", ascending=False)
)
print(ag_genero.to_string(index=False))

# Agrupamento 2 — Top 5 Categorias por volume (groupby)
print("\n[AGRUPAMENTO 2] Top 5 categorias por volume de compras:")
ag_cat = (
    df.groupby("PR_CAT")["CO_ID"]
    .count()
    .reset_index(name="Total")
    .sort_values("Total", ascending=False)
    .head(5)
    .rename(columns={"PR_CAT": "Categoria"})
)
print(ag_cat.to_string(index=False))

# Agrupamento 3 — Gênero × Categoria (pivot_table)
print("\n[AGRUPAMENTO 3] Compras por Gênero × Categoria (pivot_table):")
pivot_gc = pd.pivot_table(
    df,
    values="CO_ID",
    index="CL_GENERO",
    columns="PR_CAT",
    aggfunc="count",
    fill_value=0,
)
pivot_gc.index = [
    "Feminino" if g == "F" else "Masculino" for g in pivot_gc.index
]
print(pivot_gc.to_string())

# Agrupamento 4 — Compras por Segmento Social (groupby)
print("\n[AGRUPAMENTO 4] Compras por Segmento Social:")
ag_seg = (
    df.groupby("CL_SEG")["CO_ID"]
    .count()
    .reset_index(name="Compras")
    .sort_values("Compras", ascending=False)
    .rename(columns={"CL_SEG": "Segmento"})
)
print(ag_seg.to_string(index=False))


# Agrupamento 5 — Compras por Número de Filhos (groupby)
print("\n[AGRUPAMENTO 5] Compras por Número de Filhos do Cliente:")
ag_filhos = (
    df.groupby("CL_FHL")["CO_ID"]
    .count()
    .reset_index(name="Compras")
    .rename(columns={"CL_FHL": "Nº de Filhos"})
)
ag_filhos["Nº de Filhos"] = ag_filhos["Nº de Filhos"].astype(int)
print(ag_filhos.to_string(index=False))


#  SPRINT 6 — CONCLUSÕES E INSIGHTS

print("\n" + SEPARADOR)
print("  SPRINT 6 — CONCLUSÕES E INSIGHTS")
print(SEPARADOR)

# Categoria líder (para inserir dinamicamente na conclusão)
cat_lider = (
    df.groupby("PR_CAT")["CO_ID"].count().idxmax()
)

# Segmento líder (para inserir dinamicamente na conclusão)
seg_lider = (
    df.groupby("CL_SEG")["CO_ID"].count().idxmax()
)

print("1. DADOS LIMPOS")
print(f"A base começou com 830.000 linhas, mas depois de tirar os '#N/D' e colunas zoadas, ficamos com {df.shape[0]} registros válidos.")

print("\n2. CAMPEÃO DE VENDAS")
print(f"A categoria '{cat_lider}' foi a que mais vendeu de longe, seguida por HIGIENE e LIMPEZA.")

print("\n3. PÚBLICO E FILHOS")
print("As mulheres compraram mais que os homens em quase tudo.")
print(f"Em média, a galera tem {media:.2f} filhos. Mas quem mais compra é justamente o pessoal que não tem filho nenhum.")

print("\n4. CLASSE SOCIAL")
print(f"O segmento {seg_lider} é o que mais aparece comprando no mercado.")

print("\n5. OBSERVAÇÃO SOBRE A BASE")
print("Os dados estão muito proporcionais e constantes ao longo dos anos. Pode ser que essa base tenha sido gerada artificialmente para o exercício.")

print(SEPARADOR)
print("  ANÁLISE EXPLORATÓRIA CONCLUÍDA COM SUCESSO!")
print(SEPARADOR + "\n")
