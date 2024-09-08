import streamlit as st

st.markdown('<style>.big-font {font-size:116px !important;}</style>', unsafe_allow_html=True)

buttons = []
emojis = ["😡","😢","😐","😏","😃"]

st.title("Como voce está Agora?")
cols = st.columns(5)

for i, x in enumerate(cols):
    buttons.append(x.button(emojis[i]))

for i, button in enumerate(buttons):
    if button:
        st.write(f"{i} button was clicked")
