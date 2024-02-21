
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
            # Somehow we need a highlight function here
            self.setOpacity(0.7 if self.selected else 1.0)