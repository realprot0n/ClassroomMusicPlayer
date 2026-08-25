import json
from video_info import VideoInfo
from typing import Final
from videoDownloading import download_folder, thumbnail_folder

save_path: Final[str] = "video_storage/video_data.json"

default_storage_dict: dict[str, str | dict | list] = {
  "videos": []
}

def add_video_info(original_path: str, downloaded_info: dict) -> None:
  print(downloaded_info["title"])
  VideoInfo(
    downloaded_info["title"],
    original_path,
    original_path
  )




def move_thumbnails_to(
    folder_to: str = thumbnail_folder
  ) -> None:
  pass

def main() -> None:
  pass

if __name__ == "__main__":
  main()