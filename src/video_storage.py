import json
from video_info import VideoInfo
from typing import Final, Any
from videoDownloading import download_folder, thumbnail_folder

save_path: Final[str] = "video_storage/video_data.json"

default_storage_dict: dict[str, Any] = {
  "videos": []
}

def add_video_info(original_path: str, downloaded_info: dict) -> None:
  print(downloaded_info["title"])
  info: VideoInfo = VideoInfo(
    downloaded_info["title"],
    original_path,
    original_path
  )
  default_storage_dict["videos"].append(info.turn_into_dict())

def save_video_info(path: str = save_path) -> None:
  with open(path, "r") as save:
    json.dump(default_storage_dict, save, indent="  ")

def load_video_info(path: str = save_path) -> None:
  with open(path, "w") as save:
    default_storage_dict = json.load(save)

def move_thumbnails_to(
    folder_to: str = thumbnail_folder
  ) -> None:
  pass

def main() -> None:
  pass

if __name__ == "__main__":
  main()