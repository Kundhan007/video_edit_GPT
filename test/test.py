import os
from moviepy.editor import VideoFileClip, AudioFileClip


# <--- Functions  ---->

# Input: Audio file  -> Output: Clipped Audio file
def clip_audio(audio_file, start_trim, end_trim):
    clip = AudioFileClip(audio_file).subclip(t_start=start_trim, t_end=end_trim)
    clip.write_audiofile(audio_file.replace(os.path.split(audio_file)[-1], 'clip_audio.mp3'))
    return


# Input : Any Audio Type -> Output: Audio with .mp3 Type
def audio_convert(audio_file):
    clip = AudioFileClip(audio_file)
    clip.write_audiofile(audio_file.replace(os.path.splitext(audio_file)[1], '.mp3'))
    return


# Input: Video with Audio  -> Output : Audio
def extract_audio(video_file):
    VideoFileClip(video_file).audio.write_audiofile(
        video_file.replace(os.path.split(video_file)[-1], 'extract_audio.mp3'))
    return


# Input: Video, Audio file -> Output: Video file with audio merged
def combine_video_audio(audio_file, video_file):
    audio = AudioFileClip(audio_file)
    video = VideoFileClip(video_file)
    final_video = video.set_audio(audio)
    final_video.write_audiofile(video_file.replace(os.path.split(video_file)[-1], 'final_video.mp3'), fps=60)
    return


# Input: Any Video Type -> Output: Video with .mp4 Type
def video_convert(video_file):
    clip = VideoFileClip(video_file)
    clip.write_videofile(video_file.replace(os.path.splitext(video_file)[1], '.mp4'), fps=60)
    return


# Input: Video with Audio  -> Output : Video without Audio
def extract_video(video_file):
    clip = VideoFileClip(video_file).without_audio()
    clip.write_videofile(video_file.replace(os.path.split(video_file)[-1], 'without_audio.mp4'), fps=60)
    return


# Input: Video file  -> Output: Clipped Video file
def clip_video(video_file, start_trim, end_trim):
    clip = VideoFileClip(video_file).subclip(t_start=start_trim, t_end=end_trim)
    clip.write_videofile(video_file.replace(os.path.split(video_file)[-1], 'clip_video.mp4'), fps=60)
    return


if __name__ == '__main__':
    video_convert('test/sample_files/video/Sample_1.mp4')
    extract_video('test/sample_files/video/Sample_1.mp4')
    clip_video('test/sample_files/video/Sample_1.mp4', 10, 20)
    extract_audio('test/sample_files/video/Sample_1.mp4')
    audio_convert('test/sample_files/audio/Sample_1.m4a')
    clip_audio('test/sample_files/audio/Sample_1.m4a', 10, 20)
    combine_video_audio('test/sample_files/video/Sample_1.mp4')
