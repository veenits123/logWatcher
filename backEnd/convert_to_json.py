import json


def ConvertToJSON(lines):
    dictionary = {index: value for index, value in enumerate(lines)}
    jsonString = json.dumps(dictionary)
    return jsonString
