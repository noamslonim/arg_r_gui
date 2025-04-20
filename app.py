import streamlit as st
import openai
import os

# Make sure your API key is available
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Argument Refinement Loop", layout="centered")
st.title("🧠 Argument Refinement Loop")

# User input for topic
st.subheader("Step 1: Enter a debatable topic")
topic = st.text_input("Or leave blank to auto-generate one")

# User input for initial argument
st.subheader("Step 2: Provide your argument (optional)")
argument = st.text_area("Or let the model generate one for you")

# Button to start the loop
if st.button("Start Refinement Loop"):
    if not topic:
        st.warning("Automatic topic generation isn't wired in yet — please enter a topic.")
    else:
        st.success("Argument refinement would start here... (this is a placeholder)")