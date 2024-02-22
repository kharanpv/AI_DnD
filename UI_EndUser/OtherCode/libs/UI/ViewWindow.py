from . import ImageOnCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction, QFileDialog, QInputDialog, QGraphicsView
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QVBoxLayout, QWidget, QGraphicsSceneWheelEvent


from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt

class ViewWindow(QGraphicsView):
    def __init__(self, parent=None):
        super(ViewWindow, self).__init__(parent)

        # Qt Rendering
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        self.setRenderHint(QPainter.Antialiasing, True)
        self.setRenderHint(QPainter.SmoothPixmapTransform, True)

        self.image_item = QGraphicsPixmapItem()
        self.scene.addItem(self.image_item)

        # Images
        self.image_items = []  

        # Mouse
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.middle_mouse_pressed = False
        self.left_mouse_pressed = False
        self.setMouseTracking(True)

    def set_image(self, image_path):
        image = QPixmap(image_path)
        self.image_item.setPixmap(image)

    def wheelEvent(self, event: QGraphicsSceneWheelEvent):
        factor = 1.2
        if event.angleDelta().y() < 0:
            factor = 1.0 / factor

        self.scale(factor, factor)

    def addImageOnCanvas(self, image_on_canvas):
        self.scene.addItem(image_on_canvas)
        self.image_items.append({'x': image_on_canvas.x, 'y': image_on_canvas.x, 'image_path': image_on_canvas.image_path})

    def mousePressEvent(self, event):
        super(ViewWindow, self).mousePressEvent(event)
        # Maybe swap this to a switch (match in py 3.10)
        # waiting until guaranteed stability of pyqt5
        if event.button() == Qt.LeftButton:
            self.left_mouse_pressed = True
            self.last_left_pos = event.pos()

        elif event.button() == Qt.MiddleButton:
            self.middle_mouse_pressed = True
            self.last_middle_pos = event.pos()

        elif event.button() == Qt.RightButton: 
            pos = self.mapToScene(event.pos())
            #rotation = Qt.QInput
            image_path, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.bmp *.gif *.jpeg);;All Files (*)")
            if image_path:
                self.addImageOnCanvas(ImageOnCanvas.ImageOnCanvas(pos.x(), pos.y(), 1.0, 0.0, image_path))

    def mouseReleaseEvent(self, event):
        super(ViewWindow, self).mouseReleaseEvent(event)

        if event.button() == Qt.MiddleButton:
            self.middle_mouse_pressed = False

    def mouseMoveEvent(self, event):
        super(ViewWindow, self).mouseMoveEvent(event)

        if self.middle_mouse_pressed:
            delta_middle = event.pos() - self.last_middle_pos
            self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() - delta_middle.x())
            self.verticalScrollBar().setValue(self.verticalScrollBar().value() - delta_middle.y())
            self.last_middle_pos = event.pos()

    def list_images_on_canvas(self):
        return self.image_items