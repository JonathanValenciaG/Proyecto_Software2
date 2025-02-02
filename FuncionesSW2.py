import streamlit as st
import pandas as pd
import pydeck as pdk
from BasedeDatos1 import FirebaseDB
from firebase_admin import db
import os

# Proporciona la ruta completa al archivo BaseDatos.json
path = os.path.join(os.path.dirname(__file__), 'Clave2.json')
url = "https://proyectois2-cabb0-default-rtdb.firebaseio.com/"

# Verifica si el archivo existe
if not os.path.exists(path):
    st.error(f'El archivo {path} no existe. Por favor, verifica la ruta.')

# Inicializa la base de datos
firebase_db = FirebaseDB(path, url)

def mostrar_inicio():
    st.title("Bienvenido al Taller Mecánico")
    st.write("Aquí puedes gestionar tus citas y tus registros para tu servico de Mecanica.")

# Función para mostrar el formulario de registro de usuarios
def formulario_registro():
    st.title("Formulario de Registro ")
    with st.form("registro_usuario"):
        nombre = st.text_input('Nombre Completo')
        telefono = st.text_input('Teléfono')
        email = st.text_input('Correo Electrónico')
        
        # Selectbox para elegir el tipo de vehículo
        Vehiculo = st.selectbox('Tipo de Vehículo', ['Carro', 'Moto', "Motocarro", "Buseta", "Tractomula", "Cuatrimoto"])
        
        DetallesVehiculo = st.text_input('Marca y Modelo del Vehículo')
        placa = st.text_input('Número de Placa')
        
        # Botón para registrar
        submit = st.form_submit_button('Registrar')
        if submit:
            if nombre and telefono and email and Vehiculo and DetallesVehiculo and placa:
                # Guardar los datos en Firebase Realtime Database
                data = {
                    "nombre": nombre,
                    "telefono": telefono,
                    "email": email,
                    "Vehiculo": Vehiculo,
                    "DetallesVehiculo": DetallesVehiculo,
                    "placa": placa,
                }
                try:
                    firebase_db.write_record(f'registros/{nombre}', data)
                    st.success('Registro exitoso')
                except Exception as e:
                    st.error(f'Error en el registro: {e}')

# Función para mostrar el formulario de registro de mecánicos
def FormularioRegistroMecanico():
    st.title("Formulario Mecánico")
    with st.form("registro_mecanico"):
        nombre = st.text_input('Nombre Completo')
        telefono = st.text_input('Teléfono')
        email = st.text_input('Correo Electrónico')
        experiencia = st.text_area('Experiencia y Especialización')
        # Botón para registrar
        submit = st.form_submit_button('Registrar')
        if submit:
            if nombre and telefono and email and experiencia:
                # Guardar los datos en Firebase Realtime Database
                data = {
                    "nombre": nombre,
                    "telefono": telefono,
                    "email": email,
                    "experiencia": experiencia,
                }
                try:
                    firebase_db.write_record(f'mecanicos/{nombre}', data)
                    st.success('Registro exitoso')
                except Exception as e:
                    st.error(f'Error en el registro: {e}')

# Función para mostrar el formulario de registro de talleres
def FormularioTaller():
    st.title("Formulario Taller")
    with st.form("registro_taller"):
        nombre_taller = st.text_input('Nombre del Taller')
        telefono = st.text_input('Teléfono')
        email = st.text_input('Correo Electrónico')
        direccion = st.text_input('Dirección')
        horario = st.text_input('Horario de Atención')
        servicios = st.text_area('Servicios que Ofrece')
        
        # Botón para registrar
        submit = st.form_submit_button('Registrar')
        if submit:
            if nombre_taller and telefono and email and direccion and horario and servicios:
                # Guardar los datos en Firebase Realtime Database
                data = {
                    "nombre_taller": nombre_taller,
                    "telefono": telefono,
                    "email": email,
                    "direccion": direccion,
                    "horario": horario,
                    "servicios": servicios
                }
                try:
                    firebase_db.write_record(f'talleres/{nombre_taller}', data)
                    st.success('Registro exitoso')
                except Exception as e:
                    st.error(f'Error en el registro: {e}')

# Función para mostrar los registros de todos los usuarios
def mostrar_registros():
    st.title("Registros de Clientes")
    try:
        registros = firebase_db.read_record('registros')
        if registros:
            # Convertir los registros en un DataFrame de Pandas para mostrarlos en Streamlit
            registros_df = pd.DataFrame.from_dict(registros, orient='index')
            st.dataframe(registros_df)
        else:
            st.write('No hay registros disponibles aún.')
    except Exception as e:
        st.error(f'Error al obtener los registros: {e}')
        
    st.title("Registros de Mecanicos")
    try:
        registros = firebase_db.read_record('mecanicos')
        if registros:
            # Convertir los registros en un DataFrame de Pandas para mostrarlos en Streamlit
            registros_df = pd.DataFrame.from_dict(registros, orient='index')
            st.dataframe(registros_df)
        else:
            st.write('No hay registros disponibles aún.')

    except Exception as e:
        st.error(f'Error al obtener los registros: {e}')

    st.title("Registros de Talleres")
    try:
        registros = firebase_db.read_record('talleres')
        if registros:
            # Convertir los registros en un DataFrame de Pandas para mostrarlos en Streamlit
            registros_df = pd.DataFrame.from_dict(registros, orient='index')
            st.dataframe(registros_df)
        else:
            st.write('No hay registros disponibles aún.')
    except Exception as e:
        st.error(f'Error al obtener los registros: {e}')

# Función para mostrar el mapa de Manizales
def mapa_manizales():
    manizales_center = {
        'latitude': 5.0689,
        'longitude': -75.5174
    }

    # Configuración del mapa
    view_state = pdk.ViewState(
        latitude=manizales_center['latitude'],
        longitude=manizales_center['longitude'],
        zoom=12  # Ajusta el nivel de zoom para mostrar la ciudad
    )

    # Crear el mapa sin puntos
    mapa = pdk.Deck(map_style='mapbox://styles/mapbox/streets-v11', initial_view_state=view_state)

    # Mostrar el mapa
    st.title("Mapa de Manizales, Colombia")
    st.pydeck_chart(mapa)