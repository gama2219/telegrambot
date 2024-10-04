from botintergration import send,results
from flask import Flask,request,abort
from databaseconf import save_message,get_chat_history,chat_hist
import telebot



def data_processing(update):
    save_message(user_id=update.message.from_user.id,
                role='user',
                text=update.message.text)
    #chain 
    _=results.delay(update.message.text,
              update.message.chat.id,
              chat_hist(get_chat_history(update.message.from_user.id)))
    try:
        send.delay(update.message.from_user.id,*(_.get()))
        save_message(user_id=update.message.from_user.id,role='model',text=_.get()[1])
    except Exception as e:
        print(e)


app=Flask(__name__)

@app.route('/webhook',methods=['POST'])
def webhook():
    try:
        json_str = request.get_data().decode('UTF-8')
        update = telebot.types.Update.de_json(json_str)
        data_processing(update=update)
    except Exception as e:
        return abort(400)
    else:
        return "succsess"
