import logging
import sys

from PyQt5 import QtWidgets

from parser_vendor_code import database, dialogs, utils, vendors
from parser_vendor_code.ui import ui_main_window

logger = logging.getLogger(__name__)


class MainWindow(QtWidgets.QMainWindow, ui_main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        utils.configure_logging()
        database.init()

        self.pushButtonParse.clicked.connect(self.parse)
        self.actionTemplates.triggered.connect(self.get_all_templates)
        self.actionDirectories.triggered.connect(self.get_all_directories)
        self.actionLocalPath.triggered.connect(utils.open_localdir)
        self.comboBox.currentIndexChanged.connect(self.on_combobox_changed)
        self.checkBoxAuto.stateChanged.connect(self.on_checkbox_changed)
        self.upsert_combobox()

    def parse(self):
        text = utils.normalize(self.lineEditInput.text())
        logger.info(f"Start text={text}")
        self.statusbar.showMessage("")
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        if not text:
            return

        if self.checkBoxAuto.isChecked():
            combobox_indexes = tuple(range(self.comboBox.count()))
        else:
            combobox_indexes = (self.comboBox.currentIndex(),)

        results = None
        for combobox_index in combobox_indexes:
            template_id = self.comboBox.itemData(combobox_index)
            template = database.get_template(template_id)
            try:
                results = vendors.parse(template=template, text=text)
            except vendors.ErrorParse:
                logger.warning(f"Template {template_id} not parsed {text}")
                continue
            except Exception:
                logger.exception(f"Error parse template_id={template_id}, text={text}")
                continue
            if results:
                logger.info(f"Selected {combobox_index} index")
                self.comboBox.setCurrentIndex(combobox_index)
                self.statusbar.showMessage(
                    f"Строка распаршена с помощью шаблона '{template.name}'"
                )
                self.tableWidget.setRowCount(len(results))
                for row, result in enumerate(results):
                    self.tableWidget.setItem(
                        row, 0, QtWidgets.QTableWidgetItem(result.description)
                    )
                    self.tableWidget.setItem(
                        row, 1, QtWidgets.QTableWidgetItem(result.raw_value)
                    )
                    self.tableWidget.setItem(
                        row, 2, QtWidgets.QTableWidgetItem(result.parsed_value)
                    )

                self.tableWidget.resizeColumnsToContents()
                break

        if not results:
            self.statusbar.showMessage("Строку не удалось распарсить")

    def upsert_combobox(self):
        index = self.comboBox.currentIndex()
        self.comboBox.clear()
        for template in database.get_templates():
            self.comboBox.addItem(f"{template.name}", template.template_id)
        if index >= 0:
            self.comboBox.setCurrentIndex(index)

    def get_all_templates(self):
        directories = database.get_directories()
        dialog = dialogs.DialogTemplates(self, directories=directories)
        if dialog.exec():
            pass
        self.upsert_combobox()

    def get_all_directories(self):
        dialog = dialogs.DialogDirectories(self)
        if dialog.exec():
            pass

    def on_combobox_changed(self, value):
        if value < 0:
            return
        template_id = self.comboBox.currentData()
        template = database.get_template(template_id)
        self.lineEditInput.setPlaceholderText(template.mask)

    def on_checkbox_changed(self, value):
        self.comboBox.setEnabled(not value)


def excepthook(exc_type, exc_value, exc_tb):
    import traceback

    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("error catched!:")
    print("error message:\n", tb)
    QtWidgets.QApplication.quit()


sys.excepthook = excepthook


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
