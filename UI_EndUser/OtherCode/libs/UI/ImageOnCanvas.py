from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction, QFileDialog, QInputDialog, QGraphicsView
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QVBoxLayout, QWidget, QGraphicsSceneWheelEvent, QPushButton, QHBoxLayout
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QWidget, QTabWidget, QHBoxLayout
from PyQt5.QtWidgets import QLabel, QLineEdit

from . import Popup
#
# Below should eventually be replaced with 
#
class ImageControllerPopup(Popup.Popup):
    def __init__(self, parent=None, text:str=None, title:str="Controller Image", alternate_parent=None):
        super().__init__(parent, text, title)

        if alternate_parent:
            self.alternate_parent = alternate_parent
            self.add_text(alternate_parent.image_path)

        # Create a tab widget
        self.tab_widget = QTabWidget(self)

        # Adding buttons for data, move, delete, and rotate to separate tabs
        # add_tab is a place holder currently
        # these should be staticly encoded
        self.add_tab("Data", self.handle_data)
        self.add_move_tab()
        self.add_tab("Delete", self.handle_delete)
        self.add_rotate_tab()
        self.add_scale_tab()

        # Add the tab widget to the main layout
        self.layout().addWidget(self.tab_widget)

    def add_tab(self, title, handler_function):
        # Create a tab and layout
        tab = QWidget()
        tab_layout = QVBoxLayout()

        # Adding buttons to the tab
        button = QPushButton(title, self)
        button.clicked.connect(handler_function)

        # Add the button to the layout
        tab_layout.addWidget(button)

        # Set the layout for the tab
        tab.setLayout(tab_layout)

        # Add the tab to the tab widget
        self.tab_widget.addTab(tab, title)

    def add_move_tab(self):
        title = "Move"

        # Create a tab and layout
        tab = QWidget()
        tab_layout = QVBoxLayout()
        # Add labels and input boxes for X, Y, and Z coordinates
        x_label = QLabel("X:")
        x_input = QLineEdit(self)
        tab_layout.addWidget(x_label)
        tab_layout.addWidget(x_input)

        y_label = QLabel("Y:")
        y_input = QLineEdit(self)
        tab_layout.addWidget(y_label)
        tab_layout.addWidget(y_input)

        z_label = QLabel("Z:")
        z_input = QLineEdit(self)
        tab_layout.addWidget(z_label)
        tab_layout.addWidget(z_input)
        # Adding buttons to the tab
        button = QPushButton(title, self)

        handler_function = lambda: self.alternate_parent.move_item(x_input.text(), y_input.text(), z_input.text())
        button.clicked.connect(handler_function)

        # Add the button to the layout
        tab_layout.addWidget(button)

        # Set the layout for the tab
        tab.setLayout(tab_layout)

        # Add the tab to the tab widget
        self.tab_widget.addTab(tab, title)

    def add_rotate_tab(self):
        title = "Rotate"
        # Create a tab and layout
        tab = QWidget()
        tab_layout = QVBoxLayout()
        # Add labels and input boxes for X, Y, and Z coordinates
        rot_label = QLabel("Angle:")
        rot_input = QLineEdit(self)
        tab_layout.addWidget(rot_label)
        tab_layout.addWidget(rot_input)
        # Adding buttons to the tab
        button = QPushButton(title, self)
        handler_function = lambda: self.alternate_parent.rotate_item(rot_input.text())
        button.clicked.connect(handler_function)
        # Add the button to the layout
        tab_layout.addWidget(button)

        button = QPushButton(title + " Absolute", self)
        handler_function = lambda: self.alternate_parent.rotate_item(rot_input.text(), absolute=True)
        button.clicked.connect(handler_function)
        tab_layout.addWidget(button)
        

        # Set the layout for the tab
        tab.setLayout(tab_layout)

        # Add the tab to the tab widget
        self.tab_widget.addTab(tab, title)

    def add_scale_tab(self):
        title = "Scale"
        
        # Create a tab and layout
        tab = QWidget()
        tab_layout = QVBoxLayout()
        
        # Add labels and input boxes for X, Y, and Z coordinates
        scal_label = QLabel("Factor:")
        scal_input = QLineEdit(self)
        tab_layout.addWidget(scal_label)
        tab_layout.addWidget(scal_input)
        
        # Adding buttons to the tab
        button = QPushButton(title, self)
        handler_function = lambda: self.alternate_parent.scale_item(scal_input.text())
        button.clicked.connect(handler_function)

        # Add the button to the layout
        tab_layout.addWidget(button)

        # Set the layout for the tab
        tab.setLayout(tab_layout)

        # Add the tab to the tab widget
        self.tab_widget.addTab(tab, title)


    def handle_data(self):
        # Implements file reading here
        pass
    
    # below should be useed to handle moving on the board which has yet to be implemented
    def handle_update(self):
        pass
        
    # below must be wrapped in local fxn
    def handle_delete(self):
        self.alternate_parent.remove_self()

    def closeEvent(self, event):
        # Close the popup when its parent (main window) is closed
        self.close()
        self.alternate_parent.swap_selection()

