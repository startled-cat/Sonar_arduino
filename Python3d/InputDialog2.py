from PyQt5.QtWidgets import *


class InputDialog2(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.first = QSpinBox(self)
        self.second = QComboBox(self)
        self.second.addItem("Circle")
        self.second.addItem("Square")
        self.second.addItem("Diamond")

        label = QLabel()
        label.setText("Morphology parameters")

        label2 = QLabel()
        label2.setText("Approximation parameters")
        self.third = QSpinBox(self)
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self);

        Vlayout = QVBoxLayout(self)
        Hlayout = QHBoxLayout()
        Hlayout2 = QHBoxLayout()
        Hlayout.addWidget(label)
        Hlayout2.addWidget(label2)
        layout = QFormLayout()
        layout2 = QFormLayout()
        layout.addRow("size", self.first)
        layout.addRow("type", self.second)
        layout2.addRow("radius", self.third)
        layout2.addWidget(buttonBox)
        Vlayout.addLayout(Hlayout)
        Vlayout.addLayout(layout)
        Vlayout.addLayout(Hlayout2)
        Vlayout.addLayout(layout2)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def getInputs(self):
        return (self.first.value(), self.second.currentIndex(), self.third.value())