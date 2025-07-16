import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="MBTI Countries Analysis", layout="wide")

st.title("🌍 Countries MBTI 16 Types Analysis")

# 같은 폴더에 있는 CSV 파일을 바로 읽기
file_path = "countriesMBTI_16types.csv"
df = pd.read_csv(file_path)

st.subheader("데이터 미리 보기")
st.dataframe(df.head())

# MBTI 컬럼만 추출
mbti_columns = df.columns[1:]

# 전세계 평균 비율 계산
global_avg = df[mbti_columns].mean().sort_values(ascending=False).reset_index()
global_avg.columns = ['MBTI', 'Average']

st.subheader("🌐 전세계 MBTI 평균 비율")
chart = alt.Chart(global_avg).mark_bar().encode(
    x=alt.X('MBTI', sort='-y'),
    y='Average',
    color='MBTI'
).properties(width=800, height=400)
st.altair_chart(chart, use_container_width=True)

# 풍선 효과
st.balloons()

# 국가별 가장 흔한 MBTI 유형 찾기
most_common_mbti = df[['Country']].copy()
most_common_mbti['Most Common MBTI'] = df[mbti_columns].idxmax(axis=1)
most_common_mbti['Percentage'] = df[mbti_columns].max(axis=1)

st.subheader("🏆 국가별 가장 흔한 MBTI 유형")
st.dataframe(most_common_mbti)

# 선택한 국가의 MBTI 분포 시각화
selected_country = st.selectbox("국가를 선택해서 MBTI 분포를 확인하세요", df['Country'].unique())

if selected_country:
    country_row = df[df['Country'] == selected_country]
    country_mbti = country_row[mbti_columns].T.reset_index()
    country_mbti.columns = ['MBTI', 'Percentage']

    st.subheader(f"📊 {selected_country}의 MBTI 분포")
    country_chart = alt.Chart(country_mbti).mark_bar().encode(
        x=alt.X('MBTI', sort='-y'),
        y='Percentage',
        color='MBTI'
    ).properties(width=800, height=400)
    st.altair_chart(country_chart, use_container_width=True)
