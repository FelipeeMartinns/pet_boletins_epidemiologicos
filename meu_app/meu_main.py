import streamlit as st
import pandas as pd
import formulas

# 1. Definição dos caminho
caminho_indicadores = 'meu_app\\indicadores.csv'
caminho_excel='.\\GT1-TUBERCULOSE_1.xlsx'

# 2. Carregando o CSV
@st.cache_data
def carregar_dados_csv(caminho):
    df = pd.read_csv(caminho)
    
    return df

@st.cache_data
def carregar_dados_excel(caminho):
    df=pd.read_excel(caminho)

    return df


df_indicadores=carregar_dados_csv(caminho_indicadores)
df_dados=carregar_dados_excel(caminho_excel)

# 3. Pegando a lista de nomes da coluna (Supondo que a coluna se chame 'indicadores')
lista_indicadores = df_indicadores['indicador'].unique()
lista_indicadores_formulas=df_indicadores['formulas']

anos = [col for col in df_dados.columns if col != "INDICADORES"]

st.title('GT1-TUBERCULOSE')

# 4. O selectbox recebe a lista diretamente
indicadores_select = st.multiselect('Selecione o indicador', lista_indicadores)

# st.dataframe(df_dados)

ano_select= st.multiselect('selecione os anos',anos)

