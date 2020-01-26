# ------------------------------------------------------
# -------------------- mplwidget.py --------------------
# ------------------------------------------------------
from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D  # <-- Note the capitalization!
from matplotlib.figure import Figure


class MplWidget2dmorf(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.canvas = FigureCanvas(Figure())
        self.canvas2 = FigureCanvas(Figure())

        vertical_layout = QVBoxLayout()
        horizontal_layoutPlot = QHBoxLayout()
        horizontal_layoutToolBars = QHBoxLayout()
        horizontal_layoutLabels = QHBoxLayout()
        Label = QLabel()
        Label.setText("Before Morphology")
        Label.setStyleSheet("font: 16pt Arial")
        horizontal_layoutLabels.addWidget(Label)
        Label = QLabel()
        Label.setText("After Morphology")
        Label.setStyleSheet("font: 16pt Arial")
        horizontal_layoutLabels.addWidget(Label)

        self.navi_toolbar = NavigationToolbar(self.canvas, self)
        self.canvas.axes = self.canvas.figure.add_subplot(111)

        self.navi_toolbar2 = NavigationToolbar(self.canvas2, self)
        self.canvas2.axes = self.canvas2.figure.add_subplot(111)

        horizontal_layoutPlot.addWidget(self.canvas)
        horizontal_layoutPlot.addWidget(self.canvas2)

        horizontal_layoutToolBars.addWidget(self.navi_toolbar)
        horizontal_layoutToolBars.addWidget(self.navi_toolbar2)

        vertical_layout.addLayout(horizontal_layoutLabels)
        vertical_layout.addLayout(horizontal_layoutPlot)
        vertical_layout.addLayout(horizontal_layoutToolBars)

        self.setLayout(vertical_layout)


