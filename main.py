import streamlit as st
from agents import chat
from iterative_runner import run_refinement_loop

st.set_page_config(page_title="Argument Refinement Loop", page_icon="🧠")
st.title("🧠 Argument Refinement Loop")

# Initialize session state variables
if "topic" not in st.session_state:
    st.session_state.topic = None
if "argument" not in st.session_state:
    st.session_state.argument = None
if "result" not in st.session_state:
    st.session_state.result = None

# Step 1: Topic selection
st.header("Step 1: Enter a debatable topic")
user_topic = st.text_input("Or leave blank to auto-generate one with the model:")

if st.button("Continue"):
    if user_topic.strip():
        st.session_state.topic = user_topic
    else:
        st.session_state.topic = chat.choose_topic(interactive=False)
    st.session_state.argument = None  # reset argument on new topic
    st.session_state.result = None    # reset result too

if st.session_state.topic:
    st.success(f"✅ Selected topic: **{st.session_state.topic}**")

    # Step 2: Argument input
    st.header("Step 2: Provide your argument (optional)")
    user_argument = st.text_area(
        "Write your own argument here, or leave blank to let the model generate it:",
        value=st.session_state.argument or ""
    )

    if st.button("Generate or Refine Argument"):
        if user_argument.strip():
            initial_argument = user_argument.strip()
        else:
            initial_argument = chat.get_initial_argument(st.session_state.topic, interactive=False)

        st.session_state.argument = initial_argument
        st.session_state.result = run_refinement_loop(st.session_state.topic, initial_argument)

# Display results
if st.session_state.result:
    st.subheader("📉 Baseline Argument")
    st.write(st.session_state.result["baseline"])

    st.subheader(f"📈 Best Argument (Score: {st.session_state.result['score']:.1f})")
    st.write(st.session_state.result["best"])

    st.success("🎯 Optimization complete!")
