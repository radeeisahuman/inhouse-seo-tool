import json

def change_credentials(username: str, password: str):
    json_object = json.dumps({
        "name" : username,
        "password": password
    }, indent=4)

    with open("credentials.json", "w") as file:
        file.write(json_object)

def get_credentials():
    with open("credentials.json", "r") as file:
        data = json.load(file)

    return data