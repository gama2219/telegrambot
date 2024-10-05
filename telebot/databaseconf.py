import sqlite3


#database initialization
def init_db():
    with sqlite3.connect('chat_history.db') as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS chat_history (
                user_id INTEGER,
                role TEXT,
                text TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()


def save_message(user_id, role, text):
        with sqlite3.connect('chat_history.db') as conn:
            c = conn.cursor()
            c.execute('''
                INSERT INTO chat_history (user_id, role, text) VALUES (?, ?, ?)
            ''', (user_id, role, text))
            conn.commit()

def get_chat_history(user_id):
        with sqlite3.connect('chat_history.db') as conn:
            c = conn.cursor()
            c.execute('''
                SELECT role, text FROM chat_history WHERE user_id = ? ORDER BY timestamp ASC
            ''', (user_id,))
            rows = c.fetchall()
            return rows
def chat_hist(history):
    history_payload = [{"role": role[0], "parts": role[1]} for role in history]
    return history_payload