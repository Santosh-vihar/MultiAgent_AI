import os
from groq import Groq
import streamlit as st

def get_groq_api_key():
    # 1. Direct environment variable check
    if os.environ.get("GROQ_API_KEY"):
        return os.environ["GROQ_API_KEY"]
        
    # 2. Try fetching from Streamlit secrets
    try:
        # Check exact key
        if "GROQ_API_KEY" in st.secrets:
            return st.secrets["GROQ_API_KEY"]
            
        # Fallback: Search keys for 'groq' case-insensitive
        for k in st.secrets.keys():
            if "groq" in k.lower():
                return st.secrets[k]
                
        # Fallback: Search keys for generic 'api_key' or 'key'
        for k in st.secrets.keys():
            if "key" in k.lower():
                return st.secrets[k]
    except Exception:
        pass
        
    return None

def ask_hf(prompt):
    api_key = get_groq_api_key()
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