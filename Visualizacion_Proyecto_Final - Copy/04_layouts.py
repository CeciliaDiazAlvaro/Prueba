# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import time

# Configuración de la página (debe ser lo primero)
st.set_page_config(
    page_title="Layouts de Streamlit",
    page_icon="🎨",
    layout="wide",  # "centered" o "wide"
    initial_sidebar_state="expanded"  # "auto", "expanded", "collapsed"
)

# Datos de ejemplo
df = pd.DataFrame({
    'animal': ['gato', 'perro', 'caracol', 'serpiente'],
    'edad': ['3 años', '5 meses', '5 días', '1 año'],
    'característica': ['mamífero', 'mamífero', 'molusco', 'reptil']
})

#########################
## 1. SIDEBAR (Barra lateral)
#########################
st.sidebar.title("🎯 Sidebar")
st.sidebar.header("Bienvenido a nuestra web")
genero = st.sidebar.selectbox(
    "Elige tu género",
    ("Hombre", "Mujer", "Prefiero no decirlo")
)
st.sidebar.write(f"Has seleccionado: {genero}")
st.sidebar.divider()
st.sidebar.info("Los sidebars son perfectos para controles y navegación")

#########################
## 2. COLUMNS (Columnas)
#########################
st.title("📊 Guía Completa de Layouts en Streamlit")
st.divider()

st.header("1. Columnas (Columns)")

# Columnas de igual ancho
st.subheader("a) Columnas de igual ancho")
col1, col2, col3 = st.columns(3)
with col1:
    st.write("**Columna 1**")
    st.write(df)
with col2:
    st.write("**Columna 2**")
    st.metric("Temperatura", "25°C", "+2°C")
with col3:
    st.write("**Columna 3**")
    st.button("Click aquí")

# Columnas con ancho proporcional
st.subheader("b) Columnas con ancho proporcional")
col1, col2, col3 = st.columns([3, 1, 2])
col1.info("Esta columna tiene proporción 3")
col2.success("Proporción 1")
col3.warning("Proporción 2")

# Columnas con gap personalizado
st.subheader("c) Columnas con espaciado (gap)")
col1, col2 = st.columns(2, gap="large")  # "small", "medium", "large"
col1.write("Columna con gap grande")
col2.write("Entre estas columnas")

st.divider()

#########################
## 3. TABS (Pestañas)
#########################
st.header("2. Tabs (Pestañas)")
tab1, tab2, tab3, tab4 = st.tabs(["📈 Gráficos", "🗃 Datos", "📝 Información", "⚙️ Config"])

with tab1:
    st.subheader("Gráficos")
    st.line_chart({"Ventas": [10, 20, 15, 25, 30]})

with tab2:
    st.subheader("Tabla de Datos")
    st.dataframe(df)

with tab3:
    st.subheader("Información")
    st.write("Las tabs son excelentes para organizar contenido relacionado")

with tab4:
    st.subheader("Configuración")
    st.checkbox("Activar modo oscuro")
    st.slider("Volumen", 0, 100, 50)

st.divider()

#########################
## 4. EXPANDER (Expandible)
#########################
st.header("3. Expander (Contenedor expandible)")

with st.expander("📖 Ver detalles sobre los datos"):
    st.write("""
    Los datos anteriores recogen la edad de distintos animales, 
    así como su clasificación según sus características animales.
    """)
    st.dataframe(df)

with st.expander("🔍 Más información", expanded=True):
    st.write("Este expander está expandido por defecto")
    st.code("st.expander('Título', expanded=True)")

st.divider()

#########################
## 5. CONTAINER (Contenedor múltiple)
#########################
st.header("4. Container (Contenedor múltiple)")
st.write("Permite añadir elementos fuera de orden:")

container = st.container(border=True)  # border=True añade borde
container.write("✅ Primer elemento del container")
st.write("⚠️ Esto está FUERA del container")
container.write("✅ Segundo elemento del container (añadido después)")
container.metric("Usuarios", "1,234", "+12%")

st.divider()

#########################
## 6. EMPTY (Contenedor único/placeholder)
#########################
st.header("5. Empty (Placeholder/Contenedor único)")
st.write("Útil para actualizar un único elemento:")

placeholder = st.empty()
placeholder.info("Contenido inicial")

if st.button("Cambiar contenido del placeholder"):
    placeholder.success("¡Contenido actualizado!")

# Ejemplo de contador
st.subheader("Ejemplo: Contador dinámico")
if st.button("Iniciar contador de 5 segundos"):
    countdown_placeholder = st.empty()
    for seconds in range(5, 0, -1):
        countdown_placeholder.write(f"⏳ Quedan {seconds} segundos")
        time.sleep(1)
    countdown_placeholder.success("✔️ ¡Completado!")

