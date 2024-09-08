import streamlit as st

st.markdown("""<style>
.stButton > button {
    
    background-color: Transparent;
    background-repeat:no-repeat;
    border: none;
    cursor:pointer;
    overflow: hidden;
    outline:none;
    padding : auto;
    margin: 0 auto;
}
.stButton > button > div > p {
    font-size: 116px;
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
        picture = st.camera_input("")
        if picture:
            st.image(picture)

