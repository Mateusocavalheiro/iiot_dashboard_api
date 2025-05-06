import streamlit as st
from utils.api_client import get_leituras

st.title("Leituras de um Sensor")

sensor_id = st.number_input("ID do Sensor", min_value=1, step=1)

if st.button("Consultar Leituras"):
    leitura = get_leituras(sensor_id)
    st.json(leitura)
