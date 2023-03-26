import logging

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QModelIndex, Qt
from PyQt5.QtSql import QSqlTableModel

from parser_vendor_code import database, models
from parser_vendor_code.ui import (
    ui_directories,
    ui_directory_update,
    ui_new_directory,
    ui_new_directory_value,
    ui_template,
    ui_template_item,
    ui_templates,
)

logger = logging.getLogger(__name__)


class DialogDeleteObject(QtWidgets.QMessageBox):
    def __init__(self, parent=None, *, object_name: str):
        super().__init__(parent)
        self.setWindowTitle("Удаление объекта")
        self.setText(f"Вы действительно хотите удалить: {object_name}")
        self.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        self.setIcon(QtWidgets.QMessageBox.Question)


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
        self.pushButtonDelete.clicked.connect(self.delete_template)

        select = self.tableViewTemplates.selectionModel()
        select.selectionChanged.connect(self.selection_changed)

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

    def selection_changed(
        self, selected: QtCore.QItemSelection, deselected: QtCore.QItemSelection
    ):
        self.pushButtonDelete.setEnabled(bool(selected.count()))

    def delete_template(self):
        select = self.tableViewTemplates.selectionModel()
        if select.hasSelection():
            index = select.selectedIndexes()[0]
            model = index.model()
            object_name = model.data(model.index(index.row(), 1))
            if (
                DialogDeleteObject(object_name=object_name).exec()
                == QtWidgets.QMessageBox.Yes
            ):
                self.model.deleteRowFromTable(index.row())
                self.model.select()
        else:
            self.pushButtonDelete.setEnabled(False)


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
            logger.error(f"ComboBox {editor} has no data {data}")
            editor.setProperty("currentIndex", 0)
            return

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
        self.groupBox.setTitle(model.name)
        self.mapper = QtWidgets.QDataWidgetMapper()
        self.mapper.setModel(model)
        self.mapper.setItemDelegate(ComboUserDataDelegate(self))
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
        self.mapper.addMapping(self.lineEditID, 0)
        self.mapper.addMapping(self.lineEditName, 1)
        self.mapper.addMapping(self.lineEditMask, 2)
        self.mapper.addMapping(self.textEditValue, 3, b"plainText")
        self.mapper.toFirst()

        self.template_keys_updated()
        self.template.keysUpdated.connect(self.template_keys_updated)

    def template_keys_updated(self):
        self.listWidgetTemplateItems.clear()
        for index, key_model in enumerate(self.template.keys):
            widget = WidgetTemplateItem(model=key_model, directories=self.directories)
            item = QtWidgets.QListWidgetItem(self.listWidgetTemplateItems)
            item.setSizeHint(widget.sizeHint())

            self.listWidgetTemplateItems.addItem(item)
            self.listWidgetTemplateItems.setItemWidget(item, widget)


