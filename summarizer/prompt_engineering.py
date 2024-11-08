import json
import os
import re
from LLM import get_gpt_response

#주어진 뉴스를 요약하는 프롬프트, GPT 응답을 반환
def pm_strategy(content):
 
    prompt = f"다음 뉴스 내용 중 가장 핵심 내용을 세 줄로 200자 내로 요약해, 한국어로 요약하고 문장 마무리 제대로:\n{content}"
    gpt_response = get_gpt_response(prompt)
    
    if gpt_response:
        return gpt_response
    else:
        return "요약을 생성할 수 없습니다."


# data.json에서 뉴스를 읽고 pm_strategy 함수로 처리하여 요약 생성
def process_json():

    json_path = os.path.join('..', 'new_scrapper', 'data.json') # 상대 경로로 data.json 불러옴
    
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"{json_path} 파일을 찾을 수 없습니다. 경로를 확인하세요.")
        return
    except json.JSONDecodeError:
        print(f"{json_path} 파일이 올바른 JSON 형식이 아닙니다.")
        return

    for article in data:
        url = article.get("url")
        title = article.get("title")
        date = article.get("date")
        content = article.get("content")

        # 불필요한 부분 제거
        content = re.sub(r'\[사진 출처.*?\]\n*', '', content)
        content = re.sub(r'■ 제보하기.*', '', content)

        summary = pm_strategy(content)

        #출력 형식
        print(f"URL: {url}\nTitle: {title}\nDate: {date}\nSummary: {summary}\n")

if __name__ == "__main__":
    process_json()        
