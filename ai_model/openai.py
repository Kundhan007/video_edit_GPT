import requests
from util import read_config
import json

cred_config = read_config('../cred.json')

url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer "+cred_config['open_ai']['api_key']  # Replace with your actual API key
}

user_prompt = '''
user statement: Here is Video foo.mp4. Here is new Audio stream. Clip Video first 3 seconds off video and clip first 3 seconds from Audio. Of the remaining Video and Audio, combine them to form a new Video
functions available= [trim_audio(audio, seconds, front), trim_video(video, seconds, front), combine_audio_video(audio, video), divide_audio_video(video)]
initial_variables=
{
    video: video_var,
    audio: audio_var
}
considerations: 
start the function with initial variables
if necessary, give output of one function to other create variables
give function calls in json also include output variable in json for each function
output json should have 3 parts: function name, input parameters, output variable name
return expectation:
list of function calls that will satisfy the user statement

'''
data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": user_prompt}],
    "temperature": 0.7
}

content = requests.post(url, json=data, headers=headers).json()["choices"][0]["message"]["content"]
formatted_result = json.dumps(json.loads(content), indent=2)
print(formatted_result)

