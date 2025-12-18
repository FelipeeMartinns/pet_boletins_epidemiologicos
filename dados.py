#processamento dos dados arquivo csv zika virus, sexo , segundo mês notificação

import pandas as pd

# 1. Nome do arquivo CSV
arquivo = "sinannet_cnv_zika.csv"

# 2. Ler o CSV
df = pd.read_csv(
    arquivo,
    sep=";",
    encoding="latin-1",
    skiprows=3
)

# 3. Mostrar as colunas
print("Colunas:")
print(df.columns)

# 4. Mostrar os primeiros dados
print("\nPrimeiras linhas:")
print(df.head())

# 5. Converter a coluna Total para número
df["Total"] = pd.to_numeric(df["Total"], errors="coerce")

# 6. Somar os casos
total_casos = df["Total"].sum()

print("\nTotal de casos no ano:", total_casos)