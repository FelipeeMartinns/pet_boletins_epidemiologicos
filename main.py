import pandas as pd
import streamlit as st


# data=pd.read_excel("data\\GT1-TUBERCULOSE.xlsx")
# print(data)


# # st.write("""
# # # GT1-PET SAÚDE

# # aqui:""")


# st.title('dashboard arbovirose')


# filter=st.multiselect("Selecione a o filtro:",data['INDICADORES'].unique())


# if filter:
#     data = data[data['INDICADORES'].isin(filter)]


# st.metric("teste kkkk", f'{data["2020"]}')


import pandas as pd
import streamlit as st

st.set_page_config(page_title="Boletim Epidemiológico - TB", layout="centered")

st.title("📊 Boletim Epidemiológico - Tuberculose (Parnaíba)")

# Caminho do arquivo
arquivo = "data\\GT1-TUBERCULOSE.xlsx"

# Ler o Excel
df = pd.read_excel(arquivo)

# Mostrar dados (opcional, bom pra demonstrar)
with st.expander("📄 Ver dados carregados"):
    st.dataframe(df)

# Lista de indicadores
indicadores = df["INDICADORES"].dropna().unique().tolist()

# Lista de anos (ajuste se tiver mais)
anos = [col for col in df.columns if col != "INDICADORES"]

st.divider()

# Filtros
indicador_sel = st.selectbox("Selecione o indicador", indicadores)
ano_sel = st.selectbox("Selecione o ano", anos)

# Filtrar dados
linha = df[df["INDICADORES"] == indicador_sel]

valor = linha[ano_sel].values[0]

# Mostrar indicador
st.metric(
    label=f"{indicador_sel} ({ano_sel})",
    value=valor
)

st.divider()

# Gráfico de evolução do indicador
st.subheader("📈 Evolução do indicador ao longo dos anos")

df_linha = linha.melt(
    id_vars="INDICADORES",
    var_name="Ano",
    value_name="Valor"
)

df_linha["Ano"] = df_linha["Ano"].astype(str)

st.line_chart(df_linha.set_index("Ano")["Valor"])

