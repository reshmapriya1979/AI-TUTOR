import streamlit as st
from google import genai

st.set_page_config(
    page_title="AI Tutor",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background: #050912;
    color: white;
}

.title {
    font-size: 42px;
    color: #00c6ff;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">🤖 AI Smart Tutor</div>',
    unsafe_allow_html=True
)

st.write("Ask questions and learn with your AI-powered tutor.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Ask your AI Tutor anything...")

if question:

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    try:
        client = genai.Client(api_key)

        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=question
        )

        answer = response.text

    except Exception as e:
        answer = f"Error: {e}"

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    with st.chat_message("assistant"):
        st.markdown(answer)