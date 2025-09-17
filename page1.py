import streamlit as st
import pandas as pd

st.title("######你好，这是我的测试网站！！！")
"## 早上好！！!!!"
a = 222 *3
a

[11, 22, 33]

{"a": 123, "b": 456}
{"a": 123, "b": 456}

st.image("./维元logo.jpg", width=300)
df = pd.DataFrame({"学号": ["01", "02", "03"],
              "班级": ["一班", "二班", "三班"]})

st.dataframe(df)
st.divider()
st.table(df)