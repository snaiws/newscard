import re

def process_newscontent(string):
    """
    뉴스 본문 텍스트에서 불필요한 부분을 제거합니다.
    """
    # 불필요한 부분 제거
    string = re.sub(r'\[사진 출처.*?\]\n*', '', string)
    string = re.sub(r'■ 제보하기[\s\S]*', '', string)
    string = re.sub(r'당신의 제보가 뉴스로 만들어집니다[\s\S]*', '', string)

    return string