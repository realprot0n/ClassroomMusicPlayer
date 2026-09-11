# ClassroomMusicPlayer
Three step process for letting students submit songs for a classroom- submission, downloading, and playback. (quite unifinished right now but trust)

## Benifits Over Other Options
* No ads
* No internet needed after downloads finish
  * Can play videos blocked by school policy (if you download videos at home)
* No need to remember whomst submitted a video

# Setup
1. Clone this repository to your device.
2. Download Python 3.14 (NOTE: developed on 3.14 testing needed to check for backwards compatability)
3. Download yt-dlp, PySide6, and pygame using pip (run `py -m pip install yt-dlp`)
  * If you get any other errors mentioning missing libaries, also install those using pip.
4. Download ffmpeg from the [ffmpeg website](https://ffmpeg.org/download.html) and extract its contents.
5. Add ffmpeg to your computer's PATH variables
  * For windows:
    1. Search up "path" in the windows search bar, and click on "Edit the system environment variables" (See the [FAQ](#faq) if you can't access this.)
    2. Look for "Path" in either user or system variables
    3. Click "Edit..."
    4. Click "New" and paste the path to where the ffmpeg binaries are located (e.g, `C:\Users\<USER>\Downloads\ffmpeg-2026-08-23...\bin`)
    5. Save the changes you made.
6. Create a google form, with the exact same questions as [this example.](https://docs.google.com/forms/d/e/1FAIpQLSepe10z8sHp2lL1tmqGwM8B74-fqPeuWPgTwiIyHas1ccnp4g/viewform)
7. Link the google form to google sheets.
  * You can change other parameters of the google form if you want (e.g. only allow one submission per email), but the questions must stay the same.

# How to Use
1. Give the google form link to your students (or whoever you want to add links to the playlist)
2. Save a .csv file from the form and place it in the `src` foler (TEMPORARY)

# FAQ
* "My school/admins won't let us have admin permission on our computers, so I can't set the ffmpeg executables in my compter's PATH"
  * Place copies of the three executables from your ffmpeg download in the `ffmpeg_binaries` folder.