import streamlit as st

st.title("Sobre o Fluxo de Funcionamento")

st.markdown("""
Este dashboard interage com uma API FastAPI de sensores IIoT. O fluxo é:

1. **Consulta de Sensores**: lista todos os sensores registrados.
2. **Cadastro de Sensor**: envia dados de um novo sensor via POST.
3. **Leitura de Sensor**: consulta os dados de leitura de um sensor específico.

A API usada está disponível em:  
[https://iiot-sensors-api-fastapi.onrender.com](https://iiot-sensors-api-fastapi.onrender.com)
""")
