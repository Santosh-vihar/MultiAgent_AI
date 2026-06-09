import os
from groq import Groq
import streamlit as st

def ask_hf(prompt):
    # Retrieve key from environment variables or Streamlit secrets
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        try:
            api_key = st.secrets.get("GROQ_API_KEY")
        except Exception:
            pass

    if not api_key or not api_key.strip():
        raise ValueError("GROQ_API_KEY is not configured. Please set it in environment variables or Streamlit secrets.")

    client = Groq(
        api_key=api_key
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_tokens=1500
    )

    return response.choices[0].message.content