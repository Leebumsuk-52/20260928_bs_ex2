import streamlit as st
import random
import time
import pandas as pd

# ==========================================
# 1. 페이지 기본 설정 및 커스텀 CSS
# ==========================================
st.set_page_config(
    page_title="BS를 소개합니다 | 전설의 시작",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 애니메이션 상태창 감성을 살리는 커스텀 스타일
st.markdown("""
<style>
    .main-title {
        font-size: 3.2rem;
        font-weight: 900;
        background: linear-gradient(90deg, #ff4b4b, #ff914d, #ffd700);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    .sub-title {
        font-size: 1.3rem;
        color: #a0aab4;
        font-style: italic;
        margin-bottom: 25px;
    }
    .quote-box {
        padding: 20px;
        border-left: 6px solid #ff4b4b;
        background-color: rgba(255, 75, 75, 0.08);
        border-radius: 0 12px 12px 0;
        font-size: 1.15rem;
        font-weight: 600;
        margin: 15px 0;
    }
    .timeline-card {
        padding: 16px 20px;
        border-left: 4px solid #4d94ff;
        background-color: rgba(77, 148, 255, 0.07);
        border-radius: 8px;
        margin-bottom: 14px;
    }
    .badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        background: linear-gradient(45deg, #ff4b4b, #ff8000);
        color: white;
        font-weight: bold;
        font-size: 0.85rem;
        margin-right: 6px;
        margin-bottom: 6px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. 사이드바: 세계관 & 사진 설정 컨트롤러
# ==========================================
with st.sidebar:
    st.header("⚙️ BS 세계관 컨트롤러")
    st.write("원하는 애니메이션 세계관과 프로필 사진을 선택해 보세요!")

    anime_theme = st.selectbox(
        "🌌 애니메이션 주인공 모드 선택",
        [
            "🤞 주술회전 모드 (현세대 최강의 특급 주술사)",
            "🗡️ 귀멸의 칼날 모드 (전집중 야근의 호흡 '염주')",
            "⚔️ 진격의 거인 모드 (인류 최강의 병사 리바이 BS)"
        ]
    )

    st.divider()
    st.subheader("📸 주인공 프로필 사진 설정")
    photo_choice = st.radio(
        "드라마 남주인공 프리셋",
        [
            "미즈카미 코시 (오카다 켄시) - 《첫사랑 일기》 남주",
            "사토 타케루 - 《First Love 하츠코이》 남주",
            "직접 이미지 URL 입력"
        ]
    )

    if photo_choice == "미즈카미 코시 (오카다 켄시) - 《첫사랑 일기》 남주":
        # 위키미디어 공용에 등록된 미즈카미 코시(오카다 켄시) 사진 직링크
        profile_img_url = "https://commons.wikimedia.org/wiki/Special:FilePath/%22TOKYO_BURST%22_Japan_Premiere_%E6%B0%B4%E4%B8%8A%E6%81%92%E5%8F%B8.png"
        photo_caption = "《첫사랑 일기(中学聖日記)》 아키라 역 - 미즈카미 코시(오카다 켄시) 모드"
    elif photo_choice == "사토 타케루 - 《First Love 하츠코이》 남주":
        # 위키미디어 공용에 등록된 사토 타케루 사진 직링크
        profile_img_url = "https://commons.wikimedia.org/wiki/Special:FilePath/Satoh_Takeru_in_2019.jpg"
        photo_caption = "《First Love 하츠코이》 하루미치 역 - 사토 타케루 모드"
    else:
        profile_img_url = st.text_input(
            "원하는 사진의 웹 URL을 붙여넣으세요:",
            value="https://commons.wikimedia.org/wiki/Special:FilePath/%22TOKYO_BURST%22_Japan_Premiere_%E6%B0%B4%E4%B8%8A%E6%81%92%E5%8F%B8.png"
        )
        photo_caption = "커스텀 남주인공 아바타 모드"

    st.divider()
    st.subheader("🎵 BGM 분위기 설정")
    bgm_mood = st.select_slider(
        "현재 페이지의 브금 텐션",
        options=["잔잔한 첫사랑 피아노", "각성 직전 빌드업", "최종 결전 오케스트라", "오프닝 하이라이트 폭발"],
        value="최종 결전 오케스트라"
    )
    st.caption(f"현재 재생 중인 심상 BGM: **{bgm_mood}** 🎧")

# 세계관별 텍스트 데이터 매핑
if "주술회전" in anime_theme:
    hero_title = "특급 주술사 · 육안(六眼)과 무하한의 계승자"
    signature_quote = "「천상천하 유아독존(天上天下 唯我獨尊). 걱정 마, 어차피 내가 '최강'이니까.」"
    ult_skill = "🤞 영역 전개: 무량공처 (無量空處)"
    ult_msg = "무량공처가 발동되었습니다! 방문자의 뇌에 BS의 무한한 매력 정보가 0.2초 만에 흘러들어갑니다!"
elif "귀멸의 칼날" in anime_theme:
    hero_title = "귀살대 최고위 검사 · 정열의 염주(炎柱)"
    signature_quote = "「마음을 불태워라! 한계를 넘어선 그곳에 나, BS가 서 있다!」"
    ult_skill = "🔥 제9형: 연옥 (煉獄) - 전집중 상시 발동"
    ult_msg = "화염의 호흡 제9형 발동! 주변의 모든 슬럼프와 피로가 순식간에 불타 사라집니다!"
else:
    hero_title = "조사병단 특별작전반 병장 · 인류 최강의 전력"
    signature_quote = "「후회 없는 선택을 해라. 나를 믿든, 네 자신의 선택을 믿든 결과는 내가 증명한다.」"
    ult_skill = "⚔️ 초고속 입체기동 베기"
    ult_msg = "섬광 같은 입체기동 발동! 눈앞의 모든 과제와 시련을 단 1초 만에 썰어버렸습니다!"

# ==========================================
# 3. 메인 헤더 & 히어로 섹션 (인적사항)
# ==========================================
st.markdown('<p class="main-title">⚡ BS를 소개합니다</p>', unsafe_allow_html=True)
st.markdown(f'<p class="sub-title">― 아련한 첫사랑의 비주얼과 세계관 최강자의 전투력을 동시에 지닌 20대 청년 ―</p>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1.8], gap="large")

with col1:
    # 웹 이미지 로드
    st.image(profile_img_url, caption=photo_caption, use_container_width=True)
    
    # 필살기 버튼
    if st.button(f"⚡ 필살기 발동: {ult_skill}", use_container_width=True, type="primary"):
        st.balloons()
        st.toast(ult_msg, icon="🔥")
        st.success(f"**[필살기 적중]** {ult_msg}")

with col2:
    st.subheader("📜 【 기밀 인물 도감 : 코드네임 B.S 】")
    st.markdown(f'<div class="quote-box">{signature_quote}</div>', unsafe_allow_html=True)

    # 스펙 배지
    st.markdown("""
    <div>
        <span class="badge">SSR+ 등급</span>
        <span class="badge">세계관 최강자</span>
        <span class="badge">첫사랑 비주얼</span>
        <span class="badge">주인공 보정 MAX</span>
    </div>
    """, unsafe_allow_html=True)
    st.write("")

    # 기본 인적사항 (웅장한 만화 주인공 묘사)
    info_col1, info_col2 = st.columns(2)
    with info_col1:
        st.markdown("- **본명 / 코드네임**: **BS** (Beyond the Star)")
        st.markdown("- **나이**: **25세** (2001년 푸른 붉은 달이 뜨던 밤 출생)")
        st.markdown("- **신장 / 체중**: 184cm / 74kg (실전 압축 근육)")
        st.markdown("- **소속**: 지구 방위 및 미지의 영역 개척 본부 (특무대장)")
    with info_col2:
        st.markdown(f"- **클래스**: {hero_title}")
        st.markdown("- **혈액형 / MBTI**: Rh- 왕가의 피 / **ENTJ** (전장을 지휘하는 통솔자)")
        st.markdown("- **주 무기**: 봉인된 흑염룡의 오른손 & 눈빛 하나로 서사를 만드는 아우라")
        st.markdown("- **약점**: 비 오는 날 편의점 우산 씌워주기 (첫사랑 일기 패시브 발동)")

    st.info(
        "💡 **외형 및 기질 묘사**: 평소에는 봄바람이 불어오는 창가 자리에서 아련한 눈빛으로 창밖을 바라보는 "
        "일본 청춘 드라마 남주인공의 모습을 하고 있으나, 동료나 자신의 목표가 위협받는 순간 눈동자의 안광이 "
        "깨어나며 반경 5km의 대기를 진동시키는 압도적인 패기(覇氣)를 방출한다."
    )

st.divider()

# ==========================================
# 4. 핵심 요약 메트릭 (전투력 측정기)
# ==========================================
st.subheader("📊 스카우터 측정 실시간 스탯 ( 측정 불가 경고 🚨 )")
m1, m2, m3, m4 = st.columns(4)
m1.metric(label="⚔️ 종합 전투력", value="999,999+", delta="스카우터 폭발")
m2.metric(label="💘 첫사랑 서사력", value="MAX (100%)", delta="+아련함 한도초과")
m3.metric(label="🔥 위기 돌파력 (주인공 보정)", value="SS+ 등급", delta="절체절명일 때 3배 상승")
m4.metric(label="☕ 카페인 흡수 효율", value="초월적", delta="아이스 아메리카노 연성")

st.divider()

# ==========================================
# 5. 탭(Tabs)으로 구성한 상세 스토리 & 재미 요소
# ==========================================
tab1, tab2, tab3, tab4 = st.tabs([
    "📖 태어나고 자란 전설의 연혁",
    "⚡ 육각형 능력치 & 보유 스킬",
    "🎲 BS와의 동료 궁합 테스트",
    "📝 동료 모집 & 방명록"
])

# --- 탭 1: 연혁 ---
with tab1:
    st.subheader("🌌 BS 연대기 : 신화가 시작된 20여 년의 기록")
    st.write("평범한 인간의 궤적을 거부하고 매 순간 클라이맥스를 써 내려간 BS의 성장 서사입니다.")

    timelines = [
        ("제 1장 : 서막 (2001년 · 0세) — 『별이 떨어지던 밤의 강림』",
         "태풍과 벚꽃이 동시에 휘몰아치던 기이한 봄날 밤, 병원 상공에 일곱 줄기의 무지개와 푸른 번개가 교차하며 탄생했다. "
         "울음소리 대신 나지막한 미소로 산부인과 의사들의 경외심을 불러일으키며 '선택받은 아이'로 기록되었다."),
        ("제 2장 : 각성 (2008년 · 7세) — 『놀이터의 지배자, 비범한 유년기』",
         "만 6세에 동네 골목대장들을 눈빛 하나로 평정하고 평화 조약을 체결했다. "
         "모래성 쌓기 대회에서 중력을 거스르는 고대 바벨탑 구조물을 설계하여 유치원 교사들에게 충격을 안겼다."),
        ("제 3장 : 질풍노도 (2017년 · 16세) — 『첫사랑 일기와 봉인된 힘』",
         "학교 옥상과 도서관 창가 자리를 독점하던 전설의 고교 시절. 운동장을 가로지르기만 해도 복도 창문에 수많은 인파가 몰려들었다. "
         "비가 쏟아지던 여름날, 우산 없이 서 있던 누군가에게 무심하게 우산을 건네고 빗속으로 걸어간 일화는 지금까지도 학교의 7대 전설로 내려온다."),
        ("제 4장 : 시련과 초월 (2021년 · 20세) — 『성인의 문턱, 한계를 부수다』",
         "20대에 접어들며 세계 곳곳의 거대한 프로젝트와 고난에 정면으로 맞섰다. "
         "모두가 불가능이라 말하던 절체절명의 마감 5분 전, '각성 상태(Zone)'에 돌입하여 기적 같은 결과물을 연성해 내며 학계와 업계에 이름을 각인시켰다."),
        ("제 5장 : 현재 (2026년 · 25세) — 『새로운 시대의 정점을 향하여』",
         "20대 중반에 이르러 마침내 지략과 행동력, 그리고 낭만이 완벽한 조화를 이루었다. "
         "이제 자신의 세계관을 깃허브(GitHub)와 디지털 공간으로 확장하며, 함께 세상을 뒤흔들 진정한 동료들을 모으고 있다.")
    ]

    for title, desc in timelines:
        st.markdown(f"""
        <div class="timeline-card">
            <h4 style="margin-top:0; color:#ff6b6b;">{title}</h4>
            <p style="margin-bottom:0;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

# --- 탭 2: 능력치 & 보유 스킬 ---
with tab2:
    st.subheader("⚡ 세부 패러미터 & 고유 스킬 트리")
    stat_col1, stat_col2 = st.columns([1.2, 1])

    with stat_col1:
        st.markdown("##### 📈 6대 핵심 능력치")
        st.write("**지략 및 문제 해결력 (Intelligence)**")
        st.progress(98)
        st.write("**행동력 및 추진력 (Agility & Action)**")
        st.progress(95)
        st.write("**청춘 드라마 서사력 (Romance Aura)**")
        st.progress(100)
        st.write("**동료애 및 리더십 (Charisma)**")
        st.progress(96)
        st.write("**절체절명 주인공 보정 (Plot Armor)**")
        st.progress(100)

    with stat_col2:
        st.markdown("##### 🃏 패시브 & 액티브 스킬")
        with st.expander("🌟 [패시브] 주인공 전용 브금 자동 재생", expanded=True):
            st.write("위기 상황에 처하거나 중요한 발표를 시작할 때, 어디선가 웅장한 오케스트라 OST가 흘러나오며 성공 확률이 200% 상승합니다.")
        with st.expander("☔ [패시브] 첫사랑 기억 조작"):
            st.write("흰 셔츠를 입거나 비 오는 날 창밖을 바라보면 주변 사람들의 기억 속에 '학창 시절 아련한 첫사랑'으로 자동 저장됩니다.")
        with st.expander("⚡ [액티브] 마감 1시간 전의 기적 (초집중)"):
            st.write("남은 시간이 1시간 미만일 때 시간의 흐름을 1/10로 느리게 인지하며, 평소의 5배 속도로 과업을 완수합니다.")

# --- 탭 3: 동료 궁합 테스트 (재미 요소) ---
with tab3:
    st.subheader("🎲 당신은 BS의 파티에 합류할 수 있을까? (동료 적합도 진단)")
    st.write("간단한 질문 3개로 주인공 **BS**와 당신의 세계관 시너지를 측정해 보세요!")

    visitor_name = st.text_input("당신의 이름(또는 코드네임)을 입력하세요:", placeholder="예: 불꽃의 동료 K")
    q1 = st.radio(
        "Q1. 절체절명의 위기 상황! 거대한 시련이 눈앞에 나타났을 때 당신의 행동은?",
        ["등 뒤를 BS에게 맡기고 함께 정면 돌파한다!", "냉철하게 적의 약점을 분석해 BS에게 브리핑한다.", "맛있는 간식과 아메리카노를 준비해 후방 지원한다."]
    )
    q2 = st.selectbox(
        "Q2. 당신이 가장 선호하는 모험 시간대는?",
        ["햇살이 부서지는 청량한 오후", "모두가 잠든 고요한 새벽의 각성 시간", "비 내리는 감성적인 저녁"]
    )
    q3 = st.slider("Q3. BS의 웅장한 세계관에 대한 당신의 몰입도는?", 0, 100, 90)

    if st.button("🔍 동료 적합도 결과 확인하기"):
        if not visitor_name:
            visitor_name = "이름 없는 모험가"
        
        with st.spinner("세계관의 인과율을 계산하는 중입니다..."):
            time.sleep(0.8)
        
        score = min(100, int(q3 * 0.4 + random.randint(55, 65)))
        
        if "정면 돌파" in q1:
            role = "🔥 최전선 쌍벽의 파트너 (부대장 포지션)"
        elif "약점을 분석" in q1:
            role = "🧠 천재 참모 & 전략가 (브레인 포지션)"
        else:
            role = "💎 파티의 정신적 지주 & 치유사 (서포터 포지션)"

        st.success(f"🎉 **{visitor_name}** 님과 **BS**의 동료 시너지 지수는 **{score}%** 입니다!")
        st.info(f"**추천 포지션**: {role}\n\n**BS의 한마디**: *\"흥미롭군, {visitor_name}. 내 등 뒤를 맡길 자격이 충분해 보인다. 함께 가자.\"*")

# --- 탭 4: 방명록 & 명언 생성기 ---
with tab4:
    st.subheader("📝 동료 모집 신청서 & 오늘의 주인공 대사")

    col_g1, col_g2 = st.columns([1, 1.3])

    with col_g1:
        st.markdown("##### 🎙️ BS의 랜덤 명대사 자판기")
        quotes = [
            "「포기하는 순간, 내 사전의 페이지는 넘어가지 않는다.」",
            "「첫사랑이 아름다운 건 이루어지지 않아서가 아니라, 그때의 내가 진심이었기 때문이다.」",
            "「길이 없다면 내가 걸어간 발자국이 곧 길이 될 것이다.」",
            "「내 한계를 정하는 건 세상이 아니라, 오직 나 자신뿐이다.」",
            "「오늘의 커피 한 잔이 내일의 세계를 구한다.」"
        ]
        if st.button("🎲 새로운 명대사 뽑기"):
            st.markdown(f'<div class="quote-box">{random.choice(quotes)}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="quote-box">{quotes[0]}</div>', unsafe_allow_html=True)

    with col_g2:
        st.markdown("##### 💬 BS에게 한마디 남기기 (방명록)")
        if "guestbook" not in st.session_state:
            st.session_state.guestbook = [
                {"작성자": "고죠 사토루", "메시지": "BS, 역시 너도 최강이구나! 다음에 디저트 먹으러 가자고."},
                {"작성자": "쿠로이와 아키라", "메시지": "첫사랑 일기 감성 그대로네요. 응원합니다!"}
            ]

        with st.form("guestbook_form", clear_on_submit=True):
            g_name = st.text_input("닉네임", placeholder="방문자 이름")
            g_msg = st.text_input("응원 메시지", placeholder="BS에게 남길 말을 적어주세요!")
            submitted = st.form_submit_button("방명록 등록")
            if submitted and g_name and g_msg:
                st.session_state.guestbook.insert(0, {"작성자": g_name, "메시지": g_msg})
                st.toast("방명록이 성공적으로 등록되었습니다!", icon="✅")

        for item in st.session_state.guestbook:
            st.markdown(f"- **{item['작성자']}**: {item['메시지']}")

st.divider()
st.caption("© 2026 Created by BS | Powered by Streamlit & Protagonist Aura ⚡")