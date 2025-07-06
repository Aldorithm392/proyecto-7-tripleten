import streamlit as st
import pandas as pd
import plotly.express as px

# Configurar la página
st.set_page_config(page_title="Análisis de Vehículos", layout="wide")

# Título principal
st.header("🚗 Análisis de Datos de Vehículos en Venta")

# Cargar los datos
@st.cache_data  # Esto mejora el rendimiento
def load_data():
    data = pd.read_csv('vehicles_us.csv')
    return data

car_data = load_data()

# Mostrar información básica
st.subheader("Vista previa de los datos")
st.write(f"El dataset contiene {car_data.shape[0]} vehículos y {car_data.shape[1]} características")

# Crear dos columnas para los controles
col1, col2 = st.columns(2)

# Botón para el histograma
with col1:
    hist_button = st.button('Construir histograma')

# Botón para el gráfico de dispersión
with col2:
    scatter_button = st.button('Construir gráfico de dispersión')

# Mostrar histograma si se presiona el botón
if hist_button:
    st.write('### Histograma del Kilometraje de los Vehículos')
    
    # Crear histograma
    fig = px.histogram(car_data, 
                       x="odometer",
                       title="Distribución del Kilometraje",
                       labels={"odometer": "Kilometraje", "count": "Cantidad"})
    
    # Mostrar el gráfico
    st.plotly_chart(fig, use_container_width=True)

# Mostrar gráfico de dispersión si se presiona el botón
if scatter_button:
    st.write('### Relación entre Precio y Kilometraje')
    
    # Crear gráfico de dispersión
    fig = px.scatter(car_data, 
                     x="odometer", 
                     y="price",
                     title="Precio vs Kilometraje",
                     labels={"odometer": "Kilometraje", "price": "Precio ($)"})
    
    # Mostrar el gráfico
    st.plotly_chart(fig, use_container_width=True)

# Sección adicional con casillas de verificación (opcional pero recomendado)
st.subheader("Visualizaciones con casillas de verificación")

# Crear casillas de verificación
build_histogram = st.checkbox('Mostrar histograma de años')
build_scatter = st.checkbox('Mostrar dispersión precio vs año')

if build_histogram:
    fig = px.histogram(car_data, 
                       x="model_year",
                       title="Distribución de Años de los Modelos",
                       labels={"model_year": "Año del Modelo", "count": "Cantidad"})
    st.plotly_chart(fig, use_container_width=True)

if build_scatter:
    fig = px.scatter(car_data, 
                     x="model_year", 
                     y="price",
                     title="Precio por Año del Modelo",
                     labels={"model_year": "Año del Modelo", "price": "Precio ($)"})
    st.plotly_chart(fig, use_container_width=True)