import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("5️⃣ 파일 업로드 - CSV 분석")

uploaded = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

if uploaded is not None:
    df = pd.read_csv(uploaded)

    st.success("CSV 파일 업로드 완료!")

    st.subheader("📄 데이터 미리 보기")
    st.dataframe(df)

    st.subheader("📊 기술 통계")
    st.write(df.describe())

    numeric_cols = df.select_dtypes(include=["float", "int"]).columns

    if len(numeric_cols) > 0:
        selected = st.selectbox("📌 시각화할 컬럼 선택", numeric_cols)

        fig, ax = plt.subplots()
        ax.hist(df[selected], bins=20)
        ax.set_title(f"{selected} 분포")
        st.pyplot(fig)
    else:
        st.info("수치형 데이터가 없습니다.")
else:
    st.info("CSV 파일을 업로드하면 분석이 시작됩니다.")
