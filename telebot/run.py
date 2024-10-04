import flask_
import databaseconf
import os


"""make sure the redis server is running:
    and youve filled your bot token and gemini api key
    in the setting.py file before running this file
"""
def main():
    databaseconf.init_db()
    #start workers
    flask_.app.run(host='0.0.0.0',port=5000)
if __name__=='__main__':
    main()







