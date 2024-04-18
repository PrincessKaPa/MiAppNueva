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
st.header("This is a safe place. Feel free to be honest, only you can access to the information you provide.")
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


st.write("If you feel more comfortable speaking, press the button and tell me how you feel:")


stt_button = Button(label=" Speak ", width=200)

stt_button.js_on_event("button_click", CustomJS(code="""
    var recognition = new webkitSpeechRecognition();
    recognition.continuous = true;
    recognition.interimResults = true;
 
    recognition.onresult = function (e) {
        var value = "";
        for (var i = e.resultIndex; i < e.results.length; ++i) {
            if (e.results[i].isFinal) {
                value += e.results[i][0].transcript;
            }
        }
        if ( value != "") {
            document.dispatchEvent(new CustomEvent("GET_TEXT", {detail: value}));
        }
    }
    recognition.start();
    """))

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
    translation = translator.translate(result.get("GET_TEXT"), src="es", dest="en")
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
