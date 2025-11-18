import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 페이지 설정 (레이아웃 스타일만)
st.set_page_config(
    page_title="Streamlit Dashboard",
    page_icon="🐧",
    layout="wide"
)

# ================================
# 메인 제목
# ================================
st.title("Streamlit 실습")
st.markdown("---")

# ================================
# Task 1: 기본 UI 컴포넌트
# ================================
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

st.markdown("---")

# ================================
# Task 2: 데이터 표시하기 (DataFrame & 통계 정보)
# ================================
st.header("2️⃣ 데이터 표시하기 (DataFrame & 통계 정보)")

# CSV 파일 읽기 (penguins.csv 사용)
df_penguins = pd.read_csv("penguins.csv")

st.subheader("📄 데이터프레임 미리보기")
st.dataframe(df_penguins)

st.subheader("📊 기본 통계 정보")
st.write(df_penguins.describe())

st.markdown("---")

# ================================
# Task 3: 차트 그리기 - 선/막대/영역 차트
# ================================

st.header("3️⃣ 차트 그리기 (Line / Bar / Area)")

chart_df = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])

st.subheader("📈 Line Chart")
st.line_chart(chart_df)

st.subheader("📊 Bar Chart")
st.bar_chart(chart_df)

st.subheader("📉 Area Chart")
st.area_chart(chart_df)

st.markdown("---")

# ================================
# Task 4: 인터랙티브 필터 - 데이터 필터링
# ================================
st.header("4️⃣ Task 4: 인터랙티브 필터")
st.write("데이터를 조건에 따라 필터링해보는 예제입니다.")

# 예시 데이터 (상품/카테고리/매출)
data = {
    "상품": ["A", "B", "C", "D", "E", "F"],
    "카테고리": ["식품", "식품", "의류", "의류", "전자", "전자"],
    "매출": [10, 25, 30, 15, 40, 22]
}
df_sales = pd.DataFrame(data)

st.subheader("📦 원본 데이터")
st.dataframe(df_sales)

# --- 사이드바 필터 ---
st.sidebar.header("🔍 필터 설정")

# 카테고리 선택 필터
selected_category = st.sidebar.multiselect(
    "카테고리 선택",
    options=df_sales["카테고리"].unique(),
    default=list(df_sales["카테고리"].unique())
)

# 매출 최소값 슬라이더
min_sales = st.sidebar.slider(
    "최소 매출 선택",
    min_value=int(df_sales["매출"].min()),
    max_value=int(df_sales["매출"].max()),
    value=int(df_sales["매출"].min())
)

# --- 필터 적용 ---
filtered_df = df_sales[
    (df_sales["카테고리"].isin(selected_category)) &
    (df_sales["매출"] >= min_sales)
]

st.subheader("📊 필터링된 결과")
st.dataframe(filtered_df)

st.subheader("📈 필터링된 결과 막대 그래프")
if not filtered_df.empty:
    chart_df_filtered = filtered_df.set_index("상품")["매출"]
    st.bar_chart(chart_df_filtered)
else:
    st.info("조건에 맞는 데이터가 없습니다. 필터를 조정해 보세요.")

st.markdown("---")

# ================================
# CSV 파일 분석 페이지 (penguins.csv 다시 사용)
# ================================
st.title("5️⃣ Task 5: CSV 파일 업로드")

# 1. CSV 자동 로드
csv_path = "penguins.csv"   # 같은 폴더에 있어야 함
df = pd.read_csv(csv_path)

st.success(f"로컬 CSV 파일을 불러왔습니다: {csv_path}")

# 2. 데이터 미리 보기
st.subheader("📄 데이터 미리 보기")
st.dataframe(df)

# 3. 기본 정보
st.subheader("ℹ️ 기본 정보")
st.write("행(row) 수:", df.shape[0])
st.write("열(column) 수:", df.shape[1])
st.write("열 목록:", list(df.columns))

# 4. 기술 통계
st.subheader("📊 기술 통계")
st.write(df.describe())

st.subheader("📈 컬럼 분포 히스토그램")

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

st.markdown("---")


# ==========================================================
# 6️⃣ Task 6: 레이아웃 구성 (Columns, Tabs, Expander)
# ==========================================================
st.header("6️⃣ 레이아웃 구성 데모")

# penguins.csv 로드
df_penguins_6 = pd.read_csv("penguins.csv")

# ------------------------------
# 📌 Columns 레이아웃 (3열)
# ------------------------------
st.subheader("📌 Columns 레이아웃 (Left / Center / Right)")

left_col, center_col, right_col = st.columns(3)

with left_col:
    st.write("📍 왼쪽 컬럼")
    st.dataframe(df_penguins_6.head(3))

with center_col:
    st.write("📍 중앙 컬럼")
    st.dataframe(df_penguins_6.iloc[3:6])

with right_col:
    st.write("📍 오른쪽 컬럼")
    st.dataframe(df_penguins_6.iloc[6:9])


# ------------------------------
# 📌 Tabs 레이아웃
# ------------------------------
st.subheader("📌 Tabs 레이아웃")

tab1, tab2, tab3 = st.tabs(["탭 1", "탭 2", "탭 3"])

with tab1:
    st.write("📄 탭 1: penguins 데이터 미리보기")
    st.dataframe(df_penguins_6.head())

with tab2:
    st.write("📊 탭 2: 기술 통계")
    st.write(df_penguins_6.describe())

with tab3:
    st.write("🔎 탭 3: species별 count")
    st.bar_chart(df_penguins_6["species"].value_counts())


# ------------------------------
# 📌 Expander 레이아웃
# ------------------------------
st.subheader("📌 Expander 예시")

with st.expander("펭귄 데이터 전체 보기 (눌러서 펼치기)"):
    st.dataframe(df_penguins_6)
