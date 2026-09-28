import streamlit as st

st.set_page_config(
    page_title="AI Quiz",
    page_icon="📝",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background:#050912;
    color:white;
}

.title {
    font-size:42px;
    color:#00c6ff;
    font-weight:bold;
}

.quiz {
    padding:30px;
    background:#0b1627;
    border:1px solid #173454;
    border-radius:20px;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">📝 AI Quiz</div>',
    unsafe_allow_html=True
)

st.write("Test your programming knowledge.")

st.markdown("""
<div class="quiz">

<h3>Question 1</h3>

<p>Which language is commonly used for Artificial Intelligence?</p>

</div>
""", unsafe_allow_html=True)

answer = st.radio(
    "Select your answer:",
    [
        "Python",
        "HTML",
        "CSS",
        "SQL"
    ]
)

if st.button("Check Answer"):

    if answer == "Python":
        st.success("🎉 Correct answer!")
    else:
        st.error("Try again!")