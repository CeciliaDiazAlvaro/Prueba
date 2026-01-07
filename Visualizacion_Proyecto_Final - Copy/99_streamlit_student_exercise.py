# Usando la libreria request y la api WeatherApi genera una aplicacion de streamlit
# Esta aplication de streamlit tiene que tener un control en el que se pueda introducir el nombre de la ciudad
# y que saque en una tabla la información del tiempo en esa ciudad

# Para generar tu API_KEY tienes que seguir los siguientes pasos
# Ve https://www.weatherapi.com
# Create una cuenta con el plan free
# te generara una clave para que puedas ponerla en el codigo



import requests
import pandas as pd

# Tu clave de API
api_key = "TU_CLAVE"
# Ciudad para la que quieres obtener el clima
city = "Madrid"
# URL de la API de WeatherAPI
url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"

# Realizar la solicitud GET
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()
    # Extraer información del clima
    temperature = data['current']['temp_c']  # Temperatura en Celsius
    weather_description = data['current']['condition']['text']  # Descripción del clima
    humidity = data['current']['humidity']  # Humedad
    wind_speed = data['current']['wind_kph']  # Velocidad del viento en km/h

    # Mostrar la información
    print(f"Clima en {city}:")
    print(f"Temperatura: {temperature}°C")
    print(f"Descripción: {weather_description}")
    print(f"Humedad: {humidity}%")
    print(f"Velocidad del viento: {wind_speed} km/h")
    # Extraer datos relevantes
    weather_data = {
        "Ciudad": data['location']['name'],
        "Temperatura (°C)": data['current']['temp_c'],
        "Descripción": data['current']['condition']['text'],
        "Humedad (%)": data['current']['humidity'],
        "Velocidad del viento (km/h)": data['current']['wind_kph']
    }

    # Crear un DataFrame de pandas
    df = pd.DataFrame([weather_data])  # Usamos una lista para crear el DataFrame
else:
    print("Error al obtener los datos del clima:", response.status_code)