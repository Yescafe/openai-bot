from pycqBot.cqApi import cqHttpApi, cqLog
import logging
from pycqBot import Message
import secret_tokens
import openai_utils

cqLog(logging.DEBUG)
cqapi = cqHttpApi()

def chat(command_data, msg: Message):
    print(command_data)
    prompt = ' '.join(command_data)
    answer = openai_utils.get_completion(prompt)
    msg.reply(answer)

bot = cqapi.create_bot(
    group_id_list=secret_tokens.GROUP_ID_LIST,
    options = secret_tokens.OPTIONS
)

bot.command(chat, "chat", {
    "help": [
        "#chat - 与 ChatGPT 对话"
    ]
})

bot.start()

