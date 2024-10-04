from celery_ import app
import settings
import telebot
import  google.generativeai as genai

#this file handles the intergration between the telegrambot and gemini api
genai.configure(api_key=settings.GEMINI_KEY)
generation_config = {
    "temperature": 2,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
}
model = genai.GenerativeModel(model_name="gemini-1.5-flash",
                              generation_config=generation_config,
                              system_instruction=settings.GEMINI_INSTRUCTIONS)
#bot object
tb = telebot.TeleBot(settings.BOT_API_KEY)
tb.remove_webhook()
tb.set_webhook(url=settings.WEBHOOK)



class Communication:
    def send_response(self,user_id, chat_id, text):
        tb.send_chat_action(str(user_id),"typing")
        tb.send_message(chat_id, text)
    
    def get_answers(self, message, chat_id,history):
        chat_session = model.start_chat(history=history)
        response = chat_session.send_message(message)
        return [chat_id, response.text]
    
    def __repr__(self):
        return 'This is a bot and AI API integration object'
    

obj=Communication()

    
@app.task()
def send(user_id,chat_id,text):
    obj.send_response(user_id,chat_id,text)


@app.task()
def results(message,chat_id,history):
    res=obj.get_answers(message,chat_id,history)
    print(res)
    return res

