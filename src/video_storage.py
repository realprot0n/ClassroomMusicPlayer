import json
import os
from typing import Final, Any
from video_info import VideoInfo
from videoDownloading import download_folder, thumbnail_folder

save_path: Final[str] = "video_storage/video_data.json"

default_storage_dict: dict[str, Any] = {
  "videos": []
}

def video_info_already_in_dict(video_id: str) -> bool:
  for video_info in default_storage_dict["videos"]:
    if video_info["video_id"] == video_id:
      return True
  return False

def add_video_info(original_path: str, downloaded_info: dict, suggestor: str, anonymous: str | bool) -> bool:
  video_id: str = downloaded_info["id"]
  if video_info_already_in_dict(video_id):
    return False

  if type(anonymous) == str:
    anonymous = True if anonymous.lower() == "yes" else False

  info: VideoInfo = VideoInfo(
    downloaded_info["title"],
    original_path + ".mp3",
    original_path + ".webp",
    video_id,
    suggestor,
    bool(anonymous),
  )
  default_storage_dict["videos"].append(info.turn_into_dict())
  return True

def save_video_info(path: str = save_path) -> None:
  open_code: str = "x"
  if os.path.exists(path):
    open_code = "w"
  
  with open(path, open_code) as save:
    json.dump(default_storage_dict, save, indent="  ")

def load_video_info(path: str = save_path) -> None:
  with open(path, "r") as save:
    default_storage_dict = json.load(save)

def move_thumbnails_to(
    folder_to: str = thumbnail_folder
  ) -> None:
  pass

def main() -> None:
  pass

if __name__ == "__main__":
  main()