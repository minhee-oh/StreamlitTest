import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="CSV 파일 분석 페이지",
    page_icon="📊",
    layout="wide"
)

st.title("📊 CSV 파일 분석 페이지")

# ----------------------
# 1. CSV 자동 로드
# ----------------------
csv_path = "penguins.csv"   # 같은 폴더에 있어야 함
df = pd.read_csv(csv_path)

st.success(f"로컬 CSV 파일을 불러왔습니다: {csv_path}")

# ----------------------
# 2. 데이터 미리 보기
# ----------------------
st.subheader("📄 데이터 미리 보기")
st.dataframe(df)

# ----------------------
# 3. 기본 정보
# ----------------------
st.subheader("ℹ️ 기본 정보")
st.write("행(row) 수:", df.shape[0])
st.write("열(column) 수:", df.shape[1])
st.write("열 목록:", list(df.columns))

# ----------------------
# 4. 기술 통계
# ----------------------
st.subheader("📊 기술 통계")
st.write(df.describe())

# ----------------------
# 5. 수치형 컬럼 선택 후 그래프
# ----------------------
st.subheader("📈 컬럼 분포 시각화")

numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns

if len(numeric_cols) > 0:
    selected_col = st.selectbox("시각화할 수치형 컬럼 선택", numeric_cols)

    fig, ax = plt.subplots()
    ax.hist(df[selected_col], bins=20)
    ax.set_title(f"{selected_col} 분포")
    ax.set_xlabel(selected_col)
    ax.set_ylabel("Frequency")

    st.pyplot(fig)
else:
    st.info("수치형 데이터가 없습니다.")