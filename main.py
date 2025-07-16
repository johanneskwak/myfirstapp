import streamlit as st
st.title('커리어 컨설팅 서비스 만들기')
st.write('안녕하세요, 당신의 커리어를 진단해주는 서비스입니다')
name = st.text_input('이름을 입력해주세요 : ')
menu = st.selectbox('좋아하는 음식을 선택해주세요:', ['망고빙수','아몬드봉봉'])
if st.button('인사말 생성') : 
  st.write(name+'님! 당신이 좋아하는 음식은 '+menu+'이군요?! 저도 좋아요!!')
