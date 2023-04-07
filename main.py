import os
import openai
import telebot

openai.api_key = "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"
bot = telebot.TeleBot("6093362517:AAHu35tew7qgS67XfZwihcHQUnNKUAoOrTA")

@bot.message_handler(func = lambda _: True)
def handle_message(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.5,
        max_tokens=3000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
    )
    bot.send_message(chat_id=message.from_user.id, text=response["choices"][0]["text"])

bot.polling()

