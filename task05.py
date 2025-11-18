import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="CSV 분석 페이지",
    page_icon="📊",
    layout="wide"
)

st.title("📊 CSV 파일 분석 페이지")

# ----------------------
# 1. CSV 파일 업로드
# ----------------------
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요.", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 데이터 미리 보기")
    st.dataframe(df)

    # ----------------------
    # 2. 기본 정보
    # ----------------------
    st.subheader("ℹ️ 기본 정보")
    st.write("행(row) 수:", df.shape[0])
    st.write("열(column) 수:", df.shape[1])
    st.write("열 목록:", list(df.columns))

    # ----------------------
    # 3. 통계 요약
    # ----------------------
    st.subheader("📊 기술 통계")
    st.write(df.describe())

    # ----------------------
    # 4. 선택한 컬럼 시각화
    # ----------------------
    st.subheader("📈 컬럼 시각화")

    numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns

    if len(numeric_cols) > 0:
        col = st.selectbox("시각화할 수치형 컬럼 선택", numeric_cols)

        fig, ax = plt.subplots()
        ax.hist(df[col], bins=20)
        ax.set_title(f"{col} 분포")
        st.pyplot(fig)
    else:
        st.info("수치형 데이터가 없습니다.")
else:
    st.info("CSV 파일을 업로드해주세요!")
