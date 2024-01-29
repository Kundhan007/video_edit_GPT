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
    - 