from textblob import TextBlob
import pandas as pd
import streamlit as st
from PIL import Image
from googletrans import Translator

import os
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
import time
import glob
from gtts import gTTS


st.title("MY FIRST MULTIMODAL APP") 
st.title("Welcome!")
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
      text= st.write( 'I am so glad everything seems to be fine 😊')
  elif x <= -0.5:
      text= st.write( "I'm so sorry to hear this. I hope listening to this song can encourage you. And in the meantime you can practice some Spanish")
      st.video(video_bytes)
  else:
      text= st.write( "I'm not sure I can help you. But just in case, remember that God loves you")
st.write("You can keep practicing by listening to my response in Spanish")

st.subheader("Press the button to listen to the translation")



result = streamlit_bokeh_events(
    stt_button,
    events="GET_TEXT",
    key="listen",
    refresh_on_update=False,
    override_height=75,
    debounce_time=0)

if result:
    if "GET_TEXT" in result:
        st.write(result.get("GET_TEXT"))
    try:
        os.mkdir("temp")
    except:
        pass
    st.title("Texto a Audio")
    translator = Translator()
    
    text = str(result.get("GET_TEXT"))
  
input_language = "en"
 
output_language = "es"
  
    
def text_to_speech(input_language, output_language, text, tld):
  translation = translator.translate(text, src=input_language, dest=output_language)
  trans_text = translation.text
  tts = gTTS(trans_text, lang=output_language, tld=tld, slow=False)
  try:
      my_file_name = text[0:20]
  except:
      my_file_name = "audio"
  tts.save(f"temp/{my_file_name}.mp3")
  return my_file_name, trans_text
    
 
    if st.button("convertir"):
        result, output_text = text_to_speech(input_language, output_language, text, tld)
        audio_file = open(f"temp/{result}.mp3", "rb")
        audio_bytes = audio_file.read()
        st.markdown(f"## Your audio:")
        st.audio(audio_bytes, format="audio/mp3", start_time=0)
    
        if display_output_text:
            st.markdown(f"## Texto de salida:")
            st.write(f" {output_text}")
    
    
    def remove_files(n):
        mp3_files = glob.glob("temp/*mp3")
        if len(mp3_files) != 0:
            now = time.time()
            n_days = n * 86400
            for f in mp3_files:
                if os.stat(f).st_mtime < now - n_days:
                    os.remove(f)
                    print("Deleted ", f)

    remove_files(7)

try:
    os.mkdir("temp")
except:
    pass

texto= text

tld="es"

def text_to_speech(texto, tld):
    
    tts = gTTS(texto,"es", tld, slow=False)
    try:
        my_file_name = texto[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, texto



#display_output_text = st.checkbox("Verifica el texto")

if st.button("convertir"):
    result, output_texto = text_to_speech(texto, tld)
    audio_file = open(f"temp/{result}.mp3", "rb")
    audio_bytes = audio_file.read()
    st.markdown(f"## Tú audio:")
    st.audio(audio_bytes, format="audio/mp3", start_time=0)

    #if display_output_text:
    st.markdown(f"## Texto en audio:")
    st.write(f" {output_texto}")


def remove_files(n):
    mp3_files = glob.glob("temp/*mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)
                print("Deleted ", f)


remove_files(7)

