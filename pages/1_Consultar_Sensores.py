import streamlit as st
import pandas as pd
from utils.api_client import get_sensores

# Função para exibir os sensores como tabela
def mostrar_sensores():
    sensores = get_sensores()
    
    if sensores:
        # Converter para DataFrame para uma tabela mais bonita
        df_sensores = pd.DataFrame(sensores)
        
        # Exibir a tabela no Streamlit
        if 'leituras' in df_sensores.columns:
            df_sensores = df_sensores.drop(columns=['leituras'])
        st.table(df_sensores)
    else:
        st.write("Não foi possível carregar os sensores.")

# Cabeçalho da página
st.title("Consultar Sensores")

# Exibir os sensores
mostrar_sensores()
