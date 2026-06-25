import streamlit as st
from parser import parse_sections
from prompts import create_story_prompt
from gemini_service import generate_story

st.set_page_config(
    page_title="AI Micro Drama Studio",
    page_icon="🎬",
    layout="wide"
)
if "history" not in st.session_state:
    st.session_state.history = []

st.title("🎬 AI Micro Drama Studio")


st.sidebar.title("📚 Story History")
st.sidebar.markdown("---")
st.sidebar.caption("🚀 AI Micro Drama Studio")
st.sidebar.caption("Built with Python + Streamlit + Gemini")

if len(st.session_state.history) == 0:
    st.sidebar.info("No stories generated yet.")
else:
    for index, item in enumerate(st.session_state.history, start=1):
        st.sidebar.write(f"{index}. {item['genre']}")
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

st.caption("Generate complete AI-powered short drama content in seconds.")
col1, col2, col3 = st.columns(3)

col1.metric("Stories Generated", len(st.session_state.history))

col2.metric("Current Genre", genre)

col3.metric("Language", language)

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
        st.session_state.history.append({
           "genre": genre,
           "story": story
       })
        sections = parse_sections(story)
        if "Title" in sections:
            st.header(sections["Title"].strip())

        with st.expander("👥 Characters", expanded=True):
            st.markdown(sections.get("Characters", ""))

        with st.expander("🎬 Story", expanded=True):
             st.markdown(sections.get("Story", ""))

        with st.expander("🎨 Thumbnail Prompt"):
            st.code(sections.get("Thumbnail Prompt", ""), language="text")

        with st.expander("🎙 Voiceover Script"):
            st.markdown(sections.get("Voiceover Script", ""))

        with st.expander("📱 Instagram Caption"):
           st.markdown(sections.get("Instagram Caption", ""))
  
        with st.expander("🏷️ Hashtags"):
            st.download_button(
                label="📥 Download Story",
                data=story,
                file_name="micro_drama_story.md",
                mime="text/markdown"
            )
            st.markdown(sections.get("Hashtags", ""))

    st.success("✅ AI Content Generated Successfully!")

    st.markdown(story)