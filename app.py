import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

fig2 = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
fig2.show() # crear gráfico de dispersión

st.header('Análisis de precios de vehículos')

st.markdown("""
Este proyecto realiza un análisis exploratorio de una base de datos con información sobre vehículos listados para la venta.

El objetivo principal es comprender el comportamiento del mercado de carros y analizar los factores que pueden influir en el precio final de un vehículo. Entre las variables consideradas se incluyen el año del modelo, la marca, el kilometraje, la condición del vehículo, el tipo de transmisión, entre otros.

A continuación, elija la gráfica que desea visualizar.             
            """)

st.subheader('Distribuciones de variables')

hist_button_odom = st.button('Construir histograma odómetro') # crear un botón

if hist_button_odom: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el kilometraje de los coches en venta')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer") # crear histograma

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

hist_button_price = st.button('Construir histograma precio') # crear un botón

if hist_button_price: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="price") # crear histograma

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir gráfico de dispersión') # crear un botón

if scatter_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.scatter(car_data, x="odometer", y="price") # crear gráfico de dispersión

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# crear una casilla de verificación
build_boxplot = st.checkbox('Construir un boxplot')

if build_boxplot: # si la casilla de verificación está seleccionada
    st.write('Construir un box plot para el precio por año del modelo')
    # Boxplot por años
    fig = px.box(car_data, x="model_year", y="price")
    st.plotly_chart(fig, use_container_width=True)
