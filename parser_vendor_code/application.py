import sys

from PyQt5 import QtWidgets

from parser_vendor_code import vendors, utils
from parser_vendor_code.ui import ui_main_window


class MainWindow(QtWidgets.QMainWindow, ui_main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButtonParse.clicked.connect(self.parse)
        self.comboBox.addItem("MC", vendors.mc)

    def parse(self):
        text = utils.normalize(self.lineEditInput.text())
        self.listWidget.clear()

        if not self.comboBox.currentIndex():
            vendor = utils.get_vendor_by_request(text)
            if not vendor:
                message = "vendor not found"
                self.listWidget.addItem(QtWidgets.QListWidgetItem(message))
                self.statusbar.showMessage(message)
                return
        else:
            vendor = self.comboBox.currentData()

        try:
            results = vendor.parse(text)
        except Exception as exc:
            message = f"ERROR parse {exc}"
            self.listWidget.addItem(QtWidgets.QListWidgetItem(message))
            self.statusbar.showMessage(message)
            return
        if results:
            for result in results:
                widget_item = QtWidgets.QListWidgetItem(
                    f"{result.value or '':<4} - {result.description}"
                )
                self.listWidget.addItem(widget_item)
        else:
            message = f"VENDOR {vendor.__name__} NOT PARSED"
            self.statusbar.showMessage(message)
            self.listWidget.addItem(QtWidgets.QListWidgetItem(message))


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
