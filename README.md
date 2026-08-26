# ClassroomMusicPlayer
Three step process for letting students submit songs for a classroom- submission, downloading, and playback.

# Setup
1. Clone this repository to your device.
2. Download ffmpeg from the [ffmpeg website](https://ffmpeg.org/download.html) and extract its contents.
3. Add ffmpeg to your computer's PATH variables
    * For windows:
        1. Search up "path" in the windows search bar, and click on "Edit the system environment variables" (See the [FAQ](#faq) if you can't access this.)
        2. Look for "Path" in either user or system variables
        3. Click "Edit..."
        4. Click "New" and paste the path to where the ffmpeg binaries are located (e.g, `C:\Users\<USER>\Downloads\ffmpeg-2026-08-23...\bin`)
        5. Save the changes you made.
4. Create a google form, with the same questions as [this example.](https://docs.google.com/forms/d/e/1FAIpQLSepe10z8sHp2lL1tmqGwM8B74-fqPeuWPgTwiIyHas1ccnp4g/viewform)
5. Link the google form to google sheets.

# FAQ
* "My school/admins won't let us have admin permission on our computers, so I can't set the ffmpeg executables in my compter's PATH"
  * Place copies of the three executables from your ffmpeg download in the `ffmpeg_binaries` folder.