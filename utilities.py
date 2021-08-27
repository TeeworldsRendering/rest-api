import json

def read_json(path: str) -> list:
    f = open(path, "r")
    data = json.load(f)
    f.close() 
    return data