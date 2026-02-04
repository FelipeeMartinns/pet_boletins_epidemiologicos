# import pandas as pd
# import streamlit as st
# import altair as alt

# # ==========================================
# # CONFIGURAÇÃO DA PÁGINA
# # ==========================================
# st.set_page_config(
#     page_title="Boletim Epidemiológico - TB",
#     layout="centered"
# )

# st.title("GT1-PET - Tuberculose (Parnaíba)")

# arquivo = "data\\GT1-TUBERCULOSE.xlsx"

# # ==========================================
# # CARREGAR DADOS
# # ==========================================
# @st.cache_data
# def carrega_arquivo():
#     df = pd.read_excel(arquivo, skipfooter=1)

#     # Garantir que colunas de anos sejam strings
#     df.columns = df.columns.astype(str)

#     return df


# df = carrega_arquivo()

# # ==========================================
# # VER DADOS (OPCIONAL)
# # ==========================================
# with st.expander("📄 Ver dados carregados"):
#     st.dataframe(df)

# # ==========================================
# # LISTAS
# # ==========================================
# indicadores = df["INDICADORES"].dropna().unique().tolist()
# anos = [col for col in df.columns if col != "INDICADORES"]

# st.divider()

# # ==========================================
# # FILTROS
# # ==========================================

# # ✅ Escolher múltiplos indicadores
# indicadores_sel = st.multiselect(
#     "Selecione um ou mais indicadores",
#     indicadores,
#     default=[indicadores[0]]
# )

# # ✅ Escolher múltiplos anos
# anos_sel = st.multiselect(
#     "Selecione os anos para comparação",
#     anos,
#     default=anos
# )

# st.divider()

# # ==========================================
# # FILTRAR DADOS
# # ==========================================
# df_filtrado = df[df["INDICADORES"].isin(indicadores_sel)]

# # Transformar formato wide → long
# df_long = df_filtrado.melt(
#     id_vars="INDICADORES",
#     var_name="Ano",
#     value_name="Valor"
# )

# # Filtrar apenas anos selecionados
# df_long = df_long[df_long["Ano"].isin(anos_sel)]

# # Converter valores para número
# df_long["Valor"] = pd.to_numeric(df_long["Valor"], errors="coerce")

# # ==========================================
# # TABELA COMPARATIVA
# # ==========================================
# st.subheader("Tabela comparativa")

# st.dataframe(df_long)

# st.divider()

# # ========
# # GRÁFICO
# # ========
# st.subheader("📈 Comparação de indicadores ao longo dos anos")

# grafico = alt.Chart(df_long).mark_line(point=True).encode(
#     x=alt.X("Ano:N", title="Ano"),
#     y=alt.Y("Valor:Q", title="Valor"),

#     # ✅ Legenda embaixo + texto completo
#     color=alt.Color(
#         "INDICADORES:N",
#         title="Indicadores",
#         legend=alt.Legend(
#             orient="bottom",
#             direction="horizontal",
#             labelLimit=2000   # ✅ NÃO corta texto
#         )
#     ),

#     # Tooltip completo
#     tooltip=[
#         alt.Tooltip("INDICADORES:N", title="Indicador completo"),
#         alt.Tooltip("Ano:N", title="Ano"),
#         alt.Tooltip("Valor:Q", title="Valor")
#     ]
# ).properties(
#     width=750,
#     height=450
# )

# st.altair_chart(grafico, use_container_width=True)




# import pandas as pd
# import streamlit as st
# import altair as alt

# # ==========================================
# # CONFIGURAÇÃO DA PÁGINA
# # ==========================================
# st.set_page_config(
#     page_title="Boletim Epidemiológico - TB",
#     layout="centered"
# )

# st.title("GT1-PET – Tuberculose (Parnaíba)")

