from util import read_config
import requests
import json

config = read_config()
cred_config = read_config('../cred.json')


def prepare_payload(user_prompt: str):
    data = config["payload"]
    data["messages"][0]["content"] = user_prompt
    return data


def prompt_to_json(user_prompt: str):
    url = config['open_ai_url']
    api_key = cred_config['open_ai']['api_key']
    headers = config['headers']
    data = prepare_payload(user_prompt)
    response = requests.post(url=url, headers=headers, auth=("", api_key), json=data)

    if response.status_code == 200:
        result = response.json()
        formatted_result = json.dumps(result, indent=2)
        print(formatted_result)
    else:
        print(f"Error: {response.status_code} - {response.json}")


user = "Here is Video foo.mp4. Here is new Audio stream. Clip Video first 3 seconds off video and clip first 3 seconds from Audio. Of the remaining Video and Audio, combine them to form a new Video"
prompt_to_json(user)

