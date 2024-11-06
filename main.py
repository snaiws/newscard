import streamlit as st
from streamlit_autorefresh import st_autorefresh

from utils.now import korean_now


st_autorefresh(interval=60*1000, key="dataframerefresh")

def main():
    st.title('News card')
    last_updated = korean_now('%Y-%m-%d %H:%M:%S')
    st.caption(f"**lastly updated:** {last_updated}")


    # # 데이터 수집
    # with st.spinner("뉴스를 수집 중입니다..."):
    #     news_raw = get_news()
    # st.success("데이터 수집 완료!")

    # # 데이터 처리
    # with st.spinner("뉴스를 처리 중입니다..."):
    #     news_processed = process_news(news_raw)
    # st.success("데이터 처리 완료!")

    # # 문서 요약
    # with st.spinner("뉴스를 요약 중입니다..."):
    #     for new in news_processed:
    #         new_summary = summary(news_processed)

    #     # view


    #     st.success("뉴스 요약 완료!")
    return



if __name__ == "__main__":
    main()