import streamlit as st
import plotly.express as px
from utils.api_client import get_leituras
import time
import pandas as pd

st.set_page_config(
    layout="wide",
    page_title="Leituras do Sensor",
    page_icon="📊",
    initial_sidebar_state="collapsed",
    #menu_items={'Consultar Sensores': None}
)

query_params = st.query_params
sensor_id = int(query_params.get("sensor_id", [0])[0])  # Pega o valor ou usa 0 como padrão
tag = str(query_params.get("tag"))  # Pega o valor ou usa 0 como padrão


st.title("Leituras de um Sensor")

# Botão para consultar e recarregar as leituras

# Obtendo as leituras do sensor
leituras = get_leituras(sensor_id)
    
if leituras:
    # Exemplo de estrutura das leituras
    # Supondo que leituras seja uma lista de dicionários, onde cada dicionário tem 'timestamp' e 'valor'
    timestamps = [leitura['timestamp'] for leitura in leituras]
    valores = [leitura['valor'] for leitura in leituras]

    # Criando o gráfico
    data = {
        'Timestamp': timestamps,
        'Valor': valores
    }

    fig = px.line(data_frame=data, x='Timestamp', y='Valor', title=f"Leituras do Sensor {tag}")
        
        # Exibir o gráfico no Streamlit
    st.plotly_chart(fig)
    time.sleep(4)
else:
    st.error("Não foi possível obter as leituras ou o sensor não existe.")
    
