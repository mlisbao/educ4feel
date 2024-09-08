import streamlit as st

st.markdown(
    """
<style>
button.label {font-size: 116px}
</style>
""",
    unsafe_allow_html=True,
)

buttons = []
emojis = ["😡","😢","😐","😏","😃"]

st.title("Como voce está Agora?")
cols = st.columns(5)

for i, x in enumerate(cols):
    buttons.append(x.button(label = emojis[i]))

for i, button in enumerate(buttons):
    if button:
        st.write(f"{i} button was clicked")


