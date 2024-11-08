from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json
import time
#pip install selenium
#pip install webdriver-manager
def get_news():
    # Chrome WebDriver 설정
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    # 네이버 뉴스 기사 URL (기사 URL로 직접 접근)
    url = "https://n.news.naver.com/mnews/article/008/0005111756" ###### 뉴스 링크 ########
    driver.get(url)

    # 데이터 저장을 위한 리스트 초기화
    news = []

    try:
        # 제목, 날짜 
        title = driver.find_element(By.CSS_SELECTOR, 'h2.media_end_head_headline').text
        date = driver.find_element(By.CSS_SELECTOR, 'span.media_end_head_info_datestamp_time').text
        
        # article#dic_area 요소에서 전체 텍스트 
        content = driver.find_element(By.CSS_SELECTOR, 'article#dic_area').text

        # 수집한 데이터를 딕셔너리 형태로 저장
        news.append({
            "url": url,
            "title": title,
            "date": date,
            "content": content  # 전체 본문 텍스트 저장
        })

    except Exception as e:
        print(f"Error occurred: {e}")

    # JSON 파일로 저장
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(news, f, ensure_ascii=False, indent=4)

    driver.quit()
    print("크롤링 완료, data.json에 저장되었습니다.")

if __name__ == "__main__":
    get_news()
