import video_storage
from video_info import VideoInfo
from PySide6.QtCore import QSize#, Qt
#from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import \
  (QApplication, QWidget, QPushButton, QMainWindow, QListWidgetItem, QListWidget,)# QLabel)

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
  #side_image_label: QLabel
  
  def __init__(self, video_info: VideoInfo) -> None:
    super().__init__()
    self.video_info = video_info
    self.setText(video_info.title)

    # TODO: figure out how to add the thumbnails to the list items
    #self.side_image_label = QLabel(text="wa", pixmap=QPixmap(self.video_info.thumbnail_path))
    #self.side_image_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
    

def main() -> None:
  global ui_app
  ui_app = QApplication([])

  window = MainWindow()
  window.show()

  ui_app.exec()

if __name__ == "__main__":
  main()