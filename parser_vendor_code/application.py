import sys

from PyQt5 import QtWidgets

from parser_vendor_code import database, utils, vendors
from parser_vendor_code.ui import ui_main_window


class MainWindow(QtWidgets.QMainWindow, ui_main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        database.init()

        self.pushButtonParse.clicked.connect(self.parse)
        self.comboBox.currentIndexChanged.connect(self.on_combobox_changed)

        for vendor_template in vendors.get_all_vendors():
            self.comboBox.addItem(
                f"{vendor_template.name}: {vendor_template.mask}",
                vendor_template.template_id,
            )

    def parse(self):
        text = utils.normalize(self.lineEditInput.text())
        self.listWidget.clear()
        template_id = self.comboBox.currentData()
        try:
            results = vendors.parse(template_id=template_id, text=text)
        except Exception as exc:
            message = f"ERROR parse {exc}"
            self.listWidget.addItem(QtWidgets.QListWidgetItem(message))
            self.statusbar.showMessage(message)
            return

        if results:
            for result in results:
                widget_item = QtWidgets.QListWidgetItem(
                    f"{result.raw_value or ''}\t{result.parsed_value}"
                )
                self.listWidget.addItem(widget_item)

    def on_combobox_changed(self, value):
        template_id = self.comboBox.currentData()
        template = database.get_template(template_id)
        self.lineEditInput.setPlaceholderText(template.mask)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
