import os
import pygame
from typing import Final

os.environ["SDL_VIDEODRIVER"] = "dummy"
pygame.init()
screen: pygame.Surface = pygame.display.set_mode((1,1))

pygame.mixer.init()
SONG_END: Final[int] = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

def start_playing(song_path: str, loop_count: int = 0, volume: float = 0.5) -> None:
  if not os.path.exists(song_path):
    raise FileNotFoundError(song_path)
  
  pygame.mixer.music.load(song_path)
  pygame.mixer.music.set_volume(volume)
  pygame.mixer.music.play(loops=loop_count)

def pause_playback() -> None:
  if not pygame.mixer.music.get_busy():
    return
  
  pygame.mixer.music.pause()

def stop_playback() -> None:
  if not pygame.mixer.music.get_busy():
    return

  pygame.mixer.music.stop()

def main() -> None:
  pass

if __name__ == "__main__":
  pass