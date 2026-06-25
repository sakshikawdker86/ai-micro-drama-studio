import streamlit as st

from prompts import create_story_prompt
from gemini_service import generate_story

st.set_page_config(
    page_title="AI Micro Drama Studio",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 AI Micro Drama Studio")
st.write("Generate AI-powered micro drama scripts using Gemini.")

col1, col2 = st.columns(2)

with col1:
    genre = st.selectbox(
        "Genre",
        ["Romance", "Comedy", "Thriller", "Horror", "Family"]
    )

    language = st.selectbox(
        "Language",
        ["Hindi", "English", "Hinglish"]
    )

with col2:
    audience = st.selectbox(
        "Target Audience",
        ["Kids", "Teenagers", "18-25", "25-40", "Family"]
    )

    duration = st.selectbox(
        "Episode Length",
        ["30 Seconds", "1 Minute", "2 Minutes"]
    )

generate = st.button("✨ Generate Story")

if generate:

    prompt = create_story_prompt(
        genre,
        language,
        audience,
        duration
    )

    with st.spinner("🎬 Generating AI Micro Drama..."):
        story = generate_story(prompt)

    st.success("✅ AI Content Generated Successfully!")

    st.markdown(story)