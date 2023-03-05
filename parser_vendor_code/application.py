import logging
import sys

from PyQt5 import QtWidgets

from parser_vendor_code import database, utils, vendors
from parser_vendor_code.ui import ui_main_window

logger = logging.getLogger(__name__)


class MainWindow(QtWidgets.QMainWindow, ui_main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        utils.configure_logging()
        database.init()

        self.pushButtonParse.clicked.connect(self.parse)
        self.comboBox.currentIndexChanged.connect(self.on_combobox_changed)
        self.checkBoxAuto.stateChanged.connect(self.on_checkbox_changed)

        for vendor_template in vendors.get_all_vendors():
            self.comboBox.addItem(
                f"{vendor_template.name}: {vendor_template.mask}",
                vendor_template.template_id,
            )

    def parse(self):
        text = utils.normalize(self.lineEditInput.text())
        logger.info(f"Start text={text}")
        self.listWidget.clear()

        if self.checkBoxAuto.isChecked():
            combobox_indexes = tuple(range(self.comboBox.count()))
        else:
            combobox_indexes = (self.comboBox.currentIndex(),)

        results = None
        errors = []
        for combobox_index in combobox_indexes:
            template_id = self.comboBox.itemData(combobox_index)
            try:
                results = vendors.parse(template_id=template_id, text=text)
            except vendors.ErrorParse:
                errors.append(f"Шаблон {template_id} не распарсил строку")
                logger.warning(f"Template {template_id} not parsed {text}")
                continue
            except Exception as exc:
                logger.exception(f"Error parse template_id={template_id}, text={text}")
                errors.append(f"Непредвиденная ошибка: {exc}")
                continue
            if results:
                logger.info(f"Selected {combobox_index} index")
                self.comboBox.setCurrentIndex(combobox_index)
                for result in results:
                    widget_item = QtWidgets.QListWidgetItem(
                        f"{result.raw_value or ''}\t{result.parsed_value}"
                    )
                    self.listWidget.addItem(widget_item)
                break

        if not results and errors:
            self.listWidget.addItem(QtWidgets.QListWidgetItem("\n".join(errors)))
            self.statusbar.showMessage("; ".join(errors))

    def on_combobox_changed(self, value):
        template_id = self.comboBox.currentData()
        template = database.get_template(template_id)
        self.lineEditInput.setPlaceholderText(template.mask)

    def on_checkbox_changed(self, value):
        self.comboBox.setEnabled(not value)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
