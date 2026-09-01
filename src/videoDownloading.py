import os
import csv
import json
import yt_dlp
import log_manager
import video_storage
from typing import Final
from yt_dlp.postprocessor.ffmpeg import FFmpegExtractAudioPP

download_folder: Final[str] = "video_storage"
thumbnail_folder: Final[str] = "video_storage/thumbnails"
ffmpeg_folder: Final[str] = "ffmpeg_binaries"

csv_values: dict[str, list[str]]
current_video_index: int = 0

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

def add_ffmpeg_folder_to_path(path: str = ffmpeg_folder) -> None:
  ensure_folder_exists(path)
  os.environ["PATH"] = os.path.abspath(path) + os.pathsep + os.environ["PATH"]

def make_audio_options() -> yt_dlp._Params:
  return {
    "extractor_retries": 3,
    "paths":{"home": download_folder},
    "socket_timeout": 30,
    "quiet": True,
    "writeinfojson": True,
    "writethumbnail": True,
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
  global current_video_index
  if data["status"] != "finished":
    return
  
  file_name: str = os.path.abspath(data["filename"])
  file_name = ".".join(file_name.split(".")[:-2])
  format_json_file(file_name + ".info.json")

  with open(file_name + ".info.json", "r", encoding="utf8") as file:
    downloaded_info: dict[str, str] = json.load(file)
    video_id: str = downloaded_info["id"]
    if video_storage.video_info_already_in_dict(video_id):
      return

    if video_storage.add_video_info(
      file_name,
      downloaded_info,
      csv_values["name"][current_video_index],
      csv_values["anonymous"][current_video_index]
    ):
      current_video_index += 1

def end_downloading_hook() -> None:
  video_storage.save_video_info()

def download_videos(links: list[str]) -> None:
  ensure_folder_exists(download_folder)
  #ensure_folder_exists(thumbnail_folder)
  add_ffmpeg_folder_to_path()

  downloader: yt_dlp.YoutubeDL = create_audio_downloader()
  downloader.download(links)
  downloader.close()

def get_videos_from_csv(path: str = "src/Video Link Submissions (Responses) - Form Responses 1.csv") -> dict[str, list[str]]:
  with open(path, "r") as csv_file:
    reader = csv.reader(csv_file)
    
    return_values: dict[str, list[str]] = {
      "name": [],
      "anonymous": [],
      "link": [],
    }
    first_line: bool = True
    for line in reader:
      if first_line:
        first_line = False
        continue
      
      return_values["name"].append(line[1])
      return_values["anonymous"].append(line[2])
      return_values["link"].append(line[3])
  
  return return_values

def main() -> None:
  global csv_values
  csv_values = get_videos_from_csv()
  download_videos(
    csv_values["link"]
  )
  ## IDEA FOR LATER
  # prevent forum submissions from using playlist links

if __name__ == "__main__":
  main()