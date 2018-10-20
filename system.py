import sys


from PyQt5.QtWidgets import QApplication, QWidget, QGraphicsView, QGraphicsScene, QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QBrush, QColor



class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initUi()
        
        self.show()
    
    
    def initUi(self):
        
        
        layout = QGridLayout()
        
        graphics_view = QGraphicsView()
        layout.addWidget(graphics_view)
        
        width = graphics_view.frameGeometry().width()
        height = graphics_view.frameGeometry().height()
        
        scene = QGraphicsScene()
        scene.setSceneRect(0.0, 0.0, float(width), float(height))
        
        scene.addRect(100, 100, 150, 150)
        
        pen = QPen(Qt.SolidLine)
        pen.setColor(Qt.red)
        brush = QBrush(Qt.Dense3Pattern)
        brush.setColor(Qt.darkGreen)
        scene.addEllipse(300, 300, 100, 100, pen, brush)
        
        graphics_view.setScene(scene)
        
        self.setLayout(layout)





def main(args):
    
    app = QApplication(args)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)