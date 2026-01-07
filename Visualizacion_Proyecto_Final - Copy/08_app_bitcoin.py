import streamlit as st
import requests
import pandas as pd
import plotly.express as px


# Título de la app
st.title("Bitcoin Price Data")

# Explicación breve
st.write("Esta aplicación descarga y muestra los precios históricos de Bitcoin para un rango de fechas específico.")

# Selección de fechas
start_date = st.date_input("Fecha de inicio", value=pd.to_datetime("2023-01-01"))
end_date = st.date_input("Fecha de fin", value=pd.to_datetime("2023-12-31"))

# Convertir fechas al formato requerido por la API
start_date_str = start_date.strftime("%Y-%m-%d")
end_date_str = end_date.strftime("%Y-%m-%d")


# Función para descargar y mostrar datos
def load_and_display_data(start_date_str, end_date_str):
    # URL de la API para obtener los precios de Bitcoin
    url = "https://api.coindesk.com/v1/bpi/historical/close.json"
    params = {
        "start": start_date_str,
        "end": end_date_str
    }

    # Descargar datos usando requests
    response = requests.get(url, params=params)

    if response.ok:  # Verifica si la respuesta es exitosa
        # Mostrar mensaje de confirmación de descarga
        st.success(f"Request realizada correctamente")
        st.success(f"Datos descargados correctamente para el rango de fechas: {start_date_str} a {end_date_str}")

        # Parsear datos JSON
        data = response.json()
        prices = data["bpi"]

        # Crear DataFrame de Pandas
        df = pd.DataFrame(list(prices.items()), columns=["Date", "Price"])
        df["Date"] = pd.to_datetime(df["Date"])
        st.success(f"Comprobación del dataframe: {str(df["Date"].min())} a {str(df["Date"].max())}")

        # Mostrar tabla de precios
        st.subheader("Datos de precios de Bitcoin")
        st.write(df)

        # Crear gráfica usando Plotly
        fig = px.line(df, x="Date", y="Price", title="Precio histórico de Bitcoin")
        st.plotly_chart(fig)
    else:
        st.error(f"Error al descargar los datos. Código de estado: {response.status_code}")


# Verificar que la fecha de inicio sea menor o igual a la de fin
if start_date > end_date:
    st.error("La fecha de inicio debe ser anterior o igual a la fecha de fin.")
else:
    # Agregar botón para descargar datos
    if st.button("Descargar Datos"):
        load_and_display_data(start_date_str, end_date_str)



