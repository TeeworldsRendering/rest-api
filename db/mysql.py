import mysql.connector, json, time
from utilities import *

ENV: json = read_json("json/env.json")

class SQLCursor(object):
    def __init__(self) -> None:
        self.conn: object = mysql.connector.connect(
                    host = ENV["host"],
                    user = ENV["user"],
                    passwd = ENV["pass"],
                    database = ENV["database"])
        self.cursor: object = self.conn.cursor(buffered=True, dictionary=True)
    
    def reconnect(self, wait: float = 1.5) -> None:
        if self.conn.is_connected() == False:
            self.conn.reconnect(attempts = 1, delay = 0)
            time.sleep(wait)
        self.conn.commit()
    
    def execute(self, req: str) -> None:
        self.reconnect()
        self.cursor.execute(req)

class SQLRequests(SQLCursor):
    def __init__(self) -> None:
        super().__init__()
    
    def everything(self) -> list:
        self.execute("""SELECT * FROM skin""")
        return (self.cursor.fetchall())
    
    def byGuildId(self, _id: str) -> list:
        self.execute(f"""SELECT * FROM skin WHERE guild_id={_id} ORDER BY filename ASC""")
        return (self.cursor.fetchall())

    def lastUploads(self, n: int = 5) -> list:
        self.execute(f"""SELECT * FROM skin ORDER BY created_at ASC LIMIT {n}""")
        return (self.cursor.fetchall())

    def onlyFilenameByGuildId(self, _id: str) -> list:
        self.execute(f"""SELECT filename FROM skin WHERE guild_id={_id} ORDER BY filename ASC""")
        return (self.cursor.fetchall())

    def insertSkin(self, attr: dict) -> None:
        try:
            self.execute(f"""INSERT INTO skin (guild_id, 
            user_id, filename, md5_checksum) VALUES 
            ({attr['guild_id']}, {attr['user_id']}, 
            '{attr['filename']}', '{attr['md5_checksum']}')""")
            self.conn.commit()
        except:
            pass
    
    def removeSkin(self, attr: dict) -> None:
        self.execute(f"""DELETE FROM skin WHERE guild_id={attr['guild_id']} AND
        filename='{attr['filename']}'""")
        self.conn.commit()