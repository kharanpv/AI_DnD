import sys
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QThread
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTextEdit
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QScrollBar, QDialog, QListWidget, QListWidgetItem
from PyQt5.QtGui import QColor
import re


def get_xyz(text:str=None):
    matches = re.findall(r"\((.*?)\)", text)
    print(matches)
    if matches:
        text = matches[0].replace("(","").replace(")","").replace(" ","")
        text = text.split(',')
        x = text[0]
        y = text[1]
        return x, y
    else:
        return 0, 0

# GOOD MERGED
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

# GOOD MERGED
class HistoryWidget(QListWidget):
    def __init__(self):
        super().__init__()
        self.setWordWrap(True)

    def updateHistory(self, text):
        item = QListWidgetItem(text)
        self.addItem(item)
        self.scrollToBottom()

    def updateResponse(self, text):
        item = QListWidgetItem(text)
        item.setBackground(QColor("lightgray"))
        if text is None or len(text) == 0:
            item.setBackground(QColor("red"))
            item.setText("Response Error!")
        self.addItem(item)
        self.scrollToBottom()

class TextEntryAndHistory(QWidget):
     # GPT Endpoint is now prompt_master.generate_response()
    def __init__(self, fxn_connection=None, gpt_endpoint_fxn=None):
        super().__init__()
        self.gpt_endpoint = gpt_endpoint_fxn
        layout = QVBoxLayout()

        self.historyWidget = HistoryWidget()
        item = QListWidgetItem("DM: What would you like to generate?")
        item.setBackground(QColor("lightgray"))
        self.historyWidget.addItem(item)
        self.scrollableTextEdit = ScrollableTextEdit()
        self.fxn_connection = fxn_connection
        #if fxn_connection != None:
        #    self.scrollableTextEdit.enterPressed.connect(fxn_connection)
        self.scrollableTextEdit.enterPressed.connect(self.interaction)

        layout.addWidget(self.historyWidget, 9)  # 80 of the content
        layout.addWidget(self.scrollableTextEdit, 1)  # 20 of the content

        self.setLayout(layout)


    def updateHistoryClearText(self):
        # this fxn calls img_workflow
        self.text = self.scrollableTextEdit.toPlainText()
        self.historyWidget.updateHistory(self.text)
        self.scrollableTextEdit.clear()

    def interaction(self):
        self.updateHistoryClearText()
        if self.gpt_endpoint:
            self.worker = Worker(self.gpt_endpoint, self.text)
            self.worker.finished.connect(self.handle_response)
            self.worker.start()

    def handle_response(self, text):
        self.historyWidget.updateResponse(text)
        x, y = get_xyz(text=text)
        self.fxn_connection(x=x, y=y, z=1) 

class Worker(QThread):
    finished = pyqtSignal(str)

    def __init__(self, gpt_endpoint, text):
        super().__init__()
        self.gpt_endpoint = gpt_endpoint
        self.text = text

    def run(self):
        response = self.gpt_endpoint(self.text)
        if type(response) == list:
            response = ",".join(str(element) for element in response)

        self.finished.emit(str(response))