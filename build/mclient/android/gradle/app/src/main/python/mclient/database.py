import sqlite3
import os
class Database:
    def __init__(self,db_name='app.db') -> None:
                # 获取应用的内部存储路径
        db_path = os.path.join(os.path.expanduser('~'), db_name)
        
        # 创建数据库连接
        self.connection = sqlite3.connect(db_path)
        #self.connection=sqlite3.connect(db_name)
        self.create_table()
    
    def create_table(self):
        with self.connection:
            self.connection.execute('''
                                    CREATE TABLE IF NOT EXISTS settings(
                                        id INTEGER PRIMARY KEY,
                                        option1 BOOLEAN
                                    )
                                    
                                    ''')
    
    def insert_settings(self,option1):
        with self.connection:
            self.connection.execute('''
                                    INSERT INTO settings(option1) VALUES(?)
                                    ''',(option1,))
    
    def fetch_settings(self):
        cursor=self.connection.cursor()
        cursor.execute('SELECT * FROM settings')
        return cursor.fetchall()
    def fetch_latest_version(self):
        pass
    
    def update_settings(self):
        pass
    
    def close(self):
        self.connection.close()