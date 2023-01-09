
import streamlit as st
from multiapp import MultiApp
from apps import home, Datos, Modelos, Ejemplo_videos

app = MultiApp()


# Add all your application here
app.add_app("Home", home.app)
app.add_app("Datos", Datos.app)
app.add_app("Modelos", Modelos.app)
app.add_app("Ejemplo videos", Ejemplo_videos.app)
# The main app
app.run()