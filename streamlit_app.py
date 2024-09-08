import streamlit as st
buttons = []
st.title("Como voce está Agora?")
for i in range(5):
    buttons.append(st.button(str(i)))
for i, button in enumerate(buttons):
    if button:
        st.write(f"{i} button was clicked")


