from textblob import TextBlob
import pandas as pd
import streamlit as st
from PIL import Image
from googletrans import Translator

st.title("My first multimodal app") 
st.title("Welcome")
st.header("This is a safe place. Fel free to be honest, only you can access to the information you provide.")
st.write("In the fields below you will find the instructions for each interaction. The objective is to analyze how you feel according to the input you give and then give you a feedback according to the results. This is an experiment, therefore the information given by the machine could not be completely accurate. Do not trust this completely ;)")
image = Image.open('emociones.jpeg')

st.image(image, caption="mind and emotions")
translator = Translator()
video_file = open('Redimi2 - Todo Va a Estar Bien Evan Craft.mp4', 'rb')
video_bytes = video_file.read()

text = st.text_input("Type something expressing how you feel", "This is my text")
st.write("This is what you wrote: ", text)
if text:
  translation = translator.translate(text, src="es", dest="en")
  trans_text = translation.text
  blob = TextBlob(trans_text)
  st.write('Polarity: ', round(blob.sentiment.polarity,2))
  st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))
  x=round(blob.sentiment.polarity,2)
  if x >= 0.5:
      st.write( 'I am so glad everything seems to be fine 😊')
  elif x <= -0.5:
      st.write( "I'm so sorry to hear this. I hope listening to this song can encourage you: ")
      st.video(video_bytes)
    st.write( "And in the meantime you can practice some Spanish")
  else:
      st.write( "I'm not sure I can help you. But just in case, remember that God loves you")

      

st.write("Now you will see the result of the analysis based on what you wrote. And according to that, you will recieve recommendations.")

st.subheader("Press the button to see results")
if st.button("Analyse"):
  st.write("Gracias por presionar")
else:
  st.write("You haven't pressed the button yet")


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


