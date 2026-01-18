import requests
import streamlit as st

def get_openai_response(input_text):
    response = requests.post(
        "http://localhost:8000/song/invoke",
        json={
            "input": {
                "topic": input_text
            }
        }
    )
    
    return response.json()["output"]["content"]

# Streamlit Framework
st.title("🎵 Song Generator using LangChain")

topic = st.text_input("Enter a topic for the Song:")

if topic:
    st.write("🎶 Generating song...")
    song = get_openai_response(topic)
    st.write(song)
    st.balloons()
