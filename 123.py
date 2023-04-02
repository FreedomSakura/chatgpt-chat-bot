import openai
import json
# from __future__ import unicode_literals
# print json.dumps(odata,ensure_ascii=False)

openai.api_key = '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'

f = open('123.txt', 'a')
 
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
          {
            "role": "system",
            "content": "You are a good assistant and will respond well to the user's needs, \
              and then translate them into Chinese and tell the user."
          },
          {
            "role": "user",
            "content": "Can you tell me what an apple is?"
          },
          {
            "role": "assistant",
            "content": "Yes, apple is a fruit that is red, fragrant, and sweet. It grows mostly in temperate regions and is widely loved by people./n \
              Chinese: 苹果是一种水果，红色，很香，很甜，多生长在温带地区，广受人们喜爱。"
          },
          {
            "role": "user",
            "content": "Very good! this is it! How good are you!"
          },

          {
            "role": "user", 
             "content": "Now, can you tell me about lovecraft and his Cthulhu world?"
          }
  ]
)

print("返回结果：", completion)

message_1 = json.dumps(completion.choices[0].message.content,  ensure_ascii=False)
role = json.dumps(completion.choices[0].message.role,  ensure_ascii=False)

message_arr = message_1.split('\\n')
for item in message_arr:
    print(item)
    # f.write('\n')
    # f.write(item)
# print(message_arr)


# completion2 = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#             {
#               "role": "system",
#               "content": "you are a good "
#             },
#             {"role": "user", 
#              "content": "Ok, thank you!"
#             #  "content": "Tell the world about the ChatGPT API in the style of a pirate."

#              }]
# )

# print(completion2)
# message_2 = json.dumps(completion2.choices[0].message.content,  ensure_ascii=False)
# role_2 = json.dumps(completion2.choices[0].message.role,  ensure_ascii=False)

# message_arr2 = message_2.split('\\n')
# for item in message_arr2:
#     print(item)
