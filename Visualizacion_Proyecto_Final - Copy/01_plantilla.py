# -*- coding: utf-8 -*-
"""
Plantilla Básica de Streamlit
Autor: Iñigo Asensio
Fecha: 2025
Descripción: Plantilla base para crear aplicaciones Streamlit
"""

import streamlit as st
import pandas as pd
import numpy as np

#########################
## CONFIGURACIÓN DE PÁGINA
#########################
st.set_page_config(
    page_title="Mi App Streamlit",
    page_icon="🚀",
    layout="wide",  # "centered" o "wide"
    initial_sidebar_state="expanded"
)

#########################
## ESTILOS PERSONALIZADOS (OPCIONAL)
#########################
# st.markdown("""
#     <style>
#     .main {
#         background-color: #f5f5f5;
#     }
#     </style>
# """, unsafe_allow_html=True)

#########################
## SIDEBAR (MENÚ LATERAL)
#########################
with st.sidebar:
    st.title("⚙️ Configuración")
    st.divider()

    # Selector de página/sección
    pagina = st.selectbox(
        "Selecciona una sección",
        ["🏠 Inicio", "📊 Datos", "📈 Visualizaciones", "ℹ️ Acerca de"]
    )

    st.divider()

    # Filtros o controles adicionales
    st.subheader("Filtros")
    filtro_1 = st.checkbox("Activar filtro 1", value=True)
    filtro_2 = st.slider("Ajuste", 0, 100, 50)

    st.divider()
    st.caption("© 2025 - Mi Aplicación")

#########################
## CONTENIDO PRINCIPAL
#########################

# Título principal
st.title("🚀 Plantilla Básica Streamlit")
st.markdown("**Bienvenido** a tu aplicación Streamlit")
st.divider()

#########################
## PÁGINA: INICIO
#########################
if pagina == "🏠 Inicio":
    st.header("Página de Inicio")

    # Métricas
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Métrica 1", "100", "+10%")
    with col2:
        st.metric("Métrica 2", "250", "-5%")
    with col3:
        st.metric("Métrica 3", "75", "+2%")

    st.divider()
    "#1CB960"

    # Contenido principal
    st.subheader("Bienvenido")
    st.write("""
    Esta es una plantilla básica de Streamlit que incluye:
    - ✅ Configuración de página
    - ✅ Sidebar con navegación
    - ✅ Múltiples secciones
    - ✅ Layouts organizados
    - ✅ Ejemplos de visualizaciones
    """)

    # Botones de acción
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🎯 Acción 1", use_container_width=True):
            st.success("¡Acción 1 ejecutada!")
    with col2:
        if st.button("🔧 Acción 2", use_container_width=True):
            st.info("¡Acción 2 ejecutada!")

#########################
## PÁGINA: DATOS
#########################
elif pagina == "📊 Datos":
    st.header("Gestión de Datos")

    # Subir archivo
    st.subheader("Cargar datos")
    archivo = st.file_uploader(
        "Sube tu archivo CSV o Excel",
        type=['csv', 'xlsx']
    )

    if archivo is not None:
        # Leer archivo
        if archivo.name.endswith('.csv'):
            df = pd.read_csv(archivo)
        else:
            df = pd.read_excel(archivo)

        st.success(f"✅ Archivo cargado: {archivo.name}")

        # Mostrar datos
        st.subheader("Vista previa de datos")
        st.dataframe(df, use_container_width=True)

        # Estadísticas
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Filas", df.shape[0])
            st.metric("Columnas", df.shape[1])
        with col2:
            if st.button("📊 Ver estadísticas"):
                st.write(df.describe())

    else:
        # Datos de ejemplo
        st.info("No hay archivo cargado. Mostrando datos de ejemplo:")

        df_ejemplo = pd.DataFrame({
            'Fecha': pd.date_range('2025-01-01', periods=10),
            'Ventas': np.random.randint(100, 1000, 10),
            'Categoría': np.random.choice(['A', 'B', 'C'], 10)
        })

        st.dataframe(df_ejemplo, use_container_width=True)

#########################
## PÁGINA: VISUALIZACIONES
#########################
elif pagina == "📈 Visualizaciones":
    st.header("Visualizaciones")

    # Generar datos de ejemplo
    datos = pd.DataFrame({
        'x': range(1, 11),
        'y': np.random.randn(10).cumsum(),
        'z': np.random.randn(10).cumsum()
    })

    # Gráficos en columnas
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Gráfico de líneas")
        st.line_chart(datos[['x', 'y']].set_index('x'))

    with col2:
        st.subheader("Gráfico de área")
        st.area_chart(datos[['x', 'z']].set_index('x'))

    st.divider()

    # Gráfico de barras
    st.subheader("Gráfico de barras")
    categorias = pd.DataFrame({
        'Categoría': ['A', 'B', 'C', 'D'],
        'Valor': [23, 45, 12, 67]
    })
    st.bar_chart(categorias.set_index('Categoría'))

    st.divider()

    # Mapa (si tienes coordenadas)
    st.subheader("Mapa de ejemplo")
    map_data = pd.DataFrame({
        'lat': [40.4168, 41.3851, 39.4699],
        'lon': [-3.7038, 2.1734, -0.3763]
    })
    st.map(map_data)

#########################
## PÁGINA: ACERCA DE
#########################
elif pagina == "ℹ️ Acerca de":
    st.header("Acerca de esta aplicación")

    st.write("""
    ### 📋 Información del proyecto

    **Nombre:** Mi Aplicación Streamlit  
    **Versión:** 1.0.0  
    **Autor:** Tu nombre  
    **Fecha:** 2025

    ### 📚 Descripción

    Esta es una plantilla básica para crear aplicaciones web con Streamlit.
    Incluye las secciones más comunes y ejemplos de uso.

    ### 🛠️ Tecnologías utilizadas

    - Python 3.x
    - Streamlit
    - Pandas
    - NumPy

    ### 📞 Contacto

    Para más información, visita [streamlit.io](https://streamlit.io)
    """)

    st.divider()

    # Información adicional en expander
    with st.expander("🔧 Configuración técnica"):
        st.write("""
        - **Layout:** Wide
        - **Tema:** Light/Dark (automático)
        - **Cache:** Habilitado
        """)

    with st.expander("📖 Instrucciones de uso"):
        st.write("""
        1. Selecciona una sección en el menú lateral
        2. Carga tus datos o usa los datos de ejemplo
        3. Explora las visualizaciones
        4. Ajusta los filtros según necesites
        """)

#########################
## PIE DE PÁGINA
#########################
st.divider()
st.caption("Desarrollado con ❤️ usando Streamlit | © 2025")













