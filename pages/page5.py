import streamlit as st


if "a" not in st.session_state:
    st.session_state.a = 0

clicked = st.button("加一", width=500)
if clicked:
    st.session_state.a += 1
st.metric("当前计数：", st.session_state.a)

print(st.session_state)