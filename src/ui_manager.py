import video_storage
import sound_player
from video_info import VideoInfo
from PySide6.QtCore import (QSize, QTimer, Qt)
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import \
  (QApplication, QWidget, QPushButton, QMainWindow, QListWidgetItem, QListWidget, QLabel,  QListWidgetItem)

ui_app: QApplication 

class MainWindow(QMainWindow):
  minimum_size: QSize = QSize(400, 300)
  
  def __init__(self) -> None:
    super().__init__()
    
    self.setWindowTitle("Classroom Music Player")
    
    self.video_list: VideoListSide = VideoListSide()
    
    self.setMinimumSize(self.minimum_size)
    
    self.setCentralWidget(self.video_list)

  def exec(self) -> None:
    pass

class VideoListSide(QListWidget):
  def __init__(self):
    super().__init__()
    self.itemClicked.connect(self.item_clicked)

    video_storage.load_video_info()
    for item in video_storage.default_storage_dict["videos"]:
      info: VideoInfo = VideoInfo().info_from_dict(item)
      self.add_item(info)
  
  def add_item(self, video_info: VideoInfo) -> None:
    list_item: QListWidgetItem = QListWidgetItem(self)

    custom_row: VideoListItem = VideoListItem(video_info)

    self.setItemWidget(list_item, custom_row)

  def item_clicked(self, item: QListWidgetItem) -> None:
    connected_widget: VideoListItem = self.itemWidget(item) # type: ignore
    video_info: VideoInfo = connected_widget.video_info
    song_path: str = video_info.video_path
    sound_player.start_playing(song_path)


class VideoListItem(QLabel):
  video_info: VideoInfo
  side_image_label: QLabel
  
  def __init__(self, video_info: VideoInfo) -> None:
    super().__init__()
    self.video_info = video_info
    self.setText(video_info.title)
    
    #TODO: figure out how to add the thumbnails to the list items
    self.side_image_label = QLabel(text="wa", pixmap=QPixmap(self.video_info.thumbnail_path))
    self.side_image_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

def running_loop() -> None:
  song_position: int = sound_player.get_time_played()
  is_playing: bool = sound_player.is_playing()
  playing_string: str = ("playing; " + str(song_position) if (is_playing) else "not playing.")
  
  print("timerlicious; music is " + playing_string)

  for event in sound_player.pygame.event.get():
    if event.type == sound_player.SONG_END:
      print("song end ded")

def main() -> None:
  global ui_app
  ui_app = QApplication([])

  window = MainWindow()
  window.show()

  running_loop_timer: QTimer = QTimer()
  running_loop_timer.timeout.connect(running_loop)
  running_loop_timer.start(1000)
  
  ui_app.exec()

if __name__ == "__main__":
  main()