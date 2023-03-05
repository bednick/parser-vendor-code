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
