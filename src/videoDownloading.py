import os
import yt_dlp
import log_manager
from typing import Final

download_folder: Final[str] = "video_storage"

def ensure_download_folder_exists(path: str) -> bool:
  """Makes sure the folder downloaded videos go in exists.
  
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
    return False

  log_manager.print_if_debug(
    log_manager.DebugLevel.WARNINGS,
    f"Had to create a download folder at {path}"
  )
  os.makedirs(path)
  return True

def download_video() -> None:
  pass

def main() -> None:
  ensure_download_folder_exists(download_folder)

if __name__ == "__main__":
  main()