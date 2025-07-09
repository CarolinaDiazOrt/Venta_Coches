import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

fig2 = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
fig2.show() # crear gráfico de dispersión

st.header('Análisis de precios de vehículos')

hist_button = st.button('Construir histograma') # crear un botón

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer") # crear histograma

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir gráfico de dispersión') # crear un botón

if scatter_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.scatter(car_data, x="odometer") # crear gráfico de dispersión

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# crear una casilla de verificación
build_boxplot = st.checkbox('Construir un boxplot')

if build_boxplot: # si la casilla de verificación está seleccionada
    st.write('Construir un box plot para el precio por año del modelo')
    # Boxplot por años
    fig = px.box(car_data, x="model_year", y="price")
    st.plotly_chart(fig, use_container_width=True)
