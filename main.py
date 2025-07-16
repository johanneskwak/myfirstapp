import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="MBTI 직업 추천기",
    page_icon="🎈",
    layout="centered"
)

# 타이틀과 설명
st.title("🌸 MBTI 기반 직업 추천기")
st.markdown("""
귀엽고 깔끔하게!  
당신의 MBTI에 딱 맞을 것 같은 직업 3개를 추천해 드려요. ✨
""")

# MBTI 목록
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# 각 MBTI에 맞는 추천 직업
job_recommendations = {
    "INTJ": ["데이터 과학자", "전략 컨설턴트", "R&D 엔지니어"],
    "INTP": ["연구원", "시스템 분석가", "이론 물리학자"],
    "ENTJ": ["CEO", "프로젝트 매니저", "경영 컨설턴트"],
    "ENTP": ["벤처 창업가", "마케팅 기획자", "크리에이티브 디렉터"],
    "INFJ": ["상담가", "작가", "인권 변호사"],
    "INFP": ["시인", "일러스트레이터", "사회복지사"],
    "ENFJ": ["HR 매니저", "교사", "공익 홍보 전문가"],
    "ENFP": ["방송 작가", "콘텐츠 크리에이터", "여행 기획자"],
    "ISTJ": ["회계사", "데이터 관리자", "법률 보조원"],
    "ISFJ": ["간호사", "초등교사", "사서"],
    "ESTJ": ["행정 관리자", "프로젝트 매니저", "운영 관리자"],
    "ESFJ": ["고객 서비스 매니저", "이벤트 플래너", "HR 코디네이터"],
    "ISTP": ["기계 엔지니어", "파일럿", "응급 구조원"],
    "ISFP": ["플로리스트", "그래픽 디자이너", "패션 디자이너"],
    "ESTP": ["영업 관리자", "스포츠 코치", "모험 가이드"],
    "ESFP": ["배우", "가수", "행사 기획자"]
}

# 사용자 입력
selected_mbti = st.selectbox("🌱 당신의 MBTI를 선택하세요:", mbti_types)

# 버튼을 눌러 결과 보기
if st.button("추천 직업 보기! 💡"):
    recommended_jobs = job_recommendations.get(selected_mbti, [])
    st.subheader(f"✨ {selected_mbti}에게 추천하는 직업:")
    for job in recommended_jobs:
        st.write(f"- {job}")

# 푸터
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
