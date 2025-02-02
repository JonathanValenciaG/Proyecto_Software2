import streamlit as st
import pandas as pd
import pydeck as pdk

def mostrar_inicio():
    st.title("Bienvenido al Taller Mecánico")
    st.write("Aquí puedes gestionar tus citas y tus registros para tu servico de Mecanica.")

# Función para mostrar el formulario de registro
def formulario_registro():
    st.title("Formulario de Registro")
    with st.form("registro_usuario"):

        nombre = st.text_input('Nombre Completo')
        telefono = st.text_input('Teléfono')
        email = st.text_input('Correo Electrónico')
        
        # Selectbox para elegir el tipo de vehículo
        Vehiculo = st.selectbox('Tipo de Vehículo', ['Carro', 'Moto', "Motocarro", "Buseta", "Tractomula", "Cuatrimoto"])
        
        DetallesVehiculo = st.text_input('Marca y Modelo del Vehículo')
        placa = st.text_input('Número de Placa')
        problema = st.text_area('Descripción del Problema')
        
        # Botón para registrar
        submit = st.form_submit_button('Registrar')
        if submit:
            if nombre and telefono and email and Vehiculo and DetallesVehiculo and placa and problema:
                # Guardar los datos en el estado de la sesión
                st.session_state['user_data'].append({
                    'Nombre': nombre,
                    'Teléfono': telefono,
                    'Correo': email,
                    "Vehiculo": Vehiculo,
                    'Detalles': DetallesVehiculo,
                    'Placa': placa,
                    'Problema': problema
                })
                st.success(f'Registro completado para {nombre}')
            else:
                st.error('Por favor, complete todos los campos.')

# Función para mostrar los registros de clientes
def mostrar_registros():
    st.title("Registros de Clientes")
    if st.session_state['user_data']:
        registros_df = pd.DataFrame(st.session_state['user_data'])
        st.dataframe(registros_df)
    else:
        st.write('No hay registros disponibles aún.')

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
    st.title("Mapa de Manila, Colombia")
    st.pydeck_chart(mapa)