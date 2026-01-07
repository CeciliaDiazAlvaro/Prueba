# -*- coding: utf-8 -*-
"""
Guía Completa de Inputs/Widgets en Streamlit
Fecha: 2025
"""

import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime, date, time

# Configuración de página
st.set_page_config(
    page_title="Inputs de Streamlit",
    page_icon="🎮",
    layout="wide"
)

st.title("🎮 Guía Completa de Inputs en Streamlit")
st.write("Todos los widgets disponibles para interactuar con el usuario")
st.divider()

# Datos de ejemplo
df = pd.DataFrame({
    'animal': ['gato', 'perro', 'caracol', 'serpiente'],
    'edad': ['3 años', '5 meses', '5 días', '1 año'],
    'característica': ['mamífero', 'mamífero', 'molusco', 'reptil']
})

#########################
## 1. BUTTON (Botón)
#########################
st.header("1. Button (Botón)")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Botón simple")
    if st.button('Pulse para continuar'):
        st.success('¡Bienvenido al siguiente paso!')

    st.subheader("Botón con ícono y tipo")
    if st.button('🚀 Botón primario', type="primary"):
        st.info("Botón primario presionado")

    if st.button('Botón secundario', type="secondary"):
        st.info("Botón secundario presionado")

with col2:
    st.subheader("Botón con key personalizada")
    if st.button('Click aquí', key='boton_1'):
        st.write('Has presionado el botón 1')

    st.subheader("Botón deshabilitado")
    st.button('No puedes presionarme', disabled=True)

    st.subheader("Botón con ayuda")
    if st.button('Botón con tooltip', help="Este es un mensaje de ayuda"):
        st.write("¡Funciona!")

st.divider()

#########################
## 2. DOWNLOAD_BUTTON (Botón de descarga)
#########################
st.header("2. Download Button (Botón de descarga)")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Descargar texto")
    texto = "Este es un archivo de texto de ejemplo"
    st.download_button(
        label="📥 Descargar TXT",
        data=texto,
        file_name="archivo.txt",
        mime="text/plain"
    )

with col2:
    st.subheader("Descargar CSV")
    csv = df.to_csv(index=False)
    st.download_button(
        label="📊 Descargar CSV",
        data=csv,
        file_name="datos.csv",
        mime="text/csv"
    )

st.divider()

#########################
## 3. LINK_BUTTON (Botón con enlace)
#########################
st.header("3. Link Button (Botón con enlace)")

col1, col2 = st.columns(2)
with col1:
    st.link_button("🔗 Ir a Google", "https://google.com")
with col2:
    st.link_button("📚 Documentación Streamlit", "https://docs.streamlit.io")

st.divider()

#########################
## 4. CHECKBOX (Casilla de verificación)
#########################
st.header("4. Checkbox (Casilla de verificación)")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Checkbox simple")
    if st.checkbox('Mostrar datos'):
        st.dataframe(df)

    st.subheader("Checkbox con valor por defecto")
    acepta = st.checkbox('Acepto términos y condiciones', value=True)
    if acepta:
        st.success("✅ Términos aceptados")

with col2:
    st.subheader("Checkbox deshabilitado")
    st.checkbox('No puedes cambiarme', value=True, disabled=True)

    st.subheader("Múltiples checkboxes")
    opcion1 = st.checkbox('Opción 1')
    opcion2 = st.checkbox('Opción 2')
    opcion3 = st.checkbox('Opción 3')

    seleccionadas = sum([opcion1, opcion2, opcion3])
    st.write(f"Has seleccionado {seleccionadas} opciones")

st.divider()

#########################
## 5. TOGGLE (Interruptor)
#########################
st.header("5. Toggle (Interruptor)")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Toggle simple")
    activado = st.toggle('Activar modo oscuro')
    if activado:
        st.write("🌙 Modo oscuro activado")
    else:
        st.write("☀️ Modo claro activado")