# # arquivo = "data\\GT1-TUBERCULOSE.xlsx"  # ajuste se necessário
# arquivo= "GT1-TUBERCULOSE_Indicadores_calculados.xlsx"
# # ==========================================
# # DICIONÁRIO DE FÓRMULAS
# # ==========================================
# FORMULAS_INDICADORES = {
#     "Taxa de incidência de tuberculose":
#         "Fórmula: Casos novos ÷ População × 100.000",

#     "Taxa de mortalidade por tuberculose":
#         "Fórmula: Óbitos por TB ÷ População × 100.000",

#     "Proporção de cura":
#         "Fórmula: Casos encerrados como cura ÷ Casos com desfecho conhecido × 100",

#     "Coinfecção TB/HIV":
#         "Fórmula: Casos de TB com HIV positivo ÷ Casos testados para HIV × 100",

#     "Casos em populações vulneráveis":
#         "Fórmula: Soma dos casos em situação de rua, PPL, indígenas, idosos e outras condições de vulnerabilidade"
# }



# # ==========================================
# # CARREGAR DADOS
# # ==========================================
# @st.cache_data
# def carrega_arquivo():
#     df = pd.read_excel(arquivo, skipfooter=1)
#     df.columns = df.columns.astype(str)
#     return df

# df = carrega_arquivo()

# with st.expander("📄 Ver dados carregados"):
#      st.dataframe(df)
# # ==========================================
# # LISTAS
# # ==========================================
# indicadores = df["INDICADORES"].dropna().unique().tolist()
# anos = [col for col in df.columns if col != "INDICADORES"]

# st.divider()

# # ==========================================
# # FILTROS
# # ==========================================
# indicadores_sel = st.multiselect(
#     "Selecione um ou mais indicadores",
#     indicadores,
#     default=[indicadores[0]]
# )

# anos_sel = st.multiselect(
#     "Selecione os anos para comparação",
#     anos,
#     default=anos
# )

# st.divider()

# # ==========================================
# # FILTRAR DADOS
# # ==========================================
# df_filtrado = df[df["INDICADORES"].isin(indicadores_sel)]

# df_long = df_filtrado.melt(
#     id_vars="INDICADORES",
#     var_name="Ano",
#     value_name="Valor"
# )

# df_long = df_long[df_long["Ano"].isin(anos_sel)]
# df_long["Valor"] = pd.to_numeric(df_long["Valor"], errors="coerce")

# # ==========================================
# # GRÁFICO
# # ==========================================
# st.subheader("📈 Comparação de indicadores ao longo dos anos")

# grafico = alt.Chart(df_long).mark_line(point=True).encode(
#     x=alt.X("Ano:N", title="Ano"),
#     y=alt.Y("Valor:Q", title="Valor"),
#     color=alt.Color(
#         "INDICADORES:N",
#         title="Indicadores",
#         legend=alt.Legend(
#             orient="bottom",
#             direction="horizontal",
#             labelLimit=2000
#         )
#     ),
#     tooltip=[
#         alt.Tooltip("INDICADORES:N", title="Indicador"),
#         alt.Tooltip("Ano:N", title="Ano"),
#         alt.Tooltip("Valor:Q", title="Valor")
#     ]
# ).properties(
#     width=750,
#     height=450
# )

# st.altair_chart(grafico, use_container_width=True)

# # ==========================================
# # FÓRMULAS
# # ==========================================
# st.divider()
# st.subheader("Fórmula(s) do(s) indicador(es)")

# for ind in indicadores_sel:
#     nome = ind.lower()

#     if "incid" in nome:
#         formula = "Fórmula: Casos novos ÷ População × 100.000"

#     elif "mortal" in nome or "óbito" in nome or "obito" in nome:
#         formula = "Fórmula: Óbitos por TB ÷ População × 100.000"

#     elif "cura" in nome:
#         formula = "Fórmula: Casos encerrados como cura ÷ Casos com desfecho conhecido × 100"

#     elif "hiv" in nome:
#         formula = "Fórmula: Casos de TB com HIV positivo ÷ Casos testados para HIV × 100"

