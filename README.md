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