with col2:
    st.subheader("Toggle con valor por defecto")
    notificaciones = st.toggle('Notificaciones', value=True)
    st.write(f"Notificaciones: {'ON' if notificaciones else 'OFF'}")

st.divider()

#########################
## 6. RADIO (Botones de radio)
#########################
st.header("6. Radio (Botones de radio)")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Radio vertical")
    pais = st.radio(
        "Elige qué país prefieres",
        ('España', 'Italia', 'Alemania')
    )
    if pais == 'España':
        st.write('¡Te gusta España! 🇪🇸')
    else:
        st.write(f"Te gusta más {pais} que España")

with col2:
    st.subheader("Radio horizontal")
    color = st.radio(
        "Elige un color",
        ["🔴 Rojo", "🟢 Verde", "🔵 Azul"],
        horizontal=True
    )
    st.write(f"Has elegido: {color}")

    st.subheader("Radio con índice por defecto")
    fruta = st.radio(
        "Fruta favorita",
        ["Manzana", "Plátano", "Naranja"],
        index=1  # Plátano seleccionado por defecto
    )

st.divider()

#########################
## 7. SELECTBOX (Lista desplegable)
#########################
st.header("7. Selectbox (Lista desplegable)")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Selectbox simple")
    seleccion = st.selectbox(
        'Elige el animal que quieres conocer',
        df['animal']
    )
    st.write('Has elegido:', df[df['animal'] == seleccion])

with col2:
    st.subheader("Selectbox con placeholder")
    opcion = st.selectbox(
        'Elige una opción',
        ['Opción 1', 'Opción 2', 'Opción 3'],
        index=None,
        placeholder="Selecciona una opción..."
    )
    if opcion:
        st.write(f"Seleccionaste: {opcion}")

st.divider()

#########################
## 8. MULTISELECT (Selección múltiple)
#########################
st.header("8. Multiselect (Selección múltiple)")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Multiselect simple")
    animales_seleccionados = st.multiselect(
        'Elige uno o más animales',
        df['animal'].tolist()
    )
    if animales_seleccionados:
        st.write("Has seleccionado:", animales_seleccionados)

with col2:
    st.subheader("Multiselect con valores por defecto")
    colores = st.multiselect(
        'Selecciona colores',
        ['Rojo', 'Verde', 'Azul', 'Amarillo', 'Negro'],
        default=['Rojo', 'Verde']
    )
    st.write(f"Colores seleccionados: {len(colores)}")

st.divider()

#########################
## 9. SLIDER (Deslizador)
#########################
st.header("9. Slider (Deslizador)")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Slider simple")
    x = st.slider('Elige un número', 0, 100)
    st.write(f'Has elegido el {x}')

    st.subheader("Slider con valor por defecto")
    edad = st.slider('Tu edad', 0, 100, 25)
    st.write(f'Tienes {edad} años')

    st.subheader("Slider con paso personalizado")
    precio = st.slider('Precio', 0.0, 100.0, 50.0, 0.5)
    st.write(f'Precio: ${precio}')

with col2:
    st.subheader("Slider de rango")
    rango = st.slider(
        'Selecciona un rango de edad',
        0, 100, (25, 75)
    )
    st.write(f'Rango seleccionado: {rango[0]} - {rango[1]} años')

    st.subheader("Slider con formato")
    temperatura = st.slider(
        'Temperatura',
        -10, 50, 20,
        format="%d°C"
    )

st.divider()

#########################
## 10. SELECT_SLIDER (Slider de selección)
#########################
st.header("10. Select Slider (Slider de selección)")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Select slider con texto")
    nivel = st.select_slider(
        'Selecciona tu nivel',
        options=['Principiante', 'Intermedio', 'Avanzado', 'Experto']
    )
    st.write(f'Tu nivel: {nivel}')

