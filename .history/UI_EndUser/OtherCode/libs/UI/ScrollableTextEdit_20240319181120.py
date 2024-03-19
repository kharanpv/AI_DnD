import sys
import os
import json
import re
# import multiprocessing
import threading
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTextEdit
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QScrollBar, QDialog, QListWidget

# Add the parent directory of Pipeline to the Python module search path
pipeline_parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../Pipeline"))
sys.path.append(pipeline_parent_dir)
import prompt_master

img_pipeline_script = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../ComfyUI_windows_portable/Custom_Scripts/create_assets.py"))

def extract_json_response():
    json_path = os.path.join(pipeline_parent_dir, "chat_history.json")
    with open(json_path, "r") as file:
        chat_history = json.load(file)
      

    last_user_prompt = chat_history[-1]["user_prompt"] 
    last_dm_response = chat_history[-1]["dm_response"]

    pattern = re.compile(r"\(\d+\)\s*\n(.*?)\n}", re.DOTALL)
    match = pattern.search(last_dm_response)
    if match:
        return last_user_prompt, match.group(1).strip()  # Trim leading/trailing whitespace
    else:
        return None, None  # If no match found

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

    def updateHistory(self):
        prompt, response = extract_json_response()       
        if prompt and response: 
            self.addItem("Player: " + prompt + '\n' + "DM: " + response)
            self.scrollToBottom()
        else:
            self.addItem("RESPONSE ERROR")
            self.scrollToBottom()


class TextEntryAndHistory(QWidget):
    image_ready = pyqtSignal()

    def __init__(self, fxn_connection=None):
        super().__init__()

        layout = QVBoxLayout()

        self.historyWidget = HistoryWidget()
        self.historyWidget.addItem("DM: What would you like to generate")

        self.scrollableTextEdit = ScrollableTextEdit()

        if fxn_connection != None:
            self.scrollableTextEdit.enterPressed.connect(fxn_connection)
        self.scrollableTextEdit.enterPressed.connect(self.updateHistoryClearText)

        layout.addWidget(self.historyWidget, 9)  # 80 of the content
        layout.addWidget(self.scrollableTextEdit, 1)  # 20 of the content

        self.setLayout(layout)

        prompt_master.setup() # Call the setup function from prompt_master.py

    def updateHistoryClearText(self):
        text = self.scrollableTextEdit.toPlainText()
        prompt_master.generate_response(text)
        self.historyWidget.updateHistory()
        self.scrollableTextEdit.clear()
        img_workflow = threading.Thread(target=self.run_img_workflow)
        img_workflow.start()
    
    @pyqtSlot()
    def run_img_workflow(self):
        prompt_master.setup()
        prompt_master.run_workflow()
        self.image_ready.emit()