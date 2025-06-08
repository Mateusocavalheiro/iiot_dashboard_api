import streamlit as st
import plotly.express as px
from utils.api_client import get_leituras_by_dates
import pandas as pd
from datetime import datetime, time as dt_time, timedelta, timezone

st.set_page_config(
    layout="wide",
    page_title="Leituras do Sensor",
    page_icon="📊",
    initial_sidebar_state="collapsed",
)

query_params = st.query_params
sensor_id = int(query_params.get("sensor_id", [0])[0])
tag = str(query_params.get("tag"))

st.title("Leituras de um Sensor")

# Seleção de data e hora
st.subheader("Selecione o intervalo de leitura:")

col1, col2 = st.columns(2)
with col1:
    data_inicio = st.date_input("Data inicial", value=datetime.now().date())
    hora_inicio = st.time_input("Hora inicial", value=dt_time(0, 0))
with col2:
    data_fim = st.date_input("Data final", value=datetime.now().date())
    hora_fim = st.time_input("Hora final", value=dt_time(23, 59))

# Fuso horário de Brasília (UTC-3)
br_tz = timezone(timedelta(hours=-3))

# Cria os datetimes no fuso de Brasília e converte para UTC
start_dt_br = datetime.combine(data_inicio, hora_inicio).replace(tzinfo=br_tz)
end_dt_br = datetime.combine(data_fim, hora_fim).replace(tzinfo=br_tz)

# Converte para UTC (que é o que o backend espera com "Z")
start_iso = start_dt_br.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
end_iso = end_dt_br.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")

# Botão para buscar as leituras
if st.button("Consultar Leituras"):
    leituras = get_leituras_by_dates(sensor_id, start=start_iso, end=end_iso)

    if leituras:
        # Converte os timestamps UTC para horário de Brasília
        br_tz = timezone(timedelta(hours=-3))
        timestamps = [
            datetime.fromisoformat(leitura['timestamp'].replace("Z", "+00:00"))
            .astimezone(br_tz)
            .strftime("%Y-%m-%d %H:%M:%S")
            for leitura in leituras
        ]
        valores = [leitura['valor'] for leitura in leituras]

        data = {
            'Timestamp (Brasília)': timestamps,
            'Valor': valores
        }

        fig = px.line(data_frame=data, x='Timestamp (Brasília)', y='Valor', title=f"Leituras do Sensor {tag}")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Nenhuma leitura encontrada no intervalo selecionado.")
