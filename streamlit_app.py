import streamlit as st
buttons = []
emojis = ["😡","😢","😐","😏","😃"]

st.title("Como voce está Agora?")
cols = st.columns(5,gap="medium")

for i, x in enumerate(cols):
    buttons.append(x.button(emojis[i]))

for i, button in enumerate(buttons):
    if button:
        st.write(f"{i} button was clicked")


