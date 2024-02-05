from flask import Flask, send_file
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
from moviepy.editor import VideoFileClip, AudioFileClip


app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER_AUDIO'] = 'storage/audio'
app.config['UPLOAD_FOLDER_VIDEO'] = 'storage/video'

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route('/', methods=['GET',"POST"])
# upload the file
@app.route('/upload', methods=['GET',"POST"])
def upload():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # First grab the file
        ext = os.path.splitext(file.filename)[1].lower()
        if ext in ['.mp3', '.wav', '.wma', '.aac', '.flac','.m4a']:
            file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER_AUDIO'],secure_filename(file.filename))) # Then save the file
        if ext in ['.mp4', '.mov', '.avi', '.wmv', '.flv']:
            file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER_VIDEO'],secure_filename(file.filename))) # Then save the file
        return '200'


# Download the audio file
@app.route('/download_audio', methods=['GET'])
def download_audio():
    folder = app.config['UPLOAD_FOLDER_AUDIO']
    for root, dirs, files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root, file)
    return send_file(full_path, as_attachment=True)

# Download the video file
@app.route('/download_video', methods=['GET'])
def download_video():
    folder = app.config['UPLOAD_FOLDER_VIDEO']
    for root, dirs, files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root, file)
    return send_file(full_path, as_attachment=True)



# <------------------------>
from flask import Flask, render_template, send_file
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
import io
import zipfile
from wtforms.validators import InputRequired
from moviepy.editor import VideoFileClip, AudioFileClip
from pydub import AudioSegment
import pydub as psb


app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER_AUDIO'] = 'storage/audio'
app.config['UPLOAD_FOLDER_VIDEO'] = 'storage/video'

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route('/', methods=['GET',"POST"])
# upload the file 
@app.route('/upload', methods=['GET',"POST"])
def upload():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # First grab the file
        ext = os.path.splitext(file.filename)[1].lower()
        if ext in ['.mp3', '.wav', '.wma', '.aac', '.flac','.m4a']:
            file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER_AUDIO'],secure_filename(file.filename))) # Then save the file
        if ext in ['.mp4', '.mov', '.avi', '.wmv', '.flv']:
            file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER_VIDEO'],secure_filename(file.filename))) # Then save the file
        return "File has been uploaded."
    return render_template('index.html', form=form)

# Download the audio file 
@app.route('/download_audio', methods=['GET',"POST"])
def download_audio():    
    folder = app.config['UPLOAD_FOLDER_AUDIO']
    for root, dirs, files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root, file)
    return send_file(full_path, as_attachment=True)

# Download the video file 
@app.route('/download_video', methods=['GET',"POST"])
def download_video():    
    folder = app.config['UPLOAD_FOLDER_VIDEO']
    for root, dirs, files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root, file)
    return send_file(full_path, as_attachment=True)





# Input: Audio file  -> Output: Cliped Audio file   
def clip_audio(audio_file, start_trim, end_trim):
    clip = AudioFileClip(audio_file).subclip(start_trim,end_trim)
    clip.write_audiofile(audio_file.replace(os.path.split(audio_file)[-1], 'clip_audio.mp3'),fps=60)
    return 

# Working
# Input : Any Audio Type -> Output: Audio with .mp3 Type
def audio_convert(audio_file):
    clip = AudioFileClip(audio_file)
    clip.write_audiofile(audio_file.replace(os.path.splitext(audio_file)[1], '.wav'))
    return 

# Working
# Input: Video with Audio  -> Output : Audio
def extract_audio(video_file):
    VideoFileClip(video_file).audio.write_audiofile(video_file.replace(os.path.split(video_file)[-1], 'extract_audio.mp3'))
    return 




# Working
# Input: Video, Audio file -> Output: Video file with audio merged
def combine_video_audio(audio_file, video_file):
    audio = AudioFileClip(audio_file)
    video = VideoFileClip(video_file)
    final_video = video.set_audio(audio)
    final_video.write_audiofile(video_file.replace(os.path.split(video_file)[-1], 'final_video.mp3'),fps=60)
    return 

# Working
# Input: Any Video Type -> Output: Video with .mp4 Type
def video_convert(video_file):
    clip = VideoFileClip(video_file) 
    clip.write_videofile(video_file.replace(os.path.splitext(video_file)[1], '.mp4'),fps=60)
    return 

# Working
# Input: Video with Audio  -> Output : Video without Audio
def extract_video(video_file):
    clip = VideoFileClip(video_file).without_audio()
    clip.write_videofile(video_file.replace(os.path.split(video_file)[-1], 'without_audio.mp4'),fps=60)
    return 

# Working 
# Input: Video file  -> Output: Cliped Video file     
def clip_video(video_file, start_trim, end_trim):
    clip = VideoFileClip(video_file).subclip(start_trim,end_trim)
    clip.write_videofile(video_file.replace(os.path.split(video_file)[-1], 'clip_video.mp4'),fps=60)
    return 


if __name__ == '__main__':
    # video_convert(Sample_1)
    # extract_video(Sample_1)
    # clip_video(Sample_1,10,20)
    # extract_audio("C:/Users/sridi/OneDrive/Documents/Python_Scripts/Sample_1.mp4")
    # audio_convert("C:/Users/sridi/OneDrive/Documents/Python_Scripts/audio.mp3")
     clip_audio("C:/Users/sridi/OneDrive/Documents/Python_Scripts/audio.mp3",10,20)
    # combine_video_audio(Sample_1)

