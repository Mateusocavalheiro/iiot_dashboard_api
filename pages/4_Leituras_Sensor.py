import streamlit as st
import plotly.express as px
from utils.api_client import get_leituras

st.title("Leituras de um Sensor")

# Input para o ID do sensor
sensor_id = st.number_input("ID do Sensor", min_value=1, step=1)

# Botão para consultar e recarregar as leituras
if st.button("Consultar Leituras"):
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
        st.plotly_chart(fig)
    else:
        st.error("Não foi possível obter as leituras ou o sensor não existe.")
    
    # Botão de recarga (recarregar o gráfico)
    if st.button("Recarregar Gráfico"):
        # Ao pressionar o botão "Recarregar Gráfico", o gráfico será atualizado
        st.experimental_rerun()
