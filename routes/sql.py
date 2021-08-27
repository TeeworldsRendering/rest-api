from app import app
from db.mysql import SQLRequests
from flask import request

sql: SQLRequests  =  SQLRequests()

@app.route("/skin/all", methods = ["GET"])
def selectAll():
    return (str(sql.everything()))

@app.route("/skin/guild/<int:guild_id>", methods = ["GET"])
def selectByGuildId(guild_id: int = 0):
    return (str(sql.byGuildId(guild_id)).replace("'", "\""))

@app.route("/skin/filenames/<int:guild_id>", methods = ["GET"])
def selectOnlyFilenameByGuildId(guild_id: int = 0):
    return (str(sql.onlyFilenameByGuildId(guild_id)).replace("'", "\""))

@app.route("/skin/last/<int:count>", methods = ["GET"])
def selectLastUploaded(count: int = 5):
    return (str(sql.lastUploads(count)))

@app.route("/skin/upload", methods = ["POST"])
def insertSkin():
    sql.insertSkin(request.args.to_dict())
    return ":^)"

@app.route("/skin/delete", methods = ["DELETE"])
def deleteSkin():
    sql.removeSkin(request.args.to_dict())
    return ":^)"