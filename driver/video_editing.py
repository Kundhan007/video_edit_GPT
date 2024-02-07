import logging

logging.basicConfig(level=logging.INFO)  # Set the logging level as per your preference


def clip_audio_front(audio_mp3, seconds, front=True):
    if front:
        logging.info(f"Clipping {audio_mp3} from the front for {seconds} seconds.")
    else:
        logging.info(f"Clipping {audio_mp3} from the end for {seconds} seconds.")


def clip_video_front(video_mp4, seconds, front=True):
    if front:
        logging.info(f"Clipping {video_mp4} from the front for {seconds} seconds.")
    else:
        logging.info(f"Clipping {video_mp4} from the end for {seconds} seconds.")


def extract_video(video_mp4):
    logging.info(f"Extracting video from {video_mp4}.")


def combine_video_audio(video_mp4, new_audio):
    logging.info(f"Combining {video_mp4} with new audio.")
