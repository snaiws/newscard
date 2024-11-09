#주어진 뉴스를 요약하는 프롬프트, GPT 응답을 반환
def pm_strategy(content):
 
    prompt = f"다음 뉴스 내용 중 가장 핵심 내용을 세 줄로 200자 내로 요약해, 한국어로 요약하고 문장 마무리 제대로:\n{content}"
    gpt_response = prompt
    
    return gpt_response
 