#     elif "vulner" in nome or "popula" in nome:
#         formula = "Fórmula: Soma dos casos em situação de rua, PPL, indígenas, idosos e outras condições de vulnerabilidade"

#     else:
#         formula = "Fórmula definida conforme protocolo da vigilância epidemiológica."

#     st.markdown(f"**{ind}**  \n{formula}")



import pandas as pd
import streamlit as st
import altair as alt

# ==========================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================
st.set_page_config(
    page_title="Boletim Epidemiológico - TB",
    layout="centered"
)

st.title("GT1-PET – Tuberculose ")

# ==========================================
# CARREGAR DADOS
# ==========================================
arquivo = "GT1-TUBERCULOSE_Indicadores_calculados.xlsx"

@st.cache_data
def carrega_arquivo():
    df = pd.read_excel(
        arquivo,
        skiprows=25   # pula tudo antes da linha "INDICADORES"
    )

    # Garantir que colunas sejam strings
    df.columns = df.columns.astype(str)

    return df


df = carrega_arquivo()

with st.expander("Ver dados carregados"):
    st.dataframe(df)

# ==========================================
# LISTAS
# ==========================================
indicadores = df["INDICADORES"].dropna().unique().tolist()
anos = [col for col in df.columns if col != "INDICADORES"]

st.divider()

# ==========================================
# FILTROS
# ==========================================
indicadores_sel = st.multiselect(
    "Selecione um ou mais indicadores",
    indicadores,
    default=[indicadores[0]]
)

anos_sel = st.multiselect(
    "Selecione os anos para comparação",
    anos,
    default=anos
)

st.divider()

# ==========================================
# FILTRAR DADOS
# ==========================================
df_filtrado = df[df["INDICADORES"].isin(indicadores_sel)]

df_long = df_filtrado.melt(
    id_vars="INDICADORES",
    var_name="Ano",
    value_name="Valor"
)

df_long = df_long[df_long["Ano"].isin(anos_sel)]
df_long["Valor"] = pd.to_numeric(df_long["Valor"], errors="coerce")

# ==========================================
# GRÁFICO (FORMATADO EM %)
# ==========================================
st.subheader("Comparação de indicadores ao longo dos anos")

grafico = alt.Chart(df_long).mark_line(point=True).encode(
    x=alt.X("Ano:N", title="Ano"),
    y=alt.Y(
        "Valor:Q",
        title="Valor (%)",
        axis=alt.Axis(format="%")
    ),
    color=alt.Color(
        "INDICADORES:N",
        title="Indicadores",
        legend=alt.Legend(
            orient="bottom",
            direction="horizontal",
            labelLimit=2000
        )
    ),
    tooltip=[
        alt.Tooltip("INDICADORES:N", title="Indicador"),
        alt.Tooltip("Ano:N", title="Ano"),
        alt.Tooltip("Valor:Q", title="Valor (%)", format=".1%")
    ]
).properties(
    width=750,
    height=450
)

st.altair_chart(grafico, use_container_width=True)

# ==========================================
# FÓRMULAS
# ==========================================
st.divider()
st.subheader("Fórmula(s) do(s) indicador(es)")

for ind in indicadores_sel:
    nome = ind.lower()

    if "incid" in nome:
        formula = "Fórmula: Casos novos ÷ População × 100.000"

    elif "mortal" in nome or "óbito" in nome or "obito" in nome:
        formula = "Fórmula: Óbitos por TB ÷ População × 100.000"

    elif "cura" in nome:
        formula = "Fórmula: Casos encerrados como cura ÷ Casos com desfecho conhecido × 100"

    elif "hiv" in nome:
        formula = "Fórmula: Casos de TB com HIV positivo ÷ Casos testados para HIV × 100"

    elif "vulner" in nome or "popula" in nome:
        formula = "Fórmula: Soma dos casos em situação de rua, PPL, indígenas, idosos e outras condições de vulnerabilidade"

    else:
        formula = "Fórmula definida conforme protocolo da vigilância epidemiológica."

    st.markdown(f"**{ind}**  \n{formula}")
