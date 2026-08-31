from PySide6.QtCore import QSize
from PySide6.QtWidgets import (QApplication, QWidget, QPushButton, QMainWindow)
ui_app: QApplication 

class MainWindow(QMainWindow):
  minimum_size: QSize = QSize(400, 300)
  
  def __init__(self) -> None:
    super().__init__()
    
    self.setWindowTitle("Classroom Music Player")
    
    self.button: QPushButton = QPushButton("push me.")
    
    self.setMinimumSize(self.minimum_size)
    
    self.setCentralWidget(self.button)

def main() -> None:
  ui_app = QApplication([])

  window = MainWindow()
  window.show()

  ui_app.exec()

if __name__ == "__main__":
  main()