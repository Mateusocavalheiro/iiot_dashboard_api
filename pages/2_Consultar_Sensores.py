import streamlit as st
import pandas as pd
from utils.api_client import get_sensores

# Função para exibir os sensores como tabela
def mostrar_sensores():
    sensores = get_sensores()
    
    if sensores:
        # Converter para DataFrame para uma tabela mais bonita
        df_sensores = pd.DataFrame(sensores)
        
        # Adicionar uma coluna com links para a página de leituras
        if 'leituras' in df_sensores.columns:
            df_sensores = df_sensores.drop(columns=['leituras'])
        df_sensores['Leituras'] = df_sensores.apply(
            lambda row: f'<a href="./Leituras_Sensor_api?sensor_id={row["id"]}&tag={row["tag"]}" target="_self">Ver Leituras</a>', axis=1
        )
        df_sensores = df_sensores.set_index('id')  # Define a coluna 'id' como índice
        st.write(df_sensores.to_html(escape=False), unsafe_allow_html=True)
    else:
        st.write("Não foi possível carregar os sensores.")

# Cabeçalho da página
st.title("Consultar Sensores")

# Exibir os sensores
mostrar_sensores()
