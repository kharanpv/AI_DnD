#
# Currently scrolling works fine, dragging doesn't
# TODO finish dragging, I will probably separate out mouse when I fix this
# - fix Z, it currently is generated but not used. Higher Z should over lay lower Z images
#        - this will require someform of Z system probably
# - add rotation to generations
# - add wall combinations
#   - this will probably be hard
#   
#
#

# This is all garbage I will clean later I swear jk sorry
import sys
import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QSplitter, QMenuBar, QMenu, QAction, QFileDialog, QInputDialog, QGraphicsView
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QHBoxLayout, QVBoxLayout, QWidget, QGraphicsSceneWheelEvent


from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot

from OtherCode.libs.UI import ImageOnCanvas, ViewWindow, Popup, ScrollableTextEdit

DEBUGGING = True
if DEBUGGING:
    from pygit2 import Repository
    DEBUG_NAME = Repository('.').head.shorthand 

pipeline_parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../Pipeline"))

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Create a QSplitter to manage the resizing of the widgets
        splitter = QSplitter(Qt.Horizontal)

        # Create the image_widget on the left
        self.image_widget = ViewWindow.ViewWindow(self)
        splitter.addWidget(self.image_widget)

        self.side_bar = ScrollableTextEdit.TextEntryAndHistory()
        splitter.addWidget(self.side_bar)
        self.side_bar.image_ready.connect(self.open_latest_image)

        # Set the size ratio for the widgets (80% - 20%)
        splitter.setSizes([4 * splitter.size().width() // 5, splitter.size().width() // 5])

        layout = QVBoxLayout(self.central_widget)
        layout.addWidget(splitter)

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

        list_images_action = QAction('List Images', self)
        list_images_action.triggered.connect(self.list_images)
        file_menu.addAction(list_images_action)

        list_selected_images_action = QAction('Show Selected Details', self)
        list_selected_images_action.triggered.connect(self.show_selected)
        file_menu.addAction(list_selected_images_action)


        pop_action = QAction('Popup', self)
        pop_action.triggered.connect(self.open_popup)
        file_menu.addAction(pop_action)
        # Canvas Menu
        canvas_menu = menubar.addMenu('Canvas')

        list_images_action = QAction('List Images', self)
        list_images_action.triggered.connect(self.list_images)
        canvas_menu.addAction(list_images_action)

        populate_canvas_action = QAction('Populate Canvas', self)
        populate_canvas_action.triggered.connect(self.populate_canvas)
        canvas_menu.addAction(populate_canvas_action)
            
    def setup_side_bar(self):
        pass
    def open_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.bmp *.gif *.jpeg);;All Files (*)", options=options)

        if file_name:
            self.image_widget.set_image(file_name)
    
    @pyqtSlot()
    def open_latest_image(self):
        folder_path = os.path.join(os.path.dirname(__file__), "test_images")
        files = os.listdir(folder_path)
        if not files:
            print("No images found in test_images folder.")
            return

        # Filter only image files
        image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.bmp', '.gif', '.jpeg'))]

        if not image_files:
            print("No image files found in test_images folder.")
            return

        # Get the latest modified image file
        latest_image = max(image_files, key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))
        latest_image_path = os.path.join(folder_path, latest_image)
        if latest_image:
            self.addImageOnCanvas(ImageOnCanvas.ImageOnCanvas(10, 10, 10, 0.0, image_path))



    def list_images(self):
        image_list = self.image_widget.list_images_on_canvas()
        for index, image_info in enumerate(image_list):
            print(f"Image {index + 1}:")
            print(f"  Location: ({image_info['x']}, {image_info['y']})")
            # Below broke upon importing images from cont files, don't know why
            #print(f"  Rotation: {image_info['rotation']} degrees")
            print(f"  File Name: {image_info['image_path']}")
            print()
    # This will eventually consume some other kind of data, ie a text file full of image links
    # this is proof of concept for now
    def populate_canvas(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Set", "", "Custom Continuity files (*.cont);;All Files (*)", options=options)

        asset_folder = "./assets/"
        with open(file_name) as handle:
            for line in handle:
                image_path, x, y, z, scale =  map(str.strip, line.split(','))
                # Rotation is currently unused for our generations
                # So is Z, it would require a queing system or something
                rotation = 0
                # Currently X and Y have a bad offset, as images are positioned to the top left corner not the middle
                # We need to calculate this based off of scale, where positioning is x-scale/2, y-scale/2
                # Convert numeric values to appropriate types
                x = int(float(x)*1024)
                y = int(float(y)*1024)
                scale = float(scale)

                x = x - int(scale*1024/2)
                y = y - int(scale*1024/2)
                rotation = int(rotation)

                # Create ImageOnCanvas instance and append to image_list
                image_item = ImageOnCanvas.ImageOnCanvas(x, y, scale, rotation, asset_folder+image_path)
                self.image_widget.addImageOnCanvas(image_item)

    def open_popup(self):
        popup = Popup.Popup(self)
        popup.show()
    
    def show_selected(self):
        for x in self.image_widget.get_selected_images():
            print(x)
            popup = Popup.Popup(self)


    def open_selected_popup(self, title, text):
        Popup = Popup.Popup(self, "")




if __name__ == '__main__':
    json_path = os.path.join(pipeline_parent_dir, "chat_history.json")
    if os.path.exists(json_path):
        os.remove(json_path)
    else:
        print("File does not exist.")
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())