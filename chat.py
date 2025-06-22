import os
from dotenv import load_dotenv

from groq import Groq
import streamlit as st

st.header('Chat with Groq')
st.write('Hello I am Groq Chatbot, Ultrafast AI Chatbot')
message = st.text_input("")
# Load environment variables
load_dotenv()

client = Groq(
    # This is the default and can be omitted
    api_key=os.environ.get("GROQ_API_KEY"),
)
if message : 
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": message,
                },
                
            ],
            model="llama3-8b-8192",
        )

        st.write(chat_completion.choices[0].message.content)