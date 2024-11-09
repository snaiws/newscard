from selenium.webdriver.common.by import By

def get_news_naver(driver, url):
    # 네이버 뉴스 기사 URL (기사 URL로 직접 접근)
    driver.get(url)
    # time.sleep(1)

    # 제목, 날짜 
    title = driver.find_element(By.CSS_SELECTOR, 'h2.media_end_head_headline').text
    date = driver.find_element(By.CSS_SELECTOR, 'span.media_end_head_info_datestamp_time').text
    
    # article#dic_area 요소에서 전체 텍스트 
    content = driver.find_element(By.CSS_SELECTOR, 'article#dic_area').text

    # 수집한 데이터를 딕셔너리 형태로 저장
    result = {
        "url": url,
        "title": title,
        "date": date,
        "content": content  # 전체 본문 텍스트 저장
    }

    return result
