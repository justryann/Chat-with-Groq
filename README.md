# Groq Chatbot Streamlit App

This Streamlit app provides a simple interactive chatbot interface powered by Groq's ultrafast AI models. Users can type messages and receive instant responses from the Llama 3 model.

## Features

- Simple chat interface using Streamlit
- Powered by Groq's Llama 3 model (`llama3-8b-8192`)
- Loads API key securely from environment variables
- Real-time AI responses

## Tech Stack

- Python
- Streamlit
- Groq API
- python-dotenv

## Getting Started

1. **Install dependencies:**

   ```sh
   pip install streamlit groq python-dotenv
   ```

2. **Set up your Groq API key:**

   Create a `.env` file in the same directory as [`chat.py`](chat.py) and add your API key:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

3. **Run the app:**

   ```sh
   streamlit run chat.py
   ```

## File Structure

- [`chatbot`](chat.py): Main Streamlit chatbot application
- .env
---

*Developed for interactive AI-powered chat using Groq
