import streamlit as st

st.markdown("""<style>
button {
  background-color: Transparent;
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 100px;
  margin: 4px 2px;
  cursor: pointer;
}
            </style>""", unsafe_allow_html=True)

buttons = []
emojis = ["😡","😢","😐","😏","😃"]

st.title("Como voce está Agora?")
cols = st.columns(5)

for i, x in enumerate(cols):
    buttons.append(x.button(emojis[i]))
    

for i, button in enumerate(buttons):
    if button:
        st.write(f"{i} button was clicked")
