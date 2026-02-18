import streamlit as st
import pandas as pd
import random
import time

st.title("🌡 Temperature Monitoring Dashboard")

threshold = st.slider("Set High Temperature Alert (°C)", 30, 50, 35)

start = st.button("Start Monitoring")

if start:
    data = []
    
    temp_display = st.empty()
    alert_display = st.empty()
    chart_display = st.empty()

    for i in range(30):
        temp = random.uniform(25, 45)
        data.append(temp)

        df = pd.DataFrame(data, columns=["Temperature"])

        # Update temperature
        temp_display.metric("Current Temperature", f"{temp:.2f} °C")

        # Update alert
        if temp > threshold:
            alert_display.error("⚠ High Temperature Alert!")
        else:
            alert_display.success("Temperature Normal")

        # Update graph (this replaces old one)
        chart_display.line_chart(df)

        time.sleep(1)
