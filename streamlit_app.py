import streamlit as st
buttons = []
emojis = ["😡","😢","😐","😏","😃"]

st.title("Como voce está Agora?")

cols = st.columns(5)

for i, x in enumerate(cols):
    x.button(emojis[i])

for i, button in enumerate(x):
    if button:
        st.write(f"{i} button was clicked")


