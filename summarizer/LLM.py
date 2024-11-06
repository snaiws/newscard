


def openai_api(key, string):
    """
    API 호출 함수
    key는 streamlit에서 입력받도록(github에 안올라가게 하기 위함)
    입력 : api key
    출력 : GPT 응답
    """
    return string



if __name__ == "__main__":
    key = input("key:\n")
    openai_api(key)