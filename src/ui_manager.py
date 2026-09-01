import video_storage
from video_info import VideoInfo
from PySide6.QtCore import QSize
from PySide6.QtWidgets import (QApplication, QWidget, QPushButton, QMainWindow, QListWidgetItem, QListWidget)

ui_app: QApplication 

class MainWindow(QMainWindow):
  minimum_size: QSize = QSize(400, 300)
  
  def __init__(self) -> None:
    super().__init__()
    
    self.setWindowTitle("Classroom Music Player")
    
    self.video_list: VideoListSide = VideoListSide()
    video_storage.load_video_info()
    for item in video_storage.default_storage_dict["videos"]:
      info: VideoInfo = VideoInfo().info_from_dict(item)
      list_item: VideoListItem = VideoListItem(info)
      self.video_list.addItem(list_item)
    
    self.setMinimumSize(self.minimum_size)
    
    self.setCentralWidget(self.video_list)

class VideoListSide(QListWidget):
  
  def __init__(self):
    super().__init__()

class VideoListItem(QListWidgetItem):
  video_info: VideoInfo
  def __init__(self, video_info: VideoInfo) -> None:
    super().__init__()
    self.video_info = video_info
    self.setText(video_info.title)

def main() -> None:
  ui_app = QApplication([])

  window = MainWindow()
  window.show()

  ui_app.exec()

if __name__ == "__main__":
  main()