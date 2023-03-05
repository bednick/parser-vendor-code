from typing import List, NamedTuple, Optional


class Template(NamedTuple):
    template_id: int
    name: str
    mask: str
    value: str


class Directory(NamedTuple):
    directory_id: int
    name: str


class DirectoryValue(NamedTuple):
    directory_id: int
    key: str
    value: str


class TemplateKey(NamedTuple):
    template_id: int
    name: str
    description: str
    pattern: str
    directory_id: Optional[int]


Templates = List[Template]
Directories = List[Directory]
DirectoryValues = List[DirectoryValue]
TemplateKeys = List[TemplateKey]


class ParsedItem(NamedTuple):
    description: str
    raw_value: str
    parsed_value: str


ParsedItems = List[ParsedItem]
