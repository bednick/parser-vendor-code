import re

from parser_vendor_code import vendors

SERIES_PATTERN = re.compile(r"^(?P<series>[a-zA-Zа-яА-я]+)")

RU_to_EN = {
    "Е": "E",
    "Т": "T",
    "О": "O",
    "Р": "P",
    "А": "A",
    "Н": "H",
    "К": "K",
    "С": "C",
    "В": "B",
    "М": "M",
}


def normalize(value: str) -> str:
    for old_char, new_char in RU_to_EN.items():
        value = value.replace(old_char, new_char)
    return value.strip()


def get_vendor_by_request(value: str):
    match = re.match(SERIES_PATTERN, value)
    if match:
        vendor_name = match.group("series")
        if vendor_name and hasattr(vendors, vendor_name.lower()):
            return getattr(vendors, vendor_name.lower())
