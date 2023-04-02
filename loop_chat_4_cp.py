import openai
 
openai.api_key = "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"

# 存储对话的历史
data= [{"role": "user", "content": "你好！"}]

user_content = '你好！'
gpt_content = ''
#把上段对话数据结构化，并提交给下面的ChatGPT
user_prompt = {"role": "user", "content": user_content}
gpt_prompt = {"role": "assistant", "content": gpt_content}

# 新建一个对话
completion = openai.ChatCompletion.create(
                n = 1,  
                user = '1',    
                model = "gpt-3.5-turbo",   
                messages = data
            )

rsp = completion.choices[0].message.content

gpt_prompt = {"role": "assistant", "content": rsp}
data.extend(gpt_prompt)
print("chatgpt:", rsp)

while 1:
    a = input("user：")
    if a == 'break;' :
        print(data)
        break
    user_prompt = {"role": "user", "content": a}


    # completion = openai.ChatCompletion.create(
    #                 max_tokens = inf # 默认inf 最大令牌数
    #                 presence_penalty = 1, # 惩罚机制，-2.0 到 2.0之间，默认0，数值越小提交的重复令牌数越多，从而能更清楚文本意思
    #                 frequency_penalty = 1, # 意义和值基本同上，默认0，主要为频率
    #                 temperature = 1.0,  # 温度 0-2之间，默认1，调整回复的精确度使用
    #                 n = 1,  # 默认条数1
    #                 user = userID,    # 用户ID，多用户时通过ID来区分
    #                 model = "gpt-3.5-turbo",    # openai的模型
    #                 messages = data.extend(q) #将用户当前输入的问题加入到之前的聊天记录里进行提问。
    #             )
    print(data)
    completion1 = openai.ChatCompletion.create(
                    n = 1,  # 默认条数1
                    user = '1',    # 用户ID，多用户时通过ID来区分
                    model = "gpt-3.5-turbo",    # openai的模型
                    messages = data.extend([user_prompt, gpt_prompt]) #将用户当前输入的问题加入到之前的聊天记录里进行提问。
                )
    
    rsp1 = completion1.choices[0].message.content    # chatGPT返回的数据

    gpt_prompt = {"role": "assistant", "content": rsp1}

    print("chatgpt:", rsp1)