class DialogNewDirectory(QtWidgets.QDialog, ui_new_directory.Ui_DialogNewDirectory):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class DialogNewDirectoryValue(
    QtWidgets.QDialog, ui_new_directory_value.Ui_DialogNewDirectoryValue
):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class DialogDirectoryUpdate(
    QtWidgets.QDialog, ui_directory_update.Ui_DialogDirectoryUpdate
):
    def __init__(self, parent=None, *, directory_id: str):
        super().__init__(parent)
        self.setupUi(self)
        self.directory_id = directory_id

        self.directory_model = QSqlTableModel(self)
        self.directory_model.setTable("directories")
        self.directory_model.setFilter(f"directory_id='{directory_id}'")
        self.directory_model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.directory_model.select()

        self.mapper = QtWidgets.QDataWidgetMapper()
        self.mapper.setModel(self.directory_model)
        self.mapper.addMapping(self.lineEditID, 0)
        self.mapper.addMapping(self.lineEditName, 1)
        self.mapper.toFirst()

        self.model = QSqlTableModel(self)
        self.model.setTable("directory_values")
        self.model.setSort(1, Qt.AscendingOrder)
        self.model.setFilter(f"directory_id='{directory_id}'")
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)

        self.model.setHeaderData(0, Qt.Horizontal, "directory id")
        self.model.setHeaderData(1, Qt.Horizontal, "Ключ")
        self.model.setHeaderData(2, Qt.Horizontal, "Значение")
        self.model.select()
        # Set up the view
        self.tableViewDirectoryValues.setModel(self.model)
        self.tableViewDirectoryValues.resizeColumnsToContents()
        self.tableViewDirectoryValues.setColumnHidden(0, True)

        self.pushButtonNew.clicked.connect(self.create_new_directory_value)
        self.pushButtonDelete.clicked.connect(self.delete_directory_value)

        select = self.tableViewDirectoryValues.selectionModel()
        select.selectionChanged.connect(self.selection_changed)

    def create_new_directory_value(self):
        dialog = DialogNewDirectoryValue(self)
        if dialog.exec():
            key = dialog.lineEditKey.text().strip()
            value = dialog.lineEditValue.text().strip()
            directory_value = models.DirectoryValue(
                self.directory_id, key=key, value=value
            )
            database.upsert_directory_value(directory_value)
            self.model.select()

    def delete_directory_value(self):
        select = self.tableViewDirectoryValues.selectionModel()
        if select.hasSelection():
            index = select.selectedIndexes()[0]
            model = index.model()
            object_name = model.data(model.index(index.row(), 1))
            if (
                DialogDeleteObject(object_name=object_name).exec()
                == QtWidgets.QMessageBox.Yes
            ):
                self.model.deleteRowFromTable(index.row())
                self.model.select()
        else:
            self.pushButtonDelete.setEnabled(False)

    def selection_changed(
        self, selected: QtCore.QItemSelection, deselected: QtCore.QItemSelection
    ):
        self.pushButtonDelete.setEnabled(bool(selected.count()))


class DialogDirectories(QtWidgets.QDialog, ui_directories.Ui_DialogDirectories):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.model = QSqlTableModel(self)
        self.model.setTable("directories")
        self.model.sort(0, Qt.AscendingOrder)
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.model.setHeaderData(1, Qt.Horizontal, "Название")
        self.model.select()
        # Set up the view
        self.tableViewDirectories.setModel(self.model)
        self.tableViewDirectories.doubleClicked.connect(self.update_directory)
        self.tableViewDirectories.resizeColumnsToContents()

        self.pushButtonNew.clicked.connect(self.create_new_directory)
        self.pushButtonDelete.clicked.connect(self.delete_directory)

        select = self.tableViewDirectories.selectionModel()
        select.selectionChanged.connect(self.selection_changed)

    def update_directory(self, index: QModelIndex):
        directory_id = index.siblingAtColumn(0).data()
        dialog = DialogDirectoryUpdate(self, directory_id=directory_id)
        if dialog.exec():
            self.model.select()

    def create_new_directory(self):
        dialog = DialogNewDirectory(self)
        if dialog.exec():
            new_name = dialog.lineEditName.text().strip()
            if new_name:
                database.upsert_directory(models.Directory(name=new_name))
                self.model.select()

    def delete_directory(self):
        select = self.tableViewDirectories.selectionModel()
        if select.hasSelection():
            index = select.selectedIndexes()[0]
            model = index.model()
            object_name = model.data(model.index(index.row(), 1))
            if (
                DialogDeleteObject(object_name=object_name).exec()
                == QtWidgets.QMessageBox.Yes
            ):
                self.model.deleteRowFromTable(index.row())
                self.model.select()
        else:
            self.pushButtonDelete.setEnabled(False)

    def selection_changed(
        self, selected: QtCore.QItemSelection, deselected: QtCore.QItemSelection
    ):
        self.pushButtonDelete.setEnabled(bool(selected.count()))
