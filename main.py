import json
import traceback
import datetime

import streamlit as st
from streamlit_autorefresh import st_autorefresh

from utils.now import korean_now
from new_scraper.selenium_scraper import get_news
from data_process.preprocess import process_newscontent
from summarizer.LLM import check_openai_api_key, get_gpt_response
from summarizer.prompt_engineering import pm_strategy



@st.dialog("KEY를 입력해주세요")
def input_key():
    key = st.text_input("KEY : ")
    if st.button("Submit"):
        # 키 검증
        if check_openai_api_key(key):
            st.session_state.input_key = {"key": key}
            st.session_state.invalid=False
        else:
            st.session_state.invalid=True
        st.rerun()


def main():
    # 타이틀
    try:
        st.title('News card')
    except:
        error_message = traceback.format_exc()
        print(error_message)
        raise error_message
    # 키
    key = ""
    try:
        if "invalid" in st.session_state:
            if st.session_state.invalid:
                st.warning("유효한 키를 입력해주세요")
        if "input_key" not in st.session_state:
            if st.button("key 입력"):
                input_key()
                if "input_key" in st.session_state:
                    key = st.session_state.input_key['key']
        else:
            key = st.session_state.input_key['key']
    except:
        error_message = traceback.format_exc()
        print(error_message)
    
    # 키 입력 대기
    if not key:
        st.caption(f"키 입력 필요")
        return


    # 데이터 불러오기
    data = {
        "contents":[],
        "updated_at":""
    }
    try:
        with st.spinner("뉴스를 불러오는 중입니다..."):
            with open('data.json', 'r', encoding="utf-8") as f:
                data = json.load(f)

    except:
        error_message = traceback.format_exc()
        print(error_message)
        st.caption(f"데이터 불러오기 오류")


    # 데이터 수집
    try:
        last_updated = data['updated_at']
        now = korean_now('%Y-%m-%d %H:%M:%S')
        datetime_prior = datetime.datetime.strptime(data['updated_at'], "%Y-%m-%d %H:%M:%S")
        datetime_now = datetime.datetime.strptime(now, "%Y-%m-%d %H:%M:%S")
        if datetime_now - datetime_prior > datetime.timedelta(minutes=10):
        # refresh시 json 저장이 유지되는지 확인 필요
            with st.spinner("뉴스를 수집 중입니다..."):
                data = get_news(last_updated)
            last_updated = now
        else:
            last_updated = data['updated_at']
    except:
        error_message = traceback.format_exc()
        print(error_message)
        st.caption(f"데이터 수집 오류")

    # 시간 표시
    try:
        st.caption(f"**last updated:** {last_updated}")
    except:
        error_message = traceback.format_exc()
        print(error_message)
        st.caption(f"시간 표시 오류")

    news_raw = data['contents']
    for new in news_raw:
        with st.spinner("뉴스를 처리 중입니다..."):
            try:
                news_contents = new['content']
                # 데이터 처리
                news_processed = process_newscontent(news_contents)
            except:
                error_message = traceback.format_exc()
                print(error_message)
                st.success(f"데이터 처리 오류")
                continue

        with st.spinner("프롬프트 만드는 중입니다..."):
            try:
                prompt = pm_strategy(news_processed)
            except:
                error_message = traceback.format_exc()
                print(error_message)
                st.success(f"프롬프트 처리 오류")
                continue
        # 문서 요약
        with st.spinner("뉴스를 요약 중입니다..."):
            try:
                new_summary = get_gpt_response(key,prompt)
            except:
                error_message = traceback.format_exc()
                print(error_message)
                st.success(f"뉴스 요약 오류")
                continue
        try:
            # view
            with st.container(border=True):
                st.markdown(f"##### {new['title']} #####")
                st.write(new_summary)
                st.write(f"**날짜**: {new['date']}")
                st.link_button("기사로 이동", new["url"])
        except:
            error_message = traceback.format_exc()
            print(error_message)
            st.caption("뉴스 표시 오류")
    return



if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()

    st_autorefresh(interval=60*1000*11, key="dataframerefresh")
    main()