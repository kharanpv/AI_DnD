from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction, QFileDialog, QInputDialog, QGraphicsView
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QVBoxLayout, QWidget, QGraphicsSceneWheelEvent, QPushButton, QHBoxLayout
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt
from . import Popup

class ImageControllerPopup(Popup.Popup):
    def __init__(self, parent=None, text:str=None, title:str="Controller Image", another_object=None):
        super().__init__(parent, text, title)

        # Adding buttons for data, move, delete, and rotate
        data_button = QPushButton("Data", self)
        move_button = QPushButton("Move", self)
        delete_button = QPushButton("Delete", self)
        rotate_button = QPushButton("Rotate", self)

        # Connect buttons to corresponding slots/methods
        data_button.clicked.connect(self.handle_data)
        move_button.clicked.connect(self.handle_move)
        delete_button.clicked.connect(self.handle_delete)
        rotate_button.clicked.connect(self.handle_rotate)

        # Create a layout for buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(data_button)
        button_layout.addWidget(move_button)
        button_layout.addWidget(delete_button)
        button_layout.addWidget(rotate_button)

        # Add the button layout to the main layout
        self.layout().addLayout(button_layout)

        # Connect destroyed signal of another_object to close method of ImageControllerPopup
        if another_object:
            another_object.destroyed.connect(self.close)

    def handle_data(self):
        # implements file reading here
        pass

    def handle_move(self):
        # Implement your logic for the move button here
        pass

    def handle_delete(self):
        another_object.remove_self()

    def handle_rotate(self):
        # Implement your logic for the rotate button here
        print("Rotate button clicked")
    def closeEvent(self, event):
        # Close the popup when its parent (main window) is closed
        self.close()

class ImageOnCanvas(QGraphicsPixmapItem):
    def __init__(self, x, y, scale, rotation, image_path):
        super(ImageOnCanvas, self).__init__()
        self.setPos(x, y)
        self.setScale(scale)
        self.setRotation(rotation)
        self.set_image(image_path)
        self.image_path = image_path
        self.selected = False

    def set_image(self, image_path):
        image = QPixmap(image_path)
        self.setPixmap(image)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.selected = not self.selected
            #popup = ImageControllerPopup(another_object=self)
            # Somehow we need a highlight function here
            self.setOpacity(0.7 if self.selected else 1.0)

    def remove_self(self):
        # Remove the item from the scene
        scene = self.scene()
        if scene:
            scene.removeItem(self)

