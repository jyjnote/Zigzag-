import streamlit as st 
import time

path = "image/"
st.set_page_config(
    page_title='🌸Zigzag🌸',
    page_icon='🌸Zigzag🌸'
)

md_text = '**🌸리뷰기반 고객 및 입점주을 위한 분석 AI 대쉬보드🌸**'
st.markdown(md_text)

_LOREM_IPSUM = """
지그재그를 기반으로 데이터를 크롤링해와 소비자와 입점주를 위한 BI 도출을 위한 프로젝트입니다. 해당 프로젝트로 소비자는 본인이 원하는 상품을 검색하여 리뷰를 탐색해 최종 구매의사에 도움이 되고, 입점주는 저희가 제공하는 데이터분석을 통해 유동적인 판매전략을 가져질 수 있습니다. 이를 통해 소비자오 생산자의 상호작용을 증대시키 수 있을 것으로 기대됩니다.
"""

def stream_data():
    for word in _LOREM_IPSUM.split():
        yield word + " "
        time.sleep(0.05)

st.header("맴버 소개")

# Toggle button for member introduction
if st.button("맴버 소개"):
    if "show_members" not in st.session_state:
        st.session_state["show_members"] = False

    st.session_state["show_members"] = not st.session_state["show_members"]

# Display member introduction if toggle is on
if st.session_state.get("show_members"):
    image_urls = [
        "미나.jpg",
        "J.jpg",
        "auj.jpg",
        "lsr.jpg",
        "원영.jpg"
    ]

    # Current image index
    current_image_index = st.session_state.get("current_image_index", 0)

    # Display image
    st.image(f'{path}/{image_urls[current_image_index]}', use_column_width=False, width=800)

    # Grouped buttons for navigation
    col1, col2 = st.columns([1, 2])
    with col1:
        if st.button("Previous"):
            current_image_index -= 1
            if current_image_index < 0:
                current_image_index = len(image_urls) - 1

            # Update state
            st.session_state["current_image_index"] = current_image_index

    with col2:
        if st.button("Next"):
            current_image_index += 1
            if current_image_index >= len(image_urls):
                current_image_index = 0

            # Update state
            st.session_state["current_image_index"] = current_image_index

# Button for site introduction
if st.button("사이트 소개"):
    st.write_stream(stream_data)






