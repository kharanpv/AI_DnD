import sys
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTextEdit
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QScrollBar, QDialog, QListWidget

class ScrollableTextEdit(QTextEdit):
    enterPressed = pyqtSignal()

    def __init__(self):
        super().__init__()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.enterPressed.emit()
        else:
            super().keyPressEvent(event)

    def wheelEvent(self, event):
        modifiers = QApplication.keyboardModifiers()
        if modifiers == Qt.ControlModifier:
            # zoom in/out functionality
            if event.angleDelta().y() > 0:
                self.zoomIn(1)
            else:
                self.zoomOut(1)
        else:
            super().wheelEvent(event)


class HistoryWidget(QListWidget):
    def __init__(self):
        super().__init__()

    def updateHistory(self, text):
        self.addItem(text)
        self.scrollToBottom()


class TextEntryAndHistory(QWidget):
    def __init__(self, fxn_connection=None):
        super().__init__()

        layout = QVBoxLayout()

        self.historyWidget = HistoryWidget()
        self.scrollableTextEdit = ScrollableTextEdit()
        if fxn_connection != None:
            self.scrollableTextEdit.enterPressed.connect(fxn_connection)
        self.scrollableTextEdit.enterPressed.connect(self.updateHistoryClearText)

        layout.addWidget(self.historyWidget, 9)  # 80 of the content
        layout.addWidget(self.scrollableTextEdit, 1)  # 20 of the content

        self.setLayout(layout)

    def updateHistoryClearText(self):
        text = self.scrollableTextEdit.toPlainText()
        self.historyWidget.updateHistory(text)
        self.scrollableTextEdit.clear()