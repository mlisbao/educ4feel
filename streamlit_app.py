import streamlit as st
buttons = []
emojis = ["😡","😢","😐","😏","😃"]
st.title("Como voce está Agora?")
for i in range(5):
    buttons.append(st.button(emojis[str(i)]))
for i, button in enumerate(buttons):
    if button:
        st.write(f"{i} button was clicked")


