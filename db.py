import sqlite3

class DB:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS job_description (
            jdid TEXT PRIMARY KEY,
            jd TEXT
        )
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS resume (
            cvid TEXT PRIMARY KEY,
            cv TEXT
        )
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS conversation (
            convid TEXT,
            msgid TEXT PRIMARY KEY,
            content TEXT
        )
        ''')
        self.conn.commit()


    def set_jd(self, jd_id, jd):
        self.cursor.execute("INSERT INTO job_description (jdid, jd) VALUES (?, ?)", (jd_id, jd))
        self.conn.commit()

    def set_cv(self, cv_id, cv):
        self.cursor.execute("INSERT INTO resume (cvid, cv) VALUES (?, ?)", (cv_id, cv))
        self.conn.commit()

    def set_msg(self, conv_id, msg_id, content):
        self.cursor.execute("INSERT INTO conversation (convid, msgid, content) VALUES (?, ?, ?)", (conv_id, msg_id, content))
        self.conn.commit()

    def get_data(self, jd_id, cv_id, conv_id):
        self.cursor.execute('SELECT jd FROM job_description WHERE jdid = ?', (jd_id, ))
        jd_data = self.cursor.fetchone()

        self.cursor.execute("SELECT cv FROM resume WHERE cvid = ?", (cv_id,))
        cv_data = self.cursor.fetchone()

        self.cursor.execute("SELECT content FROM conversation WHERE convid = ?", (conv_id,))
        conv_data = self.cursor.fetchall()

        # Format the data
        result = {
            jd_id: jd_data,
            cv_id: cv_data,
            conv_id: [item[0] for item in conv_data]  
        }

        return result

    def get_conversation(self, conv_id):
        self.cursor.execute("SELECT content FROM conversation WHERE convid = ?", (conv_id,))
        conv_data = self.cursor.fetchall()
        return conv_data

    def get_cv(self, cv_id ):
        self.cursor.execute("SELECT cv FROM resume WHERE cvid = ?", (cv_id,))
        cv_data = self.cursor.fetchone()
        return cv_data

    def get_jd(self, jd_id):
        self.cursor.execute('SELECT jd FROM job_description WHERE jdid = ?', (jd_id, ))
        jd_data = self.cursor.fetchone()
        return jd_data



