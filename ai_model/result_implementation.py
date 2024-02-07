from json2functions.transform_functions import algorithm_result
sample_json_response = [
  {
    "function": "trim_video",
    "input": {
      "video": "video_var",
      "seconds": 3,
      "front": 1
    },
    "output": "trimmed_video"
  },
  {
    "function": "trim_audio",
    "input": {
      "audio": "audio_var",
      "seconds": 3,
      "front": 1
    },
    "output": "trimmed_audio"
  },
  {
    "function": "combine_audio_video",
    "input": {
      "audio": "trimmed_audio",
      "video": "trimmed_video"
    },
    "output": "new_video"
  }
]


