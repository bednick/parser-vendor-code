import functools
import pathlib
import sqlite3
from typing import Any

from parser_vendor_code import models

SCRIPT_PATH = pathlib.Path(__file__).parent.parent / "sqlite"


def init():
    executescript(str(SCRIPT_PATH / "tables.sql"))
    executescript(str(SCRIPT_PATH / "data.sql"))


@functools.lru_cache(maxsize=None)
def connect() -> sqlite3.Connection:
    return sqlite3.connect(":memory:")


def executescript(filename: str) -> Any:
    request = pathlib.Path(filename).read_text("utf-8").strip()
    with connect() as connection:
        with connection as cursor:
            cursor.executescript(request)
            cursor.commit()


def get_templates() -> models.Templates:
    with connect() as connection:
        with connection as cursor:
            results = cursor.execute(
                "SELECT template_id, name, mask, value FROM templates"
            )
            return [models.Template(*result) for result in results]


def get_template(template_id: int) -> models.Template:
    with connect() as connection:
        with connection as cursor:
            results = cursor.execute(
                "SELECT template_id, name, mask, value FROM templates WHERE template_id = ?",
                (template_id,),
            )
            return models.Template(*next(results))


def get_template_keys(template_id: int) -> models.TemplateKeys:
    with connect() as connection:
        with connection as cursor:
            results = cursor.execute(
                "SELECT template_id, name, description, pattern, directory_id FROM template_keys WHERE template_id = ?",
                (template_id,),
            )
            return [models.TemplateKey(*result) for result in results]


def get_directory_values(directory_id: int) -> models.DirectoryValues:
    with connect() as connection:
        with connection as cursor:
            results = cursor.execute(
                "SELECT directory_id, key, value FROM directory_values WHERE directory_id = ?",
                (directory_id,),
            )
            return [models.DirectoryValue(*result) for result in results]
