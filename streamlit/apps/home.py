import streamlit as st
from PIL import Image

def app():
        st.title('Clasificación de señales')

        st.markdown("""
        El objetivo de este trabajo será la clasificación de 43 señales disintas de tráfico mediante  el 
        empleo de redes neuronales. 
        """)

        background = Image.open("./imagenes/fondo_inicio.jpg")
        col1, col2, col3 = st.columns([2, 5, 2])
        col2.image(background, width=500)


        click = st.button('Click me')
        print(click)
