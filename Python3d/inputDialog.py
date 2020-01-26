from PyQt5.QtWidgets import *


class InputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.first = QSpinBox(self)
        self.second = QComboBox(self)
        self.second.addItem("Circle")
        self.second.addItem("Square")
        self.second.addItem("Diamond")
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self);

        layout = QFormLayout(self)
        layout.addRow("size", self.first)
        layout.addRow("type", self.second)
        layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def getInputs(self):
        return (self.first.value(), self.second.currentIndex())