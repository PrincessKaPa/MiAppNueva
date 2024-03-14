import streamlit as st
from PIL import Image

st.title("My first multimodal app") #Una app web que solo muestra un tìtulo
st.title("Welcome")
st.header("This is a safe place. Fel free to be honest, only you can access to the information you provide.")
st.write("In the fields below you will find the instructions for each interaction. The objective is to analyze how you feel according to the input you give and then give you a feedback according to the results. This is an experiment, therefore the information given by the machine could not be completely accurate. Do not trust this completely ;)")
image = Image.open('emociones.jpeg')

st.image(image, caption="emociones")


texto = st.text_input("Escribe algo", "Este es mi texto")
st.write("Esto es lo que escribiste: ", texto)

st.subheader("Ahora usemos 2 columnas jeje")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Te presento la primera columna :)")
  st.write("Las interfaces multomodales mejoran la experiencia de usuario")
  resp = st.checkbox("Estoy de acuerdo")
  if resp:
    st.write("¡Correcto!")

with col2:
  st.subheader("Y aquí está la segunda columna ^^")
  modo = st.radio("¿Qué modalidad es la principal en tu interfaz?", ("Visual", "Auditiva", "Táctil"))
  if modo == "Visual":
    st.write("La vista es fundamental en tu interfaz")
  if modo == "Auditiva":
    st.write("La audición es fundamental para tu interfaz")
  if modo == "Táctil":
    st.write("El tacto es fundamental para tu interfaz")

st.subheader("Uso de botones")
if st.button("Presiona el botón"):
  st.write("Gracias por presionar")
else:
  st.write("No lo has presionado aún")
