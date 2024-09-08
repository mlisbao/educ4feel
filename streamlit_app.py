import streamlit as st

st.markdown("""<style>
.emoji {font-size: 3.7em;
    background-color: Transparent;
    background-repeat:no-repeat;
    border: none;
    cursor:pointer;
    overflow: hidden;
    outline:none;
    padding : auto;
    margin: 0 auto;
            </style>""", unsafe_allow_html=True)

buttons = []
emojis = ["😡","😢","😐","😏","😃"]

st.title("Como voce está Agora?")
cols = st.columns(5)

for i, x in enumerate(cols):
    #buttons.append(x.button(emojis[i],key='big_font_button'))
    #buttons.append(x.button(emojis[i],key='big_font_button'))
buttons.append(x.button(f'<span class="emoji">Big Font Button</span>', key='big_font_button', help='Button with increased font size'))

for i, button in enumerate(buttons):
    if button:
        st.write(f"{i} button was clicked")