st.divider()

#########################
## 7. POPOVER (Menú emergente - Nuevo en Streamlit)
#########################
st.header("6. Popover (Menú emergente)")
st.write("Un menú que aparece al hacer click:")

with st.popover("🔧 Abrir opciones"):
    st.write("**Opciones avanzadas**")
    st.checkbox("Opción 1")
    st.checkbox("Opción 2")
    st.radio("Selecciona:", ["A", "B", "C"])

st.divider()

#########################
## 8. FORM (Formularios)
#########################
st.header("7. Form (Formularios)")
st.write("Agrupa inputs y se envían todos juntos:")

with st.form("mi_formulario"):
    st.write("**Completa el formulario**")
    nombre = st.text_input("Nombre")
    edad = st.number_input("Edad", 0, 120, 25)
    acepta = st.checkbox("Acepto términos y condiciones")

    submitted = st.form_submit_button("Enviar")
    if submitted:
        st.success(f"✅ Formulario enviado: {nombre}, {edad} años")

st.divider()

#########################
## 9. DIALOG (Diálogo modal - Nuevo en Streamlit)
#########################
st.header("8. Dialog (Ventana modal)")


@st.dialog("🎉 Ventana Modal")
def mostrar_dialogo():
    st.write("Esta es una ventana modal")
    st.write("Puedes poner cualquier contenido aquí")
    if st.button("Cerrar"):
        st.rerun()


if st.button("Abrir diálogo modal"):
    mostrar_dialogo()

st.divider()

#########################
## 10. STATUS (Contenedor de estado)
#########################
st.header("9. Status (Contenedor de estado)")

with st.status("Descargando datos...", expanded=True) as status:
    st.write("Buscando datos...")
    time.sleep(1)
    st.write("Encontrados datos!")
    time.sleep(1)
    st.write("Procesando...")
    time.sleep(1)
    status.update(label="✅ Descarga completa!", state="complete", expanded=False)

st.divider()

#########################
## 11. LAYOUTS AVANZADOS
#########################
st.header("10. Layouts Avanzados")

# Columnas anidadas
st.subheader("a) Columnas anidadas")
col1, col2 = st.columns(2)
with col1:
    st.write("**Columna principal 1**")
    subcol1, subcol2 = st.columns(2)
    subcol1.write("Sub 1.1")
    subcol2.write("Sub 1.2")

with col2:
    st.write("**Columna principal 2**")
    st.info("Sin subcolumnas")

# Containers con columnas
st.subheader("b) Container con columnas")
with st.container(border=True):
    st.write("**Container con columnas dentro**")
    c1, c2, c3 = st.columns(3)
    c1.metric("Métrica 1", "100")
    c2.metric("Métrica 2", "200")
    c3.metric("Métrica 3", "300")

st.divider()

#########################
## 12. ECHO (Mostrar código)
#########################
st.header("11. Echo (Mostrar código ejecutado)")

with st.echo():
    # Este código se mostrará Y ejecutará
    import numpy as np

    datos = np.random.randn(10)
    st.line_chart(datos)

st.divider()

#########################
## 13. SPINNER (Indicador de carga)
#########################
st.header("12. Spinner (Indicador de carga)")

if st.button("Iniciar proceso con spinner"):
    with st.spinner("Procesando..."):
        time.sleep(2)
    st.success("¡Proceso completado!")

st.divider()

#########################
## TIPS Y MEJORES PRÁCTICAS
#########################
st.header("📚 Tips y Mejores Prácticas")

with st.expander("Ver consejos"):
    st.markdown("""
    ### Cuándo usar cada layout:

    - **Sidebar**: Navegación, filtros globales, configuración
    - **Columns**: Comparaciones lado a lado, dashboards
    - **Tabs**: Diferentes vistas del mismo contenido
    - **Expander**: Información adicional/opcional
    - **Container**: Actualizar múltiples elementos
    - **Empty**: Actualizar UN solo elemento dinámicamente
    - **Popover**: Opciones adicionales sin ocupar espacio
    - **Form**: Agrupar inputs que se envían juntos
    - **Dialog**: Confirmaciones, alertas importantes
    - **Status**: Procesos con múltiples pasos

    ### Combinaciones potentes:
    - Sidebar + Tabs: App con navegación y contenido organizado
    - Container + Columns: Dashboards actualizables
    - Form + Expander: Formularios con ayuda contextual
    """)

st.divider()
st.caption("💡 Todos los layouts de Streamlit - Actualizado 2025")

#########################
## run
#########################
# streamlit run 04_layouts.py