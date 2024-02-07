from flask import Flask, request, Response
from werkzeug.utils import secure_filename
import os
from moviepy.editor import VideoFileClip, AudioFileClip

app = Flask(__name__)

app.config['UPLOAD_FOLDER_AUDIO'] = 'storage/audio'
app.config['UPLOAD_FOLDER_VIDEO'] = 'storage/video'
ALLOWED_AUDIO_EXTS = ['mp3', 'wav', 'wma', 'aac', 'flac', 'm4a']
ALLOWED_VIDEO_EXTS = ['mp4', 'mov', 'avi', 'wmv', 'flv']


def allowed_file(filename, allowed_exts):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_exts


# upload the file
@app.route('/upload', methods=["POST"])
def upload():
    uploaded_file_audio = request.files.get('audio')
    uploaded_file_video = request.files.get('video')

    if uploaded_file_audio is not None:
        if allowed_file(uploaded_file_audio.filename, ALLOWED_AUDIO_EXTS):
            uploaded_file_audio.save(
                os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER_AUDIO'],
                             secure_filename(uploaded_file_audio.filename)))
            return 'Audio file uploaded successfully'

    if uploaded_file_video is not None:
        if allowed_file(uploaded_file_video.filename, ALLOWED_VIDEO_EXTS):
            uploaded_file_video.save(
                os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER_VIDEO'],
                             secure_filename(uploaded_file_video.filename)))
            return 'Video file uploaded successfully'

    else:
        return {'error': 'File upload failed, or invalid file type'}


# Download the video file
@app.route('/download/<filename>', methods=['GET'])
def download(filename):
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER_AUDIO'], filename)

    def generate():
        with open(file_path, 'rb') as f:
            data = f.read()
            yield data

    response = Response(generate())
    response.headers['Content-Type'] = 'audio/mpeg'
    return response


# Modify the video into .mp3 type
@app.route('/modify_video_type/<filename>', methods=['POST'])
def modify_video_type(filename):
    upload_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER_VIDEO'], filename)
    base_filename, ext = os.path.splitext(filename)
    mp4_filename = base_filename + ".mp4"
    mp4_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER_VIDEO'], mp4_filename)
    clip = VideoFileClip(upload_path)
    clip.write_videofile(mp4_path, fps=60)
    return "Video converted to MP4"


# Modify the video into .mp3 type
@app.route('/modify_audio_type/<filename>', methods=['POST'])
def modify_audio_type(filename):
    upload_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER_AUDIO'], filename)
    base_filename, ext = os.path.splitext(filename)
    mp3_filename = base_filename + ".mp3"
    mp3_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER_AUDIO'], mp3_filename)
    clip = AudioFileClip(upload_path)
    clip.write_audiofile(mp3_path)
    return "Audio converted to MP4"


# Extract audio from video
@app.route('/extract_audio_video/<filename>', methods=['POST'])
def extract_audio_video(filename):
    upload_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER_VIDEO'], filename)
    base_filename, ext = os.path.splitext(filename)
    output_name = base_filename + "_extracted_audio.mp3"
    output_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER_AUDIO'],
                               output_name)
    VideoFileClip(upload_path).audio.write_audiofile(output_path)
    return "Audio split from video stream "


# Modify the video without audio
@app.route('/modify_video_noaudio/<filename>', methods=['POST'])
def modify_video_noaudio(filename):
    upload_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER_VIDEO'], filename)
    base_filename, ext = os.path.splitext(filename)
    output_name = base_filename + "_noaudio.mp4"
    output_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER_VIDEO'],
                               output_name)
    clip = VideoFileClip(upload_path)
    no_audio_clip = clip.without_audio()
    no_audio_clip.write_videofile(output_path, fps=60)
    return "Video split into video stream without audio"


# Trim the video
@app.route('/clip_video_trim/<filename>', methods=['POST'])
def clip_video_trim(filename):
    # Get start and end trim times
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')
    upload_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER_VIDEO'], filename)
    base_filename, ext = os.path.splitext(filename)
    output_name = f"{base_filename}_trimmed.mp4"
    output_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER_VIDEO'],
                               output_name)
    clip = VideoFileClip(upload_path)
    duration = clip.duration
    if start_time:
        start_time = int(start_time)
    else:
        start_time = 0
    if end_time:
        end_time = int(end_time)
    else:
        end_time = duration
    trimmed = clip.subclip(start_time, end_time)
    trimmed.write_videofile(output_path, fps=60)
    return "Video trimmed successfully"


@app.route('/clip_audio_trim/<filename>', methods=['POST'])
def clip_audio_trim(filename):
    # Get start and end trim times
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')
    upload_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER_AUDIO'], filename)
    base_filename, ext = os.path.splitext(filename)
    output_name = f"{base_filename}_trimmed.mp3"
    output_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER_AUDIO'],
                               output_name)
    clip = AudioFileClip(upload_path)
    duration = clip.duration
    if start_time: 
        start_time = int(start_time)
    else:
        start_time = 0

    if end_time: 
        end_time = duration - int(end_time)
    else:
        end_time = duration
    trimmed = clip.subclip(start_time, end_time)
    trimmed.write_audiofile(output_path)
    return "Audio trimmed successfully"


@app.route('/combine_video_audio/<video_file>/<audio_file>', methods=['POST'])
def combine_video_audio(video_file, audio_file):
    video_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER_VIDEO'], video_file)
    audio_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER_AUDIO'], audio_file)
    output_name = 'combined_video.mp4'
    output_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER_VIDEO'],
                               output_name)
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)

    if audio_clip.duration > video_clip.duration:   # Case 1: Audio longer
        audio_clip = audio_clip.subclip(0, video_clip.duration)

    elif video_clip.duration > audio_clip.duration:     # Case 2: Video longer
        video_clip = video_clip.subclip(0, audio_clip.duration)

    else:  # Case 3: Equal lengths, combine as is
        pass

    final_clip = video_clip.set_audio(audio_clip)
    final_clip.write_videofile(output_path, fps=60)
    return "Audio and Video merged successfully"


if __name__ == '__main__':
    app.run(debug=True)
