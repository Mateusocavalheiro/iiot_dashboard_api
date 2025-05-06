import streamlit as st
import plotly.express as px
import time
from utils.api_client import get_leituras

st.title("Leituras de um Sensor")

# Input para o ID do Sensor
sensor_id = st.number_input("ID do Sensor", min_value=1, step=1)

# Criação de um espaço vazio onde o gráfico será recarregado
grafico = st.empty()

# Função para atualizar o gráfico
def atualizar_grafico():
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

        fig = px.line(data_frame=data, x='Timestamp', y='Valor', title=f"Leituras do Sensor {sensor_id}")
        
        # Exibir o gráfico no Streamlit
        grafico.plotly_chart(fig)
    else:
        st.error("Não foi possível obter as leituras ou o sensor não existe.")

# Atualizar o gráfico a cada 5 segundos
while True:
    atualizar_grafico()
    time.sleep(5)  # Aguarda 5 segundos antes de atualizar novamente
    st.experimental_rerun()  # Força a página a recarregar
