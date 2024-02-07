# video_edit_GPT
user prompt for editing the video is taken and converted to defined set of functions which are implemented on the own server


# objective statement:
Here is Video foo.mp4. Here is new Audio stream. Clip Video first 3 seconds off video and clip first 3 seconds from Audio. Of the remaining Video and Audio, combine them to form a new Video

iteration 1: 
    - objective statement
    - happy flow only

# driver function:
    - def clip_video(video_mp4, seconds, front = True)
        - return clipped video
        - front or back will depend on the flag front
    - def extract_video(video_mp4)
        - return video component of the video audio is removed
    - def combine_video_audio(video_mp4, new_audio)
        - return combined video and audio

# request handling functions:
    - def video_audio_upload():
        - post request that will take the video
        - post request that will take the audio
    - def download_video:
        - get call with video id(mostly session)

# todo
    - open ai function handling and testing
    - connecting to the real functions
    - implementing driver functions (nitin functions)
    - testing with video, audio input
    - postman testing for downloading the output file


# Sequence Diagram :
![WhatsApp Image 2024-01-28 at 4 56 38 PM](https://github.com/Kundhan007/video_edit_GPT/assets/27908778/eaeaa785-0ba2-4ab7-a8f7-ad85dcb68cdb)


# sample output from gpt
``` json
[
  { 
    "function_name": "trim_video",
    "input_parameters": {
      "video": "video_var",
      "seconds": 3,
      "front": true
    },
    "output_variable_name": "trimmed_video"
  },
  {
    "function_name": "trim_audio",
    "input_parameters": {
      "audio": "audio_var",
      "seconds": 3,
      "front": true
    },
    "output_variable_name": "trimmed_audio"
  },
  {
    "function_name": "combine_audio_video",
    "input_parameters": {
      "audio": "trimmed_audio",
      "video": "trimmed_video"
    },
    "output_variable_name": "combined_video"
  }
]
```


next commits
mock statments for driver functions
implementing algorithm


input from user:
    - user prompt
    - video and audio files(optional)

user prompt will go to open ai:
    - includes userprompt
    - available functions
    - instructions
    - expected results

this will generate a algorithm in the form of json list of pseudo

this json list will be converted to actual python algorithm code

this python alg will be attached to our driver functions





















