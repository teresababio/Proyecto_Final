import streamlit as st


st.title('Clasificación de señales')

st.markdown("""
        El objetivo de este trabajo será la clasificación de 5 señales disintas de tráfico mediante  el 
        empleo de redes neuronales.     
        * Límite de velocidad de 20  $$\frac{km}{h}$$

        * Límite de velocidad de 30  $$\frac{km}{h}$$

        * Stop

        * Seda al paso

        * Obligatorio girar a la derecha

        * Obligatorio girar a la izquierda
        """)

click = st.button('Click me')
print(click)
