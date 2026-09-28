import streamlit as st
import random

# 1. 페이지 기본 설정 (가볍고 빠른 렌더링)
st.set_page_config(page_title="BS를 소개합니다", page_icon="😎", layout="centered")

# 2. 타이틀 & 컨셉 스위치
st.title("😎 BS를 소개합니다")
st.caption("※ 주의: 이 페이지는 다량의 '주인공 보정'과 '자아도취'가 포함되어 있습니다. (반박 시 님 말이 맞음)")

# 다 같이 웃을 수 있는 '만화 설정 vs 현실' 토글 스위치
reality_mode = st.toggle("🔍 진실의 안경 쓰기 (만화 설정 OFF / 현실 모드 ON)", value=False)

st.divider()

# 3. 메인 프로필 섹션
col1, col2 = st.columns([1, 1.4], gap="medium")

with col1:
    # 드라마 《첫사랑 일기(中学聖日記)》 남주인공 미즈카미 코시(오카다 켄시) 웹 이미지
    img_url = "https://commons.wikimedia.org/wiki/Special:FilePath/%22TOKYO_BURST%22_Japan_Premiere_%E6%B0%B4%E4%B8%8A%E6%81%92%E5%8F%B8.png"
    st.image(img_url, caption="뇌내망상 이미지: 드라마 《첫사랑 일기》 남주인공", use_container_width=True)

with col2:
    if not reality_mode:
        st.subheader("🌸 [만화 설정] 청춘 로맨스 남주 BS")
        st.markdown("""
        - **이름**: **BS** (청춘 만화 세계관 최강자)
        - **나이**: **25세** (꽃미남 전성기)
        - **포지션**: 《너에게 닿기를》 카제하야 한국 지부장
        - **특기**: 비 오는 날 우산 씌워주기, 창가 자리에서 아련하게 밖 쳐다보기
        - **성격**: 겉은 차가운 도시 남자 같지만 내 사람에겐 따뜻한 츤데레
        """)
        st.info("💬 **대표 대사**: \"어? 우산 없어? 마침 하나 더 있는데… 그냥 주는 거니까 오해하지 마.\"")
    else:
        st.subheader("🤣 [현실 모드] 인간미 넘치는 BS")
        st.markdown("""
        - **이름**: **BS** (친근함 세계관 최강자)
        - **나이**: **20대 중반** (마음만은 늘 스무 살)
        - **포지션**: 모임 분위기 메이커 & 맛집 레이더
        - **특기**: 비 오는 날 내 우산 챙기기도 바쁨, 창가 자리에서 메뉴판 정독하기
        - **성격**: 커피와 맛있는 음식 사주면 누구보다 다정해짐
        """)
        st.warning("💬 **현실 대사**: \"비 오는데 무슨 감성이야, 파전에 막걸리나 먹으러 뛰자!\"")

# 4. 한눈에 보는 스탯 (유머 버전)
st.divider()
m1, m2, m3 = st.columns(3)
if not reality_mode:
    m1.metric("✨ 첫인상 비주얼", "만찢남", "만화책 찢고 나옴")
    m2.metric("☕ 하루 커피 수혈량", "아아 3잔", "+센스 만점")
    m3.metric("🎓 학창 시절 인기", "교복 단추 완판", "자칭 전설")
else:
    m1.metric("✨ 첫인상 비주얼", "만찢남", "만화책만 찢음", delta_color="inverse")
    m2.metric("☕ 하루 커피 수혈량", "생명수", "카페인 없으면 방전")
    m3.metric("🎓 학창 시절 인기", "급식실 1등", "달리기 최강자")

st.divider()

# 5. 탭 구성: 연혁 / 능력치 / 미니게임 & 방명록
tab1, tab2, tab3 = st.tabs(["📜 태어나고 자란 연혁", "📊 육각형 능력치", "🎲 랜덤 뽑기 & 방명록"])

# --- 탭 1: 유쾌한 연혁 ---
with tab1:
    st.subheader("🎬 BS의 파란만장 20대 연대기")
    st.markdown("""
    * **🌅 1장. 탄생 (2000년대 초)** : 범상치 않은 울음소리와 함께 등장. 동네 어르신들의 귀여움을 독차지하며 골목대장으로 성장.
    * **🚲 2장. 질풍노도의 학창 시절 (10대)** : 본인은 도서관 창가 자리의 첫사랑 남주인공이었다고 주장하나, 목격자들에 의하면 매점 소보로빵을 가장 빨리 쟁취하던 열혈 소년.
    * **🔥 3장. 청춘의 캠퍼스 & 질주 (20대 초)** : 과제 마감 1시간 전에 초인적인 집중력을 발휘하는 '벼락치기 각성 능력'을 터득함.
    * **🌟 4장. 현재 (20대 중반)** : 외모는(마음속으로) 첫사랑 드라마 남주, 일할 때는 프로페셔널, 놀 때는 누구보다 진심인 완성형 캐릭터로 진화 중!
    """)

# --- 탭 2: 육각형 능력치 ---
with tab2:
    st.subheader("📊 BS의 핵심 능력치 분석")
    st.write("😎 **자신감 & 뻔뻔함 (만화 주인공 보정)**")
    st.progress(100)
    st.write("🤝 **의리 & 친화력 (사람 챙기기)**")
    st.progress(95)
    st.write("⚡ **마감 직전 추진력 (초집중 모드)**")
    st.progress(92)
    st.write("🍜 **맛집 타율 & 메뉴 선정 센스**")
    st.progress(98)

# --- 탭 3: 다 같이 해보는 재미 요소 ---
with tab3:
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("##### 🎯 오늘 BS에게 쏘면 좋은 메뉴는?")
        menus = [
            "☕ 시원한 아이스 아메리카노!",
            "🍕 치즈 듬뿍 피자 & 맥주!",
            "🥩 지글지글 삼겹살!",
            "🍰 당 충전용 달달한 디저트!",
            "🍜 얼큰한 국물 요리!"
        ]
        if st.button("🎰 랜덤 메뉴 뽑기", use_container_width=True):
            st.balloons()
            st.success(f"당첨! 오늘 BS에게 **{random.choice(menus)}** 사주시면 평생 은인으로 모십니다.")

    with col_b:
        st.markdown("##### 💬 한 줄 팩트체크 & 응원 방명록")
        if "comments" not in st.session_state:
            st.session_state.comments = [
                "익명1: 사진이랑 본인 싱크로율 해명 좀 해주세요 ㅋㅋㅋ",
                "익명2: 그래도 의리 하나는 인정합니다! 파이팅!"
            ]
        
        new_comment = st.text_input("이름과 한마디 입력 (예: 홍길동 - 페이지 잘 만들었다!)", placeholder="내용 입력 후 엔터")
        if st.button("등록하기", use_container_width=True) and new_comment:
            st.session_state.comments.insert(0, new_comment)

        for c in st.session_state.comments[:5]:
            st.caption(f"🗨️ {c}")

st.divider()
st.caption("© 2026 BS Profile Page | 웃자고 만든 페이지에 죽자고 달려들기 없기 😎")