import os
import openai
import streamlit as st

# Load your API key from an environment variable or secret management service
openai.api_key = "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"

message = """
초기 자산을 확인합니다.
- 일반 회원: 0 포인트
- vip 회원: 100 포인트

위의 내용으로 일반 회원과 vip 회원의 초기 포인트를 설정해줘 
"""

messages=[{"role": "system", "content": message }]

point_message="""
상품의 포인트를 확인합니다. 
- 치마, 드레스, 청바지, 면바지, 반바지, 티셔츠, 블라우스, 바람막이 : 10 포인트가 추가됩니다
- 비타민, 사과, 당근, 바나나, 과일, 메론, 돼지고기, 브로콜리 : 5 포인트가 추가됩니다

위의 내용을 바탕으로 회원의 포인트를 계산해줘 
"""
point_input = {"role": "system", "content": point_message}
messages.append(point_input)


def ask(q):
    q = {"role" : "user" , "content" : q}
    messages.append(q)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages = messages,
        temperature=0.7,
        )

    res = response.to_dict_recursive()
    bot_text  = response['choices'][0]['message']['content']
    bot_input = {"role": "assistant", "content": bot_text }

    messages.append(bot_input)

    return bot_text

while True:
    user_input = input("프롬프트 입력: ")
    bot_resp = ask(user_input)
    print(f"응답결과: {bot_resp}")
    print("-"*30)
