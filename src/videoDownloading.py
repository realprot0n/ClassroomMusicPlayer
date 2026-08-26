import os
import yt_dlp
import log_manager
import video_storage
import json
from typing import Final
from yt_dlp.postprocessor.ffmpeg import FFmpegExtractAudioPP

download_folder: Final[str] = "video_storage"
thumbnail_folder: Final[str] = "video_storage/thumbnails"

def ensure_folder_exists(path: str) -> bool:
  """Makes sure the folder given at path exists.
  
  If the given path doesn't exist, the path is created, and True
  is returned. If the path does exist, false is returned.

  Parameters
  ----------
  path : str
    The path to the download folder.
  
  Returns
  -------
  bool
    Whether or not a directory at the given path
    had to be created.
  """
  if os.path.exists(path) and os.path.isdir(path):
    log_manager.print_if_debug(
      log_manager.DebugLevel.INFO,
      f"There was already a download folder at {path}."
    )
    return False

  log_manager.print_if_debug(
    log_manager.DebugLevel.WARNINGS,
    f"Had to create a download folder at {path}."
    )
  os.makedirs(path)
  return True

def make_audio_options() -> yt_dlp._Params:
  return {
    "paths":{"home": download_folder},
    "writethumbnail": True,
    "writeinfojson": True,
    "quiet": True
  }

def create_audio_downloader() -> yt_dlp.YoutubeDL:
  downloader: yt_dlp.YoutubeDL = yt_dlp.YoutubeDL(params=make_audio_options())
  downloader.add_post_processor(FFmpegExtractAudioPP(preferredcodec="mp3")) # type: ignore
  downloader.add_progress_hook(save_info_hook)
  return downloader

def save_info_hook(data: dict[str, str]) -> None:
  if data["status"] != "finished":
    return

  file_name: str = data["filename"]
  file_name = ".".join(file_name.split(".")[:-2])
  with open(file_name + ".info.json", "r", encoding="utf8") as file:
    video_storage.add_video_info(
      file_name + ".mp3",
      json.load(file)
    )

def main() -> None:
  ensure_folder_exists(download_folder)
  ensure_folder_exists(thumbnail_folder)

  downloader: yt_dlp.YoutubeDL = create_audio_downloader()
  downloader.download(
    ["https://www.youtube.com/watch?v=cSV4RJ3VBME",
     "https://www.youtube.com/watch?v=h6bb2I-8Pho"]
  )

if __name__ == "__main__":
  main()