with col2:
    st.subheader("Select slider con rango")
    rango_tiempo = st.select_slider(
        'Horario de trabajo',
        options=['6:00', '9:00', '12:00', '15:00', '18:00', '21:00'],
        value=('9:00', '18:00')
    )
    st.write(f'Horario: {rango_tiempo[0]} - {rango_tiempo[1]}')

st.divider()

#########################
## 11. TEXT_INPUT (Entrada de texto)
#########################
st.header("11. Text Input (Entrada de texto)")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Text input simple")
    nombre = st.text_input("Escribe tu nombre", key="nombre")
    if nombre:
        st.write(f'Hola {nombre}, ¿Cómo estás?')

    st.subheader("Text input con placeholder")
    email = st.text_input(
        "Email",
        placeholder="usuario@ejemplo.com"
    )

with col2:
    st.subheader("Text input con valor por defecto")
    ciudad = st.text_input("Ciudad", value="Madrid")

    st.subheader("Text input con máximo de caracteres")
    codigo = st.text_input(
        "Código (máx 6 caracteres)",
        max_chars=6
    )

st.divider()

#########################
## 12. TEXT_AREA (Área de texto)
#########################
st.header("12. Text Area (Área de texto)")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Text area simple")
    comentario = st.text_area(
        "Escribe tu comentario",
        height=150
    )

with col2:
    st.subheader("Text area con valor por defecto")
    descripcion = st.text_area(
        "Descripción",
        value="Texto de ejemplo...",
        height=150,
        max_chars=200
    )
    if descripcion:
        st.write(f"Caracteres: {len(descripcion)}/200")

st.divider()

#########################
## 13. NUMBER_INPUT (Entrada numérica)
#########################
st.header("13. Number Input (Entrada numérica)")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Number input entero")
    numero = st.number_input(
        "Ingresa un número",
        min_value=0,
        max_value=100,
        value=10,
        step=1
    )
    st.write(f"Número: {numero}")

with col2:
    st.subheader("Number input decimal")
    decimal = st.number_input(
        "Ingresa un decimal",
        min_value=0.0,
        max_value=10.0,
        value=5.5,
        step=0.1,
        format="%.2f"
    )
    st.write(f"Decimal: {decimal}")

st.divider()

#########################
## 14. DATE_INPUT (Entrada de fecha)
#########################
st.header("14. Date Input (Entrada de fecha)")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Date input simple")
    fecha = st.date_input("Selecciona una fecha")
    st.write(f"Fecha seleccionada: {fecha}")

    st.subheader("Date input con valor por defecto")
    fecha_nacimiento = st.date_input(
        "Fecha de nacimiento",
        value=date(1990, 1, 1)
    )

with col2:
    st.subheader("Date input con rango")
    rango_fechas = st.date_input(
        "Selecciona rango de fechas",
        value=(date(2025, 1, 1), date(2025, 12, 31))
    )
    if len(rango_fechas) == 2:
        st.write(f"Del {rango_fechas[0]} al {rango_fechas[1]}")

st.divider()

#########################
## 15. TIME_INPUT (Entrada de hora)
#########################
st.header("15. Time Input (Entrada de hora)")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Time input simple")
    hora = st.time_input("Selecciona una hora")
    st.write(f"Hora seleccionada: {hora}")

with col2:
    st.subheader("Time input con valor por defecto")
    hora_alarma = st.time_input(
        "Hora de alarma",
        value=time(7, 30)
    )
    st.write(f"Alarma configurada a las {hora_alarma}")

st.divider()

#########################
## 16. FILE_UPLOADER (Cargador de archivos)
#########################
st.header("16. File Uploader (Cargador de archivos)")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Subir un archivo")
    archivo = st.file_uploader("Elige un archivo")
    if archivo is not None:
        st.success(f"Archivo cargado: {archivo.name}")
        st.write(f"Tamaño: {archivo.size} bytes")

