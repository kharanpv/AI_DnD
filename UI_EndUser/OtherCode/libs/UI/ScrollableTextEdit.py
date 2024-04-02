import sys
import os
import json
import re
# import multiprocessing
import threading
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTextEdit
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QScrollBar, QDialog, QListWidget, QListWidgetItem
from PyQt5.QtGui import QColor

# Add the parent directory of Pipeline to the Python module search path
pipeline_parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../Pipeline"))
sys.path.append(pipeline_parent_dir)
import prompt_master

img_pipeline_script = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../ComfyUI_windows_portable/Custom_Scripts/create_assets.py"))

# def extract_json_response():
#     json_path = os.path.join(pipeline_parent_dir, "chat_history.json")
#     with open(json_path, "r") as file:
#         chat_history = json.load(file)
      

#     last_user_prompt = chat_history[-1]["user_prompt"] 
#     last_dm_response = chat_history[-1]["dm_response"]

#     # pattern = re.compile(r"\(\d+\)\s*\n(.*?)\n}", re.DOTALL)
#     # match = pattern.search(last_dm_response)
#     # if match:
#     #     return last_user_prompt, match.group(1).strip()  # Trim leading/trailing whitespace
#     # else:
#     #     return None, None  # If no match found
#     return last_user_prompt, last_dm_response[1:-1]


# class HistoryWidget(QListWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWordWrap(True)

#     def updateHistory(self):
#         prompt, response = extract_json_response()    
#         if prompt:
#             item = QListWidgetItem("Player: " + prompt)
#             self.addItem(item)
#             self.scrollToBottom()
#         if response: 
#             item = QListWidgetItem("DM: " + response)
#             item.setBackground(QColor("darkgray"))
#             self.addItem(item)
#             self.scrollToBottom()
#         else:
#             item = QListWidgetItem("RESPONSE ERROR")
#             item.setBackground(QColor("red"))
#             self.addItem(item)
#             self.scrollToBottom()


# class TextEntryAndHistory(QWidget):
#     image_ready = pyqtSignal()

#     def __init__(self, fxn_connection=None):
#         super().__init__()

#         layout = QVBoxLayout()

#         self.historyWidget = HistoryWidget()
#         item = QListWidgetItem("DM: What would you like to generate?")
#         item.setBackground(QColor("gray"))
#         self.historyWidget.addItem(item)

#         self.scrollableTextEdit = ScrollableTextEdit()

#         if fxn_connection != None:
#             self.scrollableTextEdit.enterPressed.connect(fxn_connection)
#         self.scrollableTextEdit.enterPressed.connect(self.updateHistoryClearText)

#         layout.addWidget(self.historyWidget, 9)  # 80 of the content
#         layout.addWidget(self.scrollableTextEdit, 1)  # 20 of the content

#         self.setLayout(layout)

#         prompt_master.setup() # Call the setup function from prompt_master.py

#     def updateHistoryClearText(self):
#         text = self.scrollableTextEdit.toPlainText()
#         prompt_master.generate_response(text)
#         self.historyWidget.updateHistory()
#         self.scrollableTextEdit.clear()
#         img_workflow = threading.Thread(target=self.run_img_workflow)
#         img_workflow.start()
    

#     # Nuke TODO
#     @pyqtSlot()
#     def run_img_workflow(self):
#         prompt_master.setup()
#         prompt_master.run_workflow()
#         self.image_ready.emit()

import sys
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QThread
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTextEdit
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QScrollBar, QDialog, QListWidget, QListWidgetItem
from PyQt5.QtGui import QColor

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
        if fxn_connection != None:
            self.scrollableTextEdit.enterPressed.connect(fxn_connection)
        self.scrollableTextEdit.enterPressed.connect(self.interaction)

        layout.addWidget(self.historyWidget, 9)  # 80 of the content
        layout.addWidget(self.scrollableTextEdit, 1)  # 20 of the content

        self.setLayout(layout)

        # NUKE TODO
        # note
        # calls prompt_master.setup() here
        #
        prompt_master.setup() # Call the setup function from prompt_master.py

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

class Worker(QThread):
    finished = pyqtSignal(str)

    def __init__(self, gpt_endpoint, text):
        super().__init__()
        self.gpt_endpoint = gpt_endpoint
        self.text = text

    def run(self):
        response = self.gpt_endpoint(self.text)
        self.finished.emit(response)