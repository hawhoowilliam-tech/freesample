import streamlit as st

with st.sidebar:
    name = st.text_input("请输入你的大名：")
    if name:
        st.write(f"你好， {name}")

column1, column2, column3 = st.columns([1,2,3])
with column1:
    password = st.text_input("请输入你的密码：", type="password")


with column2:
    paragragh = st.text_area("请输入你的个人介绍：")

with column3:
    age = st.number_input("请输入你的年龄：", value=20, min_value=0, max_value=100, step=1)
    st.write(f"你的年龄是：{age}岁")


checked = st.checkbox("我同意以上的乱七八糟看不懂的东西")
if checked:
    st.write("感谢你的建议！")

st.divider()

submitted = st.button("提交")
if submitted:
    st.write("提交成功！")