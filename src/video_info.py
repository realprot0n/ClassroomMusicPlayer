import json
from typing import Self

class VideoInfo:
  title: str
  video_path: str
  thumbnail_path: str
  
  def __init__(self, title: str, video_path: str, thumbnail_path: str) -> None:
    self.title = title
    self.video_path = video_path
    self.thumbnail_path = thumbnail_path
  
  def turn_into_dict(self: Self) -> dict[str, str]:
    return {
      "title": self.title,
      "video_path": self.video_path,
      "thumbnail_path": self.thumbnail_path
    }
  
  def turn_into_json(self: Self) -> str:
    return json.dumps(self.turn_into_dict(), indent="  ")
  
  def info_from_dict(self: Self, dictionary: dict[str, str]) -> None:
    title = dictionary.get("title", None)
    video_path = dictionary.get("video_path", None)
    thumbnail_path = dictionary.get("thumbnail_path", None)
  
  def info_from_json(self: Self, json_str: str) -> None:
    self.info_from_dict(json.loads(json_str))