import openai
# OpenAI 라이브러리 버전 0.28로 다운그레이드하여 이전 API 방식으로 코드를 실행
# pip install openai==0.28

# OpenAI API 키 일단 직접 입력
openai.api_key = ""  # API 키 입력 필요

def get_gpt_response(prompt):
 
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # 사용 모델
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": prompt}],
            max_tokens=50
            
        )
        
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error: {e}")
        return None
