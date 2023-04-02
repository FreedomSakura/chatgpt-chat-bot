```python
import openai
import json

# 设置OpenAI API密钥
openai.api_key = "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"

# 定义一个函数来生成回答
def generate_answer(prompt):
    # 格式化OpenAI API请求参数
    model_engine = "text-davinci-002"
    prompt = f"{prompt.strip()}"

    # 发送OpenAI API请求
    response = openai.Completion.create(
        engine=model_engine, prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.5)

    # 从OpenAI API响应中获取回答
    answer = response.choices[0].text.strip()

    return answer

# 不断循环来获取用户输入并生成回答
while True:
    prompt = input("你：").strip().lower()
    if len(prompt) == 0:
        continue
    if prompt in ['quit', 'exit']:
        break

    # 调用生成回答函数来获取回答
    answer = generate_answer(prompt)

    print("AI：", answer)