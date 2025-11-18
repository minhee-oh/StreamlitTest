import streamlit as st
import pandas as pd

st.set_page_config(page_title="Task 6 - Layout Demo")

st.title("6️⃣ Task 6: 레이아웃 구성 데모")

# penguins.csv 로드
df = pd.read_csv("penguins.csv")

# ------------------------------
# 📌 Columns 레이아웃 (3열)
# ------------------------------
st.subheader("📌 Columns 레이아웃 (Left / Center / Right)")

left_col, center_col, right_col = st.columns(3)

with left_col:
    st.write("📍 왼쪽 컬럼")
    st.dataframe(df.head(3))

with center_col:
    st.write("📍 중앙 컬럼")
    st.dataframe(df.iloc[3:6])

with right_col:
    st.write("📍 오른쪽 컬럼")
    st.dataframe(df.iloc[6:9])

# ------------------------------
# 📌 Tabs 레이아웃
# ------------------------------
st.subheader("📌 Tabs 레이아웃")

tab1, tab2, tab3 = st.tabs(["탭 1", "탭 2", "탭 3"])

with tab1:
    st.write("📄 탭 1: penguins 데이터 미리보기")
    st.dataframe(df.head())

with tab2:
    st.write("📊 탭 2: 기술 통계")
    st.write(df.describe())

with tab3:
    st.write("🔎 탭 3: species별 count")
    st.bar_chart(df["species"].value_counts())

# ------------------------------
# 📌 Expander 레이아웃
# ------------------------------
st.subheader("📌 Expander 예시")

with st.expander("펭귄 데이터 전체 보기 (눌러서 펼치기)"):
    st.dataframe(df)
