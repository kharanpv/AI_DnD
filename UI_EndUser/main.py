#
# Currently scrolling works fine, dragging doesn't
# TODO finish dragging, I will probably separate out mouse when I fix this
#
#

# This is all garbage I will clean later I swear jk sorry
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction, QFileDialog, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QVBoxLayout, QWidget, QGraphicsSceneWheelEvent
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt

DEBUGGING = True
if DEBUGGING:
    from pygit2 import Repository
    DEBUG_NAME = Repository('.').head.shorthand  # 'master'

class ImageOnCanvas(QGraphicsPixmapItem):
    def __init__(self, x, y, scale, image_path):
        super(ImageOnCanvas, self).__init__()
        self.setPos(x, y)
        self.setScale(scale)
        self.set_image(image_path)

    def set_image(self, image_path):
        image = QPixmap(image_path)
        self.setPixmap(image)

class ImageWidget(QGraphicsView):
    def __init__(self, parent=None):
        super(ImageWidget, self).__init__(parent)

        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        self.setRenderHint(QPainter.Antialiasing, True)
        self.setRenderHint(QPainter.SmoothPixmapTransform, True)

        self.image_item = QGraphicsPixmapItem()
        self.scene.addItem(self.image_item)

        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.middle_mouse_pressed = False
        self.setMouseTracking(True)

    def set_image(self, image_path):
        image = QPixmap(image_path)
        self.image_item.setPixmap(image)

    def wheelEvent(self, event: QGraphicsSceneWheelEvent):
        factor = 1.2
        if event.angleDelta().y() < 0:
            factor = 1.0 / factor

        self.scale(factor, factor)

    def mousePressEvent(self, event):
        super(ImageWidget, self).mousePressEvent(event)

        if event.button() == Qt.MiddleButton:
            self.middle_mouse_pressed = True
            self.last_middle_pos = event.pos()

        elif event.button() == Qt.RightButton:  # Handle right-click event
            pos = self.mapToScene(event.pos())
            image_path, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.bmp *.gif *.jpeg);;All Files (*)")
            if image_path:
                new_image_item = ImageOnCanvas(pos.x(), pos.y(), 1.0, image_path)
                self.scene.addItem(new_image_item)

    def mouseReleaseEvent(self, event):
        super(ImageWidget, self).mouseReleaseEvent(event)

        if event.button() == Qt.MiddleButton:
            self.middle_mouse_pressed = False

    def mouseMoveEvent(self, event):
        super(ImageWidget, self).mouseMoveEvent(event)

        if self.middle_mouse_pressed:
            delta = event.pos() - self.last_middle_pos
            self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() - delta.x())
            self.verticalScrollBar().setValue(self.verticalScrollBar().value() - delta.y())
            self.last_middle_pos = event.pos()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        self.image_widget = ImageWidget(self)
        self.layout.addWidget(self.image_widget)

        self.setup_menu_bar()

        self.setWindowTitle('The Jaran Project')
        if DEBUGGING:
            self.setWindowTitle(DEBUG_NAME)
        self.setGeometry(100, 100, 800, 600)

    def setup_menu_bar(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')

        open_action = QAction('Open', self)
        open_action.triggered.connect(self.open_image)
        file_menu.addAction(open_action)

        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

    def open_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.bmp *.gif *.jpeg);;All Files (*)", options=options)

        if file_name:
            self.image_widget.set_image(file_name)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


# Below is a rough first draft. I started mixing QtPy and Qt5, and that caused issues (interop in QtCreator , but not python alone)
# import sys
# from qtpy.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QVBoxLayout, QMenu, QAction, QWidget

# from ui_map import MyGraphicsView
# class DraggableGridItem(QGraphicsRectItem):
#     def __init__(self, x, y, size):
#         super().__init__(x, y, size, size)
#         self.setFlag(QGraphicsRectItem.ItemIsMovable)


# class SimpleImageViewer(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.initUI()

#     def initUI(self):
#         # Create the main layout
#         main_layout = QVBoxLayout()

#         # Create QGraphicsScene and a our viewer for displaying images
#         self.scene = QGraphicsScene()
#         self.view = MyGraphicsView(self.scene)
#         main_layout.addWidget(self.view)

#         # Create a central widget and set the layout
#         central_widget = QWidget()
#         central_widget.setLayout(main_layout)
#         self.setCentralWidget(central_widget)

#         # Create top drop down menu
#         self.createTopMenu()

#         # Add a draggable grid to the scene
#         grid_size = 50
#         for x in range(0, 500, grid_size):
#             for y in range(0, 500, grid_size):
#                 grid_item = DraggableGridItem(x, y, grid_size)
#                 self.scene.addItem(grid_item)

#         # Set up the main window
#         self.setGeometry(100, 100, 800, 600)
#         self.setWindowTitle('Draggable Grid Image Viewer')

#     def openImage(self):
#         # In a real application, you would implement image loading logic here
#         # For simplicity, let's just show a placeholder message
#         self.showMessage('Open Image', 'Placeholder: Implement image loading logic here')

#     def showMessage(self, title, message):
#         # Show a simple message box
#         msg_box = QMenu(title)
#         msg_box.addAction(message)
#         msg_box.exec_()

#     def createTopMenu(self):
#         # Create a simple menu bar with a File menu
#         menubar = self.menuBar()
#         file_menu = menubar.addMenu('File')

#         # Create actions for the File menu
#         open_action = QAction('Open', self)
#         open_action.triggered.connect(self.openImage)
#         file_menu.addAction(open_action)

#         exit_action = QAction('Exit', self)
#         exit_action.triggered.connect(self.close)
#         file_menu.addAction(exit_action)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = SimpleImageViewer()
#     window.show()
#     sys.exit(app.exec_())
