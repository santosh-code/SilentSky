import streamlit as st
from backend.tools import reflect_emotions, gita_verse_for_emotion
from db.journal_db import insert_journal

st.set_page_config(page_title="SilentSky ✨", layout="centered")
st.title("🌌 SilentSky – Daily Emotional Journal")

user_id = st.text_input("Enter your user ID")

st.markdown("---")

with st.form("journal_form"):
    st.subheader("📝 Log your day")
    entry = st.text_area("What happened today?")
    emotion = st.text_input("How did you feel?")
    submitted = st.form_submit_button("Save Entry")

    if submitted and user_id:
        insert_journal(user_id, entry, emotion)
        st.success("Entry saved successfully ✨")

st.markdown("---")

if user_id:
    if st.button("🤖 Get Nightly Reflection"):
        with st.spinner("Analyzing your day..."):
            reflection = reflect_emotions(user_id)
            st.text_area("Reflection", reflection, height=200)

    emotion_for_gita = st.text_input("🎭 Want Gita advice for a feeling?")
    if st.button("🕉️ Get Gita Verse"):
        with st.spinner("Fetching wisdom from the Gita..."):
            verse = gita_verse_for_emotion(emotion_for_gita)
            st.text_area("Gita Wisdom", verse, height=150)