import streamlit as st
from utils.api_client import criar_sensor

st.title("Cadastrar Novo Sensor")

with st.form("form_sensor"):
    tag = st.text_input("Tag")
    tipo = st.selectbox("Tipo", ["Temperatura", "Pressão", "Vibração"])
    range_lrv = st.number_input("LRV")
    range_urv = st.number_input("URV")
    unidade = st.text_input("Unidade")
    valor = st.number_input("Valor Inicial")

    submitted = st.form_submit_button("Cadastrar")

    if submitted:
        data = {
            "tag": tag,
            "tipo": tipo,
            "range_lrv": range_lrv,
            "range_urv": range_urv,
            "unidade": unidade,
            "leituras": [{"valor": valor}]
        }
        resposta = criar_sensor(data)
        st.success("Sensor criado com sucesso!")
        st.json(resposta)