class ImageOnCanvas(QGraphicsPixmapItem, QObject):
    # Define a custom signal
    #destroyed = pyqtSignal()

    def __init__(self, x, y, scale, rotation, image_path, parent=None, data_name:str = None, data_text:str = None):
        super(ImageOnCanvas, self).__init__()
        self.setPos(x, y)
        self.setScale(scale)
        self.setRotation(rotation)
        self.set_image(image_path)
        self.image_path = image_path
        self.selected = False
        self.parent = parent
        self.data_name = data_name
        self.data_text = data_text
        # TODO, saving Z value, needs to reorder height of images it overlaps with upon update
        # possibly ViewWindow needs to be updated
        self.z = None

    def set_image(self, image_path):
        image = QPixmap(image_path)
        self.setPixmap(image)
    
    def set_parent(self, parent):
        self.parent = parent

    #
    # TODO: Swap below to rotate around middle
    # Currently below rotates around the top left corner
    # IE the rotation of 1 would be 00 ->  10
    #                               01 ->  00
    #
    def rotate_item(self, angle, absolute=False):
        angle = float(angle)
        if absolute:
            new_rotation = angle
        else:
            current_rotation = self.rotation()
            new_rotation = current_rotation + angle
        self.setRotation(new_rotation)
    
    def scale_item(self, factor):
        current_scale = self.scale()
        new_scale = current_scale * int(factor)
        self.setScale(new_scale)
    
    def move_item(self, x, y, z=None):
        if x and y:
            self.setPos(int(x), int(y))
        if z:
            self.z = int(z)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.swap_selection()
        if (self.selected):
            self.popup = ImageControllerPopup(parent=self.parent, alternate_parent=self)
            self.popup.show()
            # Somehow we need a highlight function here
        else:
            try:
                if self.popup:
                    self.popup.closeEvent(None)
            except TypeError:
                pass
            


    def swap_selection(self):
        self.selected = not self.selected
        self.setOpacity(0.7 if self.selected else 1.0)

    def remove_self(self):
        #
        # Emit the custom destroyed signal before removing the item
        # Below cannot convert to QOBject
        # it creates errors
        #
        #self.destroyed.emit()
        self.popup.close()
        if self.parent:
            #print(self.parent)
            self.parent.removeItem(self)
    

    def save_to_LocationObject(self):
        # Need a load and edit method
        # As some LocationObjects are already saved
        location_object = LocationObject.LocationObject(
            name=self.data_name,
            data=self.data_text,
            image_path=self.image_path,
            x=self.x(),
            y=self.y(),
            rotation=self.rotation(),
            scale=self.scale()
        )
        return location_object
        
    #
    # Unnecessary currently
    #
    #def __del__(self):
    #    remove_self()
