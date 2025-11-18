import streamlit as st
import pandas as pd

st.title("4️⃣ 인터랙티브 필터링")

data = {
    "상품": ["A", "B", "C", "D", "E", "F"],
    "카테고리": ["식품", "식품", "의류", "의류", "전자", "전자"],
    "매출": [10, 25, 30, 15, 40, 22]
}
df = pd.DataFrame(data)

st.subheader("📦 원본 데이터")
st.dataframe(df)

st.sidebar.header("🔍 필터 설정")

selected_category = st.sidebar.multiselect(
    "카테고리 선택",
    df["카테고리"].unique(),
    default=df["카테고리"].unique()
)

min_sales = st.sidebar.slider(
    "최소 매출",
    int(df["매출"].min()),
    int(df["매출"].max()),
    int(df["매출"].min())
)

filtered_df = df[
    (df["카테고리"].isin(selected_category)) &
    (df["매출"] >= min_sales)
]

st.subheader("📊 필터링된 결과")
st.dataframe(filtered_df)

st.subheader("📈 필터링된 막대그래프")
if not filtered_df.empty:
    st.bar_chart(filtered_df.set_index("상품")["매출"])
else:
    st.warning("조건에 맞는 데이터가 없습니다.")
