import streamlit as st

st.set_page_config(page_title = "Mind Reader", page_icon = ":exploding_head:", layout = "centered")

st.title("🔮 Are you telepathic? ")
st.subheader("I can read your mind. Trust me.")

number = st.number_input("Think of a number. ", step = 1)

if st.button("Read my mind!"):
    st.success(f"💥 BOOM! You were thinking of... **{int(number)}**, weren't you?")
    st.balloons()