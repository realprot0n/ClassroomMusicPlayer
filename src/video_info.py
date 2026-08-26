import json
from typing import Self

class VideoInfo:
  title: str
  video_path: str
  thumbnail_path: str
  video_id: str
  suggestor_name: str
  anonymous_suggestor: bool
  
  def __init__(self, title: str, video_path: str, thumbnail_path: str, video_id: str, suggestor_name: str = "", anonymous_suggestor: bool = False) -> None:
    self.title = title
    self.video_path = video_path
    self.thumbnail_path = thumbnail_path
    self.video_id = video_id
    self.suggestor_name = suggestor_name
    self.anonymous_suggestor = anonymous_suggestor
  
  def turn_into_dict(self: Self) -> dict[str, str]:
    return {
      "anonymous_suggestor": self.anonymous_suggestor,
      "suggestor_name": self.suggestor_name,
      "thumbnail_path": self.thumbnail_path,
      "video_path": self.video_path,
      "title": self.title,
      "video_id": self.video_id,
    }
  
  def turn_into_json(self: Self) -> str:
    return json.dumps(self.turn_into_dict(), indent="  ")
  
  def info_from_dict(self: Self, dictionary: dict[str, str]) -> None:
    self.anonymous_suggestor = bool(dictionary.get("anonymous_suggestor", ""))
    self.suggestor_name = dictionary.get("suggestor_name", "")
    self.video_path = dictionary.get("video_path", "")
    self.thumbnail_path = dictionary.get("thumbnail_path", "")
    self.video_id = dictionary.get("video_id", "")
    self.title = dictionary.get("title", "")
  
  def info_from_json(self: Self, json_str: str) -> None:
    self.info_from_dict(json.loads(json_str))