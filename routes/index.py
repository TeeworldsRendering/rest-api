from app import app

def __formatHelp(url_map: object) -> str:
    ret: list = []
    for rule in url_map.iter_rules():
        ret += [f"{rule.endpoint} {', '.join(rule.methods)} {rule}"]
    return f"<pre>{chr(10).join(ret)}</pre>"

def getHelpFormat(url_map: object):
    return f"<h2>Teeworlds Render API help</h2>\n\n{__formatHelp(url_map)}"

@app.route("/")
def index():
    return getHelpFormat(app.url_map)