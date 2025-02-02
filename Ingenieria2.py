import streamlit as st
from FuncionesSW2 import *


# Inicializa la lista para guardar registros si no existe
if 'user_data' not in st.session_state:
    st.session_state['user_data'] = []

#Pagina destinada a mostrar el inicio de la aplicacion
page = st.sidebar.radio("Opciones de Registro", ("Inicio", "Formulario de Registro ","Formulario Mecanico","Formulario Taller", "Usuarios Registrados", "Mapa de Manizales"))

# Ejecuta la función correspondiente según la opción seleccionada
if page == "Inicio":
    mostrar_inicio()
elif page == "Formulario de Registro ":
    formulario_registro()
elif page == "Formulario Mecanico":
    FormularioRegistroMecanico()
elif page=="Formulario Taller":
    FormularioTaller()
elif page == "Usuarios Registrados":
    mostrar_registros()
elif page == "Mapa de Manizales":
    mapa_manizales()