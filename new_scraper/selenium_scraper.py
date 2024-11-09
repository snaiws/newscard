import os
import json

from .core.get_driver import get_driver
from .parser.parser1 import get_headlines_naver_it
from .parser.parser2 import get_news_naver



def get_news(now):
    # Chrome WebDriver 설정
    driver = get_driver()
    target_url = os.getenv("URL_NAVER_NEWS_IT")
    headlines = get_headlines_naver_it(driver, target_url)
    news = []
    for headline in headlines:
        result = get_news_naver(driver, headline)
        news.append(result)
    data = {
        "contents":news,
        "updated_at":now
    }
    # JSON 파일로 저장
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    driver.quit()
    print("크롤링 완료, data.json에 저장되었습니다.")
    return data


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    get_news()
