import os

app.config['UPLOAD_FOLDER_AUDIO'] = 'files_storage/audio'
app.config['UPLOAD_FOLDER_VIDEO'] = 'files_storage/video'


def clip_video_front(video_mp4, seconds, front=True):
    file_name = video_mp4.split[0]
    video = VideoFileClip(video_mp4) 
    if front == True:
        trimmed = video.subclip(int(seconds))
    else:
        trimmed = video.subclip(int(seconds), int(video.duration - seconds))
    new_file = os.path.join(app.config['UPLOAD_FOLDER_VIDEO'],"Trimmed_"+file_name+".mp4")
    trimmed.write_videofile(new_file,fps=60)  
    pass


def extract_video(video_mp4):
    file_name = os.path.splitext(video_mp4)[0]
    clip = VideoFileClip(video_mp4).without_audio()
    new_file_no_audio = os.path.join(app.config['UPLOAD_FOLDER_VIDEO'],file_name + ".mp4")
    new_clip = clip.write_videofile(new_file_no_audio, fps =60)
    pass

def combine_video_audio(video_mp4, new_audio):
    pass


# <---Existing Functionality--->


# Split the audio from the video file
@app.route('/modify_video_audio', methods=['GET',"POST"])
def modify_video_audio():
    folder = app.config['UPLOAD_FOLDER_VIDEO']
    for file in os.listdir(folder):
        full_path = os.path.join(folder, file)
        file_name = os.path.splitext(file)[0]
        clip = VideoFileClip(full_path).without_audio()
        new_file = os.path.join(folder,file_name + ".mp4")
        new_clip = clip.write_videofile(new_file, fps =60)
    return "Video without audio modified"

# Trim the video getting the start and end time 
@app.route('/clip_video_trim', methods=['GET',"POST"])
def clip_video_trim(): 
    start_trim = request.form['start_trim']
    end_trim = request.form['end_trim']
    folder = app.config['UPLOAD_FOLDER_VIDEO']
    print(folder)
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.spilt[1] == '.mp4':
                full_path = os.path.join(root, file)
                video = VideoFileClip(full_path) 
                trimmed = video.subclip(int(start_trim), int(video.duration - end_trim))
                new_file = os.path.join(folder,"Trimmed_"+file_name+".mp4")
                trimmed.write_videofile(new_file,fps=60)     
                return "Video trimmed"
            else:
                return "No mp4 file found" 