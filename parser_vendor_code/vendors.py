import collections
import functools
import re
from typing import Dict

from parser_vendor_code import database, models


class ErrorParse(ValueError):
    pass


def get_all_vendors() -> models.Templates:
    return database.get_templates()


@functools.cache
def get_pattern(value: str):
    return re.compile(value)


def parse(text: str, template_id: int) -> models.ParsedItems:
    template = database.get_template(template_id)
    pattern = get_pattern(template.value)
    match = re.match(pattern, text)
    if not match:
        raise ErrorParse(f"use template '{template.name}'")

    template_key_by_name: Dict[str, models.TemplateKey] = {
        template_key.name: template_key
        for template_key in database.get_template_keys(template_id)
    }
    directories_by_name: Dict[str, Dict[str, str]] = collections.defaultdict(dict)
    for name, template_key in template_key_by_name.items():
        if template_key.directory_id:
            directory_values = database.get_directory_values(template_key.directory_id)
            for directory_value in directory_values:
                directories_by_name[name][directory_value.key] = directory_value.value

    results = []
    for name in pattern.groupindex.keys():
        value = match.group(name)
        template_key = template_key_by_name[name]
        pattern = template_key.pattern
        if not value:
            continue

        directory = directories_by_name.get(name)
        if directory:
            pattern = directory.get(value) or "!Не удалось найти данные в справочнике!"

        results.append(
            models.ParsedItem(
                description=template_key.description,
                raw_value=value,
                parsed_value=pattern.format(value=value),
            )
        )
    return results