with col2:
    st.subheader("Subir múltiples archivos")
    archivos = st.file_uploader(
        "Elige archivos",
        accept_multiple_files=True,
        type=['csv', 'txt', 'xlsx']
    )
    if archivos:
        st.write(f"Archivos cargados: {len(archivos)}")
        for archivo in archivos:
            st.write(f"- {archivo.name}")

st.divider()

#########################
## 17. CAMERA_INPUT (Entrada de cámara)
#########################
st.header("17. Camera Input (Entrada de cámara)")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Tomar foto")
    foto = st.camera_input("Toma una foto")
    if foto is not None:
        st.image(foto, caption="Foto capturada")

with col2:
    st.subheader("Info")
    st.info("📷 Este widget permite capturar fotos directamente desde la cámara del dispositivo")

st.divider()

#########################
## 18. COLOR_PICKER (Selector de color)
#########################
st.header("18. Color Picker (Selector de color)")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Color picker simple")
    color = st.color_picker('Elige un color', '#00f900')
    st.write(f"Color seleccionado: {color}")

with col2:
    st.subheader("Demostración")
    st.markdown(
        f'<div style="background-color: {color}; padding: 50px; '
        f'border-radius: 10px; text-align: center; color: white;">'
        f'<h3>Este es tu color</h3></div>',
        unsafe_allow_html=True
    )

st.divider()

#########################
## 19. DATA_EDITOR (Editor de datos)
#########################
st.header("19. Data Editor (Editor de datos)")

st.subheader("Tabla editable")
df_editable = pd.DataFrame({
    'Producto': ['Laptop', 'Mouse', 'Teclado'],
    'Precio': [800, 25, 60],
    'Stock': [10, 50, 30],
    'Disponible': [True, True, False]
})

editado = st.data_editor(
    df_editable,
    num_rows="dynamic",  # Permite añadir/eliminar filas
    use_container_width=True
)

if st.button("Mostrar datos editados"):
    st.write("Datos actualizados:")
    st.dataframe(editado)

st.divider()

#########################
## 20. CHAT_INPUT (Entrada de chat)
#########################
st.header("20. Chat Input (Entrada de chat)")

st.subheader("Simulación de chat")
prompt = st.chat_input("Escribe un mensaje...")

if prompt:
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        st.write(f"Has dicho: '{prompt}'")

st.divider()

#########################
## TIPS Y MEJORES PRÁCTICAS
#########################
st.header("📚 Tips y Mejores Prácticas")

with st.expander("Ver consejos sobre inputs"):
    st.markdown("""
    ### Cuándo usar cada input:

    **Selección:**
    - **Button**: Acciones únicas (enviar, guardar, procesar)
    - **Checkbox**: Opciones on/off, múltiples selecciones independientes
    - **Toggle**: Estados binarios (activar/desactivar)
    - **Radio**: Selección única entre pocas opciones (2-5)
    - **Selectbox**: Selección única entre muchas opciones
    - **Multiselect**: Selección múltiple entre muchas opciones

    **Valores numéricos:**
    - **Slider**: Rango visual, valores aproximados
    - **Number input**: Valores numéricos precisos

    **Texto:**
    - **Text input**: Textos cortos (nombre, email, búsqueda)
    - **Text area**: Textos largos (comentarios, descripciones)

    **Fechas y hora:**
    - **Date input**: Selección de fechas
    - **Time input**: Selección de horas

    **Archivos y media:**
    - **File uploader**: Subir archivos
    - **Camera input**: Capturar fotos
    - **Color picker**: Seleccionar colores

    ### Consejos generales:
    1. Usa `key` únicos para inputs relacionados
    2. Añade `help` para proporcionar contexto
    3. Valida inputs antes de procesarlos
    4. Usa `disabled` para mostrar valores no editables
    5. Combina con `st.form()` para agrupar inputs relacionados
    """)


#########################
## run
#########################
# streamlit run 03_inputs.py