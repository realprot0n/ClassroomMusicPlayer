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
  downloader.add_close_hook(end_downloading_hook)
  
  return downloader

def format_json_file(path, json_indent: str = "  ") -> None:
  json_data: dict = {}
  with open(path, "r", encoding="utf8") as file:
    json_data = json.load(file)
  
  with open(path, "w") as file:
    json.dump(json_data, file, indent=json_indent)

def save_info_hook(data: dict[str, str]) -> None:
  if data["status"] != "finished":
    return
  
  file_name: str = os.path.abspath(data["filename"])
  file_name = ".".join(file_name.split(".")[:-2])
  format_json_file(file_name + ".info.json")
  with open(file_name + ".info.json", "r", encoding="utf8") as file:
    video_storage.add_video_info(
      file_name,
      json.load(file)
    )

def end_downloading_hook() -> None:
  video_storage.save_video_info()

def download_videos(links: list[str]) -> None:
  ensure_folder_exists(download_folder)
  #ensure_folder_exists(thumbnail_folder)

  downloader: yt_dlp.YoutubeDL = create_audio_downloader()
  downloader.download(links)
  downloader.close()

def main() -> None:
  download_videos(
    ["https://www.youtube.com/playlist?list=PLKXdyINOQYsbqGQp08A83PtAWNBrY1FXP"]
  )
  ## IDEA FOR LATER
  # prevent forum submissions from using playlist links (like the one above)

if __name__ == "__main__":
  main()