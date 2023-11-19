
import streamlit as st

def calculate_energy(mass, height, gravity=9.81):
    return mass * gravity * height

# Streamlit application
st.title('Rock Fall Energy Calculator')
mass = st.number_input('Gi vekt av stein (i kg):', min_value=0, value=1000)
height = st.number_input('Gi høgden den fell i fritt fall (i meter):', min_value=1, value=50)

    # Button to perform calculation
if st.button('Calculate Energy'):
  energy = calculate_energy(mass, height)
  st.write(f'Energien steien har når den treff er: {energy/1000} kJ.')
