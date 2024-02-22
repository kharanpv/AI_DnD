import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QScrollArea, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt

class Popup(QWidget):
    def __init__(self, parent=None, text:str=None, title:str="Popup"):
        super().__init__(parent)

        self.setWindowTitle(title)
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout(self)

        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_content = QWidget(scroll_area)
        scroll_area.setWidget(scroll_content)

        scroll_layout = QVBoxLayout(scroll_content)

        label = QLabel(text)
        scroll_layout.addWidget(label)

        layout.addWidget(scroll_area)

    # Enable window dragging
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.drag_position = None

    # Closing (button is wack, TODO)
        close_button = QPushButton("Close", self)
        close_button.clicked.connect(self.close)
        button_layout = QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(close_button)
        layout.addLayout(button_layout)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_position)

    def change_text(self, text):
        pass

    def closeEvent(self, event):
        # Close the popup when its parent (main window) is closed
        self.close()