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

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction, QFileDialog, QInputDialog, QGraphicsView
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QVBoxLayout, QWidget, QGraphicsSceneWheelEvent


from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt

from OtherCode.libs import token_lib as token_lib
from OtherCode.libs.UI import ImageOnCanvas, ViewWindow

DEBUGGING = True
if DEBUGGING:
    from pygit2 import Repository
    DEBUG_NAME = Repository('.').head.shorthand 


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        self.image_widget = ViewWindow.ViewWindow(self)
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

        list_images_action = QAction('List Images', self)
        list_images_action.triggered.connect(self.list_images)
        file_menu.addAction(list_images_action)
        # Canvas Menu
        canvas_menu = menubar.addMenu('Canvas')

        list_images_action = QAction('List Images', self)
        list_images_action.triggered.connect(self.list_images)
        canvas_menu.addAction(list_images_action)

        populate_canvas_action = QAction('Populate Canvas', self)
        populate_canvas_action.triggered.connect(self.populate_canvas)
        canvas_menu.addAction(populate_canvas_action)

        # API Menu
        api_menu = menubar.addMenu('API')
        
        sublist_api_menu = api_menu.addMenu('Select API')
        for a_name, a_function in token_lib.list_of_apis.items():
            api_name = a_name
            api_function = a_function

            api_action = QAction(api_name, self)
            api_action.triggered.connect(api_function)

            sublist_api_menu.addAction(api_action)
            
    def open_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.bmp *.gif *.jpeg);;All Files (*)", options=options)

        if file_name:
            self.image_widget.set_image(file_name)

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
                image_item = ImageOnCanvas(x, y, scale, rotation, asset_folder+image_path)
                self.image_widget.addImageOnCanvas(image_item)




    # API Stuff
    def select_api(self):
        pass
        #for item in token_lib.api_list:
        #    pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())