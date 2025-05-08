import streamlit as st
from utils.api_client import get_leituras

st.set_page_config(
    layout="wide",
    page_title="Leituras do Sensor",
    page_icon="📊",
    initial_sidebar_state="collapsed",
    #menu_items={'Consultar Sensores': None}
)

# Obtém o parâmetro 'sensor_id' da URI

query_params = st.query_params
sensor_id = int(query_params.get("sensor_id", [0])[0])  # Pega o valor ou usa 0 como padrão
tag = str(query_params.get("tag"))  # Pega o valor ou usa 0 como padrão
leitura = get_leituras(sensor_id)
st.markdown('<a href="./Consultar_Sensores" target="_self" style="font-size:30px">Voltar para a página de Sensores</a>', unsafe_allow_html=True)

st.subheader(f"Leituras do Sensor: {tag} ", anchor=False)

st.markdown(f'<a href="./Leituras_Sensor?sensor_id={sensor_id}&tag={tag}" target="_self" style="font-size:25px">Navegar para o gráfico</a>', unsafe_allow_html=True)

st.json(leitura)


