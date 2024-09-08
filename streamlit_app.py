import streamlit as st
buttons = []
emojis = ["😡","😢","😐","😏","😃"]
cols = st.columns(5)
st.title("Como voce está Agora?")

for i, x in enumerate(cols):
    x.buttons.append(st.button(emojis[i]))

for i, button in enumerate(buttons):
    if button:
        st.write(f"{i} button was clicked")


