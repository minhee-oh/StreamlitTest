import streamlit as st
import pandas as pd

st.title("2️⃣ 데이터 표시하기")

df = pd.read_csv("penguins.csv")

st.subheader("📄 데이터프레임 미리보기")
st.dataframe(df)

st.subheader("📊 기본 통계 정보")
st.write(df.describe())
