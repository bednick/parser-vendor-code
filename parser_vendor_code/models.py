import dataclasses
import logging
import re
from typing import Dict, Optional, Sequence

from PyQt5 import QtCore, QtGui

from parser_vendor_code import ulid

logger = logging.getLogger(__name__)


@dataclasses.dataclass()
class Directory:
    directory_id: int
    name: str


@dataclasses.dataclass()
class DirectoryValue:
    directory_id: int
    key: str
    value: str


class Directories(QtCore.QAbstractTableModel):
    def __init__(self, parent=None, *, directories: Sequence[Directory]):
        super().__init__(parent)
        self.columns = ("directory_id", "name")
        self.directories = directories

    def rowCount(self, parent=None):
        return len(self.directories)

    def columnCount(self, parent=None):
        return len(self.columns)

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.columns[section].title()

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
            return getattr(self.directories[index.row()], self.columns[index.column()])
        else:
            return None

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if not index.isValid() or role != QtCore.Qt.EditRole:
            return False
        if self.directories:
            setattr(self.directories[index.row()], self.columns[index.column()], value)
            self.dataChanged.emit(index, index, [])
            return True
        return True


DirectoryValues = Sequence[DirectoryValue]


@dataclasses.dataclass()
class ParsedItem:
    description: str
    raw_value: str
    parsed_value: str


ParsedItems = Sequence[ParsedItem]


class TemplateKey(QtGui.QStandardItemModel):
    def __init__(
        self,
        template_id: str,
        name: str,
        description: str = "",
        pattern: str = "{value}",
        default_value: str = "",
        directory_id: str = "",
    ):
        super().__init__()
        self.appendRow(
            (
                QtGui.QStandardItem(template_id),
                QtGui.QStandardItem(name),
                QtGui.QStandardItem(description),
                QtGui.QStandardItem(pattern),
                QtGui.QStandardItem(default_value),
                QtGui.QStandardItem(directory_id),
            )
        )

    @property
    def template_id(self) -> str:
        return self.data(self.index(0, 0))

    @property
    def name(self) -> str:
        return self.data(self.index(0, 1)).strip()

    @property
    def description(self) -> str:
        return self.data(self.index(0, 2)).strip()

    @property
    def pattern(self) -> str:
        return self.data(self.index(0, 3)).strip()

    @property
    def default_value(self) -> Optional[str]:
        return self.data(self.index(0, 4)).strip()

    @property
    def directory_id(self) -> Optional[str]:
        return self.data(self.index(0, 5))


TemplateKeys = Sequence[TemplateKey]


class Template(QtGui.QStandardItemModel):
    keysUpdated = QtCore.pyqtSignal()

    def __init__(
        self,
        template_id: Optional[str] = None,
        name: str = "",
        mask: str = "",
        value: str = "",
        keys: TemplateKeys = None,
    ):
        super().__init__()

        keys_by_name = {}
        for key in keys or ():
            keys_by_name[key.name] = key

        self.keys_by_name: Dict[str, TemplateKey] = keys_by_name
        self._history_keys: Dict[str, TemplateKey] = keys_by_name
        self._value_item = QtGui.QStandardItem(value)
        self.appendRow(
            (
                QtGui.QStandardItem(str(template_id or ulid.ulid())),
                QtGui.QStandardItem(name),
                QtGui.QStandardItem(mask),
                self._value_item,
            )
        )
        self.parse_value(value)
        self.itemChanged.connect(self.data_updated)

    @property
    def template_id(self) -> str:
        return self.data(self.index(0, 0))

    @property
    def name(self) -> str:
        return self.data(self.index(0, 1))

    @property
    def mask(self) -> str:
        return self.data(self.index(0, 2))

    @property
    def value(self) -> str:
        return self.data(self.index(0, 3))

    @property
    def keys(self) -> Sequence[TemplateKey]:
        return list(self.keys_by_name.values())

    def parse_value(self, value: str):
        old_keys = self.keys_by_name
        self.keys_by_name = {}
        try:
            pattern = re.compile(value)
        except Exception as exc:
            logger.warning(f"Error parse regex: {exc}")
            return

        for name in pattern.groupindex.keys():
            model = self._history_keys.get(name)
            if not model:
                model = TemplateKey(template_id=self.template_id, name=name)
                self._history_keys[name] = model

            self.keys_by_name[name] = model
        if old_keys != self.keys_by_name:
            self.keysUpdated.emit()

    def data_updated(self, item: QtGui.QStandardItem):
        if item == self._value_item:
            self.parse_value(item.text())


Templates = Sequence[Template]
