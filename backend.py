from groq import Groq
import streamlit as st

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def analyze_plant_text(user_input):
    prompt = f"""
    You are an expert agricultural assistant.
    Analyze the plant problem described below and provide:

    - Plant name
    - Disease (or Healthy)
    - Symptoms
    - Causes
    - Organic treatment
    - Chemical treatment
    - Prevention

    Problem description:
    {user_input}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=600
    )

    return response.choices[0].message.content
