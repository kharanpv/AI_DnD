from . import ImageOnCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction, QFileDialog, QInputDialog, QGraphicsView
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QVBoxLayout, QWidget, QGraphicsSceneWheelEvent


from PyQt5.QtGui import QPixmap, QPainter, QColor, QImage, QBrush
from PyQt5.QtCore import Qt
from .. import LocationObject
import os
from PyQt5.QtCore import QRectF

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
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.texturePath = script_dir + "/tessalation-grass.png"

        # Images
        self.image_items = []

        # Mouse
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.middle_mouse_pressed = False
        self.left_mouse_pressed = False
        self.setMouseTracking(True)

    # def drawBackground(self, painter, rect):
    #     super().drawBackground(painter, rect)
    #     sceneRect = self.sceneRect()
    #     print(self.texturePath)
    #     pixmap = QPixmap(self.texturePath)
    #     rectf = QRectF(pixmap.rect())
    #     painter.drawPixmap(sceneRect, pixmap, rect)
    def drawBackground(self, painter, rect):
        super().drawBackground(painter, rect)
        # self.setBackgroundBrush(QBrush((QColor(63, 155, 11))))
        self.setBackgroundBrush(QBrush((QColor(0, 0, 0))))

    def set_image(self, image_path):
        image = QPixmap(image_path)
        self.image_item.setPixmap(image)

    def add_image(self, image_path:str, x:int, y:int, rotation:float, scale:float):
        self.addImageOnCanvas(ImageOnCanvas.ImageOnCanvas(x=x, y=y, scale=scale, rotation=rotation, image_path=image_path))

    def add_LocationObject(self, obj: LocationObject):
        self.add_image(obj.image_path, obj.x, obj.y, obj.rotation, obj.scale)

    def wheelEvent(self, event: QGraphicsSceneWheelEvent):
        factor = 1.2
        if event.angleDelta().y() < 0:
            factor = 1.0 / factor

        # Limit the scale to a certain threshold
        current_scale = self.transform().m11()  # Get the current horizontal scale factor
        min_scale = 0.18
        new_scale = current_scale * factor

        if new_scale < min_scale:
            factor = min_scale / current_scale

        self.scale(factor, factor)

    def addImageOnCanvas(self, image_on_canvas):
        image_on_canvas.set_parent(self)
        self.scene.addItem(image_on_canvas)
        self.image_items.append({'x': image_on_canvas.x, 'y': image_on_canvas.x, 'image_path': image_on_canvas.image_path})
    
    def removeItem(self, image_on_canvas):
        self.scene.removeItem(image_on_canvas)

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
            image_path, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.bmp *.gif *.jpeg *.lobj);;All Files (*)")
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


    def clear_canvas(self):
        self.scene.clear()
        self.image_items.clear()

    def get_selected_images(self):
        retValue = []
        for x_image in self.image_items:
            if x_image.selected == True:
                retValue += x_image
        return retValue

    def save(self, folder_path):
        # Create the folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        location_objects = []
        for item in self.scene.items():
            if isinstance(item, ImageOnCanvas.ImageOnCanvas):
                location_object = item.save_to_LocationObject()
                location_objects.append(location_object)

        for i, location_object in enumerate(location_objects):
            #file_path = os.path.join(folder_path, f"location_{i + 1}.json")
            location_object.save(folder_path)
            print("LocationObject saved to:", folder_path)

    def load_images_folder(self, folder_path):
        location_objects = []
        # Iterate over all files in the folder
        for filename in os.listdir(folder_path):
            # Check if the file is a .lobj file
            if filename.endswith(".lobj"):
                # Construct the full file path
                file_path = os.path.join(folder_path, filename)
                # Load the location object from the file
                location_object = LocationObject.LocationObject.load(file_path)  # Assuming LocationObject has a class method 'load'
                location_objects.append(location_object)
        for i in location_objects:
            self.add_LocationObject(obj=i)
            
    def open_latest_image(self, x, y, z, rotation = 0.0):
        folder_path = os.path.join(os.path.dirname(__file__), '..', '..', '..',"test_images")
        files = os.listdir(folder_path)
        if not files:
            print("No images found in test_images folder.")
            return

        # Filter only image files
        image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.bmp', '.gif', '.jpeg'))]

        if not image_files:
            print("No image files found in test_images folder.")
            return

        print("About to crash...")
        # Get the latest modified image file
        latest_image = max(image_files, key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))
        latest_image_path = os.path.join(folder_path, latest_image)
        # WE NEED COORDS HERE
        if latest_image:
            self.addImageOnCanvas(ImageOnCanvas.ImageOnCanvas(int(x), int(y), int(z), rotation, latest_image_path))