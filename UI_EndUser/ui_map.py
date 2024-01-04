from qtpy.QtWidgets import QGraphicsView, QGraphicsScene
from qtpy.QtCore import Qt

class MyGraphicsView(QGraphicsView):
    def __init__(self, scene):
        super(MyGraphicsView, self).__init__(scene)
        self.setRenderHint(QGraphicsView.Antialiasing, True)
        self.setRenderHint(QGraphicsView.SmoothPixmapTransform, True)
        self.setRenderHint(QGraphicsView.HighQualityAntialiasing, True)

        # Enable scroll bar and set the transformation anchor to the center
        self.setRenderHint(QGraphicsView.Antialiasing, True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)

    def wheelEvent(self, event):
        factor = 1.2  # Zoom factor

        if event.angleDelta().y() > 0:
            # Zoom in
            self.scale(factor, factor)
        else:
            # Zoom out
            self.scale(1.0 / factor, 1.0 / factor)