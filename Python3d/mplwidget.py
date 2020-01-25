from PyQt5.QtWidgets import*

from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from matplotlib.figure import Figure        
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D

    
class MplWidget(QWidget):
    
    def __init__(self, parent = None):

        QWidget.__init__(self, parent)
        
        self.canvas = FigureCanvas(Figure())
        
        vertical_layout = QVBoxLayout()
        self.navi_toolbar = NavigationToolbar(self.canvas, self)
        vertical_layout.addWidget(self.canvas)
        vertical_layout.addWidget(self.navi_toolbar)
        
        self.canvas.axes = self.canvas.figure.add_subplot(111, projection='3d')
        self.setLayout(vertical_layout)
        
