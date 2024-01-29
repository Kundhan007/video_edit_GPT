OpenAI GPT App model:
 
Imagine Acme Video Service that has a RestAPI interface:
Here is simplified Pseudo code for exercise purposes here (in reality it is actually described as RestAPI)
1. Initial load of Video (in .mp4 format)
Int handle openVideo(String videoname)
   
2. Clip front of rear of Video
bool status  clip_video(int handle, int seconds_from_front_of_video = 0, int seconds_from _end_of_video=0)
Non 0 seconds indicate no of seconds of Video to clip (front or back)
 
3. load of Audio
int handle  openAudio(string audio)
 
   
4. Clip from front or rear of Audio
bool status  clip_audio(int handle, int seconds_from_front_of_audio = 0, int seconds_from _end_of_audio=0)
Non 0 seconds indicate no of seconds of Audio to clip (front or back)
 
5. Replace Video’s audio stream with new Audio
bool status replace_audio(int video_handle, int audio_handle, url &new_video_file)
 
The pseudo code merely provides a conceptual example. Actual API will change as idea develops further.
 
2. The goal for OpenAI to be able to access   Acme’s Video service as needed. Acme’s Video service runs on a Web server with well defined APIs ) no different from say Youtube API or other APIs from other Web services). Note there is authentication invoved
  The use case is this from User which prompts OpenAI GPT:
     “Here is Video foo.mp4. Here is new Audio stream. Clip Video first 3 seconds off video and clip first 3 seconds from Audio. Of the remaining Video and Audio, combine them to form a new Video”
 
3. Further Requirements
 -  Secure and Protect User intellectual property. Ie, anything that is trained to GPT should be unique and available to only customers of Acme.
- API that GPT learns is retained. Ie not learned from scratch for each session. All of Acme’s API is already learned by GPT
- Acme API has transitive concept. Ie step produces a result that then goes thru another API to alter the contents ad infinitum. The final output is a new Video file that has gone thru these multiple transitive steps, This is not shown in Pseudo code example
- Acme API must be expressed as RestAPI
 
Output of this exercise:
- Explain concept wise how to achieve this on GPT V4.0 (that’s the latest at of this writing)
- Show design in schematic form
- Approach is attainable in GPT, not just theory. Substantiate against other similar real examples
 
- Provide prototype is plus
- Hints:
o Need to learn GPT basic API and do some hands training if you are not familiar already.
Do not just expouse concepts with no baseline experience in GPT APIs.
o Use GPT V4 paid account to be relevant to latest GPT (GPT4 as of this writing)
o Read GPT documentation and other avenues to learn what GPT has to offer (function calls, GPTs etc). Note this list grows on each release. However, just use whatever is available in latest release (GPT4 as of this writing).
o To achieve the goal, may need to use all features of GPT – OpenAI API, Function Calling, Custom Calls etc. Thus, it is important to first understand holistically what GPT has to offer in terms of App development.
o Possible use of Hugging Face, further LLM training etc to achieve goal
         
 