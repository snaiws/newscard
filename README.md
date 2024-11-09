# newscard
**개요**

뉴스 요약 페이지

**기능**

- 네이버 뉴스 IT 페이지 헤드라인 수집
    - 윈도우 실행 시 수집
    - 배포된 Streamlit 페이지의 경우 데이터 수집 없이 테스트 데이터로 요약
- 전처리 및 프롬프트 엔지니어링 후 openai API 사용하여 뉴스 요약(api key 입력 필요)
- Streamlit UI

**테스트**

- Windows
    
    ```
    
    pip install -r requirements.txt
    
    streamlit run main.py
    
    ```
    
- Streamlit
    
    https://newscard.streamlit.app/