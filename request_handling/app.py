from flask import render_template, send_file
import os


app.config['UPLOAD_FOLDER_AUDIO'] = 'files_storage/audio'
app.config['UPLOAD_FOLDER_VIDEO'] = 'files_storage/video'


def video_audio_upload(request_files):
    video = request_files.video
    audio = request_files.audio
    prompt = request_files.prompt
    pass

def download_video_audio(file): 
    return send_file(file, as_attachment=True)




# <---Existing Functionality--->

@app.route('/download_audio', methods=['GET',"POST"])
def download_audio(audio_id): # file -> audio_id
    folder = app.config['UPLOAD_FOLDER_VIDEO']
    for root, dirs, files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root, file)
    return send_file(full_path, as_attachment=True)


@app.route('/download_video', methods=['GET',"POST"])
def download_video(video_id): # file -> video_id
    folder = app.config['UPLOAD_FOLDER_VIDEO']
    for root, dirs, files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root, file)
    return send_file(full_path, as_attachment=True)


