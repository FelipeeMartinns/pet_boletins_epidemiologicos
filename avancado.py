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

st.title("GT1-PET - Tuberculose (Parnaíba)")

arquivo = "data\\GT1-TUBERCULOSE.xlsx"

# ==========================================
# CARREGAR DADOS
# ==========================================
@st.cache_data
def carrega_arquivo():
    df = pd.read_excel(arquivo, skipfooter=1)

    # Garantir que colunas de anos sejam strings
    df.columns = df.columns.astype(str)

    return df


df = carrega_arquivo()

# ==========================================
# VER DADOS (OPCIONAL)
# ==========================================
with st.expander("📄 Ver dados carregados"):
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

# ✅ Escolher múltiplos indicadores
indicadores_sel = st.multiselect(
    "Selecione um ou mais indicadores",
    indicadores,
    default=[indicadores[0]]
)

# ✅ Escolher múltiplos anos
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

# Transformar formato wide → long
df_long = df_filtrado.melt(
    id_vars="INDICADORES",
    var_name="Ano",
    value_name="Valor"
)

# Filtrar apenas anos selecionados
df_long = df_long[df_long["Ano"].isin(anos_sel)]

# Converter valores para número
df_long["Valor"] = pd.to_numeric(df_long["Valor"], errors="coerce")

# ==========================================
# TABELA COMPARATIVA
# ==========================================
st.subheader("Tabela comparativa")

st.dataframe(df_long)

st.divider()

# ========
# GRÁFICO
# ========
st.subheader("📈 Comparação de indicadores ao longo dos anos")

grafico = alt.Chart(df_long).mark_line(point=True).encode(
    x=alt.X("Ano:N", title="Ano"),
    y=alt.Y("Valor:Q", title="Valor"),

    # ✅ Legenda embaixo + texto completo
    color=alt.Color(
        "INDICADORES:N",
        title="Indicadores",
        legend=alt.Legend(
            orient="bottom",
            direction="horizontal",
            labelLimit=2000   # ✅ NÃO corta texto
        )
    ),

    # Tooltip completo
    tooltip=[
        alt.Tooltip("INDICADORES:N", title="Indicador completo"),
        alt.Tooltip("Ano:N", title="Ano"),
        alt.Tooltip("Valor:Q", title="Valor")
    ]
).properties(
    width=750,
    height=450
)

st.altair_chart(grafico, use_container_width=True)
