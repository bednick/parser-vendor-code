import logging

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QModelIndex, Qt
from PyQt5.QtSql import QSqlTableModel

from parser_vendor_code import database, models
from parser_vendor_code.ui import ui_template, ui_template_item, ui_templates

logger = logging.getLogger(__name__)


class DialogTemplates(QtWidgets.QDialog, ui_templates.Ui_DialogTemplates):
    def __init__(self, parent=None, *, directories: models.Directories):
        super().__init__(parent)
        self.setupUi(self)
        self.directories = directories

        self.model = QSqlTableModel(self)
        self.model.setTable("templates")
        self.model.sort(0, Qt.AscendingOrder)
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.model.setHeaderData(1, Qt.Horizontal, "Название")
        self.model.setHeaderData(2, Qt.Horizontal, "Маска")
        self.model.setHeaderData(3, Qt.Horizontal, "Шаблон")
        self.model.select()
        # Set up the view
        self.tableViewTemplates.setModel(self.model)
        self.tableViewTemplates.doubleClicked.connect(self.update_template)
        # self.tableViewTemplates.resizeColumnsToContents()

        self.pushButtonNew.clicked.connect(self.create_new_template)

    def create_new_template(self):
        dialog = DialogUpsertTemplate(self, directories=self.directories)
        if dialog.exec():
            new_template = dialog.template
            database.upsert_template(new_template)
            self.model.select()

    def update_template(self, index: QModelIndex):
        template_id = index.siblingAtColumn(0).data()
        template = database.get_template(template_id)
        dialog = DialogUpsertTemplate(
            self, template=template, directories=self.directories
        )
        if dialog.exec():
            new_template = dialog.template
            database.upsert_template(new_template)
            self.model.select()


class ComboUserDataDelegate(QtWidgets.QItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def setEditorData(self, editor: QtWidgets.QWidget, index: QModelIndex) -> None:
        if not isinstance(editor, QtWidgets.QComboBox):
            return QtWidgets.QItemDelegate.setEditorData(self, editor, index)

        index.model()
        data = index.data(Qt.EditRole)
        if not data:
            return
        editor: QtWidgets.QComboBox
        items_data = [editor.itemData(i) for i in range(editor.count())]
        if data not in items_data:
            raise ValueError(f"ComboBox {editor} has no data {data}")

        editor.setProperty("currentIndex", items_data.index(data))
        return

    def setModelData(
        self,
        editor: QtWidgets.QWidget,
        model: QtCore.QAbstractItemModel,
        index: QModelIndex,
    ) -> None:
        if not isinstance(editor, QtWidgets.QComboBox):
            return QtWidgets.QItemDelegate.setModelData(self, editor, model, index)

        editor: QtWidgets.QComboBox
        data = editor.currentData()
        model.setData(index, data, Qt.EditRole)
        return


def do_nothing(*args, **kwargs):
    pass


class WidgetTemplateItem(QtWidgets.QWidget, ui_template_item.Ui_WidgetTemplateItem):
    def __init__(
        self, parent=None, *, model: models.TemplateKey, directories: models.Directories
    ):
        super().__init__(parent)
        self.setupUi(self)
        # Чтобы comboBox не прокручивался от колесика мыши
        self.comboBoxDirectories.wheelEvent = do_nothing
        for directory in directories.directories:
            self.comboBoxDirectories.addItem(directory.name, directory.directory_id)
        self.mapper = QtWidgets.QDataWidgetMapper()
        self.mapper.setModel(model)
        self.mapper.setItemDelegate(ComboUserDataDelegate(self))
        self.mapper.addMapping(self.lineEditName, 1)
        self.mapper.addMapping(self.lineEditDescription, 2)
        self.mapper.addMapping(self.lineEditPattern, 3)
        self.mapper.addMapping(self.lineEditDefault, 4)
        self.mapper.addMapping(self.comboBoxDirectories, 5)
        self.mapper.toFirst()
        self.tabWidget.setCurrentIndex(int(bool(model.directory_id)))


class DialogUpsertTemplate(QtWidgets.QDialog, ui_template.Ui_DialogUpsertTemplate):
    def __init__(
        self,
        parent=None,
        *,
        template: models.Template = None,
        directories: models.Directories,
    ):
        super().__init__(parent)
        self.setupUi(self)
        self.directories = directories
        self.template = template or models.Template()
        self.mapper = QtWidgets.QDataWidgetMapper()
        self.mapper.setModel(self.template)
        self.mapper.addMapping(self.lineEditName, 1)
        self.mapper.addMapping(self.lineEditMask, 2)
        self.mapper.addMapping(self.textEditValue, 3, b"plainText")
        self.mapper.toFirst()

        self.template_keys_updated()
        self.template.keysUpdated.connect(self.template_keys_updated)

    def template_keys_updated(self):
        self.listWidgetTemplateItems.clear()
        for key_model in self.template.keys:
            template = WidgetTemplateItem(model=key_model, directories=self.directories)
            template.setAutoFillBackground(True)

            item = QtWidgets.QListWidgetItem(self.listWidgetTemplateItems)
            item.setSizeHint(template.sizeHint())

            self.listWidgetTemplateItems.addItem(item)
            self.listWidgetTemplateItems.setItemWidget(item, template)
