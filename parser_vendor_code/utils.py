import logging
import pathlib

RU_to_EN = {
    "Е": "E",
    "Т": "T",
    "О": "O",
    "Р": "P",
    "А": "A",
    "Н": "H",
    "К": "K",
    "Х": "X",
    "С": "C",
    "В": "B",
    "М": "M",
}


def normalize(value: str) -> str:
    value = value.upper()
    for old_char, new_char in RU_to_EN.items():
        value = value.replace(old_char, new_char)
    return value.strip()


def configure_logging():
    file = pathlib.Path.home() / ".parser-vendor-code" / "parser-vendor-code.log"
    file.parent.mkdir(exist_ok=True)
    logging.basicConfig(
        filename=str(file.absolute()), encoding="utf-8", level=logging.DEBUG
    )
