import streamlit as st
import pandas as pd
import numpy as np

st.title("3️⃣ 차트 그리기")

data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])

st.header("📈 Line Chart")
st.line_chart(data)

st.header("📊 Bar Chart")
st.bar_chart(data)

st.header("📉 Area Chart")
st.area_chart(data)
