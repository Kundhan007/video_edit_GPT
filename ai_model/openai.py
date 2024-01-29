from util import read_config
import requests

config = read_config()
cred_config = read_config('cred.json')


def prepare_payload(user_prompt: str):
    data = config["payload"]
    data["messages"][0]["content"] = user_prompt
    return data


def prompt_to_json(user_prompt: str):
    url = config['open_ai_url']
    api_key = cred_config['api_key']
    headers = config['headers']
    data = prepare_payload(user_prompt)
    response = requests.post(url=url, headers=headers, auth=("", api_key), json=data)

    if response.status_code == '200':
        result = response.json
    else:
        print(f"Error: {response.status_code} - {response.text}")
