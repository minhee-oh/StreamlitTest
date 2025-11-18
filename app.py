import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- 제목 ---
st.title("🧊 Penguins 데이터 분석 앱")

# --- Task 1: 기본 UI 컴포넌트 ---
st.header("1️⃣ 기본 UI 컴포넌트")

name = st.text_input("이름을 입력하세요")
age = st.slider("나이를 선택하세요", 1, 100, 20)
gender = st.selectbox("성별을 선택하세요", ["남성", "여성", "기타"])
hobby = st.checkbox("나는 펭귄 데이터를 좋아한다")

if st.button("제출하기"):
    st.write("### 입력한 정보")
    st.write(f"- 이름: {name}")
    st.write(f"- 나이: {age}")
    st.write(f"- 성별: {gender}")
    st.write(f"- 펭귄 데이터 좋아함: {hobby}")

# --- Task 2: 데이터 표시하기 ---
st.header("2️⃣ 데이터 표시하기 (DataFrame & 통계 정보)")

# CSV 파일 읽기
df = pd.read_csv("penguins.csv")

st.subheader("📄 데이터프레임 미리보기")
st.dataframe(df)

st.subheader("📊 기본 통계 정보")
st.write(df.describe())
import numpy as np

st.title("Team Project Streamlit Dashboard")

st.write("이곳에 Task 3: 차트 그리기 기능을 구현합니다.")

st.header("Line Chart")
df = pd.DataFrame(np.random.randn(20, 3), columns=['a','b','c'])
st.line_chart(df)

st.header("Bar Chart")
st.bar_chart(df)

st.header("Area Chart")
st.area_chart(df)

st.header("Task 4: 인터랙티브 필터")
st.write("데이터를 조건에 따라 필터링해보는 예제입니다.")

# 예시 데이터 (상품/카테고리/매출)
data = {
    "상품": ["A", "B", "C", "D", "E", "F"],
    "카테고리": ["식품", "식품", "의류", "의류", "전자", "전자"],
    "매출": [10, 25, 30, 15, 40, 22]
}
df = pd.DataFrame(data)

st.subheader("원본 데이터")
st.dataframe(df)

# --- 사이드바 필터 ---
st.sidebar.header("필터 설정")

# 카테고리 선택 필터
selected_category = st.sidebar.multiselect(
    "카테고리 선택",
    options=df["카테고리"].unique(),
    default=list(df["카테고리"].unique())
)

# 매출 최소값 슬라이더
min_sales = st.sidebar.slider(
    "최소 매출 선택",
    min_value=int(df["매출"].min()),
    max_value=int(df["매출"].max()),
    value=int(df["매출"].min())
)

# --- 필터 적용 ---
filtered_df = df[
    (df["카테고리"].isin(selected_category)) &
    (df["매출"] >= min_sales)
]

st.subheader("필터링된 결과")
st.dataframe(filtered_df)

st.subheader("필터링된 결과 막대 그래프")
if not filtered_df.empty:
    chart_df = filtered_df.set_index("상품")["매출"]
    st.bar_chart(chart_df)
else:
    st.info("조건에 맞는 데이터가 없습니다. 필터를 조정해 보세요.")

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