import functools
import pathlib
import sqlite3
from typing import Any

from PyQt5 import QtSql

from parser_vendor_code import models

DATABASE_PATH = str(
    pathlib.Path.home() / ".parser-vendor-code" / "parser-vendor-code.sqlite"
)
SCRIPT_PATH = pathlib.Path(__file__).parent.parent / "sqlite"


def init():
    executescript(str(SCRIPT_PATH / "tables.sql"))
    try:
        executescript(str(SCRIPT_PATH / "data.sql"))
    except Exception:
        pass
    con = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName(DATABASE_PATH)


if DATABASE_PATH == ":memory":

    @functools.lru_cache(maxsize=None)
    def connect() -> sqlite3.Connection:
        return sqlite3.connect(":memory:")

else:

    def connect() -> sqlite3.Connection:
        return sqlite3.connect(DATABASE_PATH)


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
                "SELECT template_id, name, mask, value FROM templates ORDER BY template_id"
            )
            return [models.Template(*result) for result in results]


def get_template(template_id: int) -> models.Template:
    with connect() as connection:
        with connection as cursor:
            results_template = cursor.execute(
                "SELECT template_id, name, mask, value FROM templates WHERE template_id = ?",
                (template_id,),
            )
            results_keys = cursor.execute(
                """
                SELECT template_id, name, description, pattern, default_value, directory_id
                FROM template_keys WHERE template_id = ?
                """,
                (template_id,),
            )
            keys = [models.TemplateKey(*result) for result in results_keys]

            return models.Template(*next(results_template), keys=keys)


def get_directories() -> models.Directories:
    with connect() as connection:
        with connection as cursor:
            results = cursor.execute(
                "SELECT directory_id, name FROM directories ORDER BY directory_id"
            )
            return models.Directories(
                directories=[models.Directory(*result) for result in results]
            )


def get_directory_values(directory_id: str) -> models.DirectoryValues:
    with connect() as connection:
        with connection as cursor:
            results = cursor.execute(
                "SELECT directory_id, key, value FROM directory_values WHERE directory_id = ?",
                (directory_id,),
            )
            return [models.DirectoryValue(*result) for result in results]


def upsert_template(template: models.Template):
    with connect() as connection:
        with connection as cursor:
            cursor.execute(
                """
                INSERT OR REPLACE INTO templates (template_id, name, mask, value)
                VALUES (?, ?, ?, ?);
                """,
                (template.template_id, template.name, template.mask, template.value),
            )
            if template.keys:
                cursor.executemany(
                    """
                    INSERT OR REPLACE INTO
                    template_keys (template_id, name, description, pattern, default_value, directory_id)
                    VALUES (?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            key.template_id,
                            key.name,
                            key.description,
                            key.pattern,
                            key.default_value,
                            key.directory_id,
                        )
                        for key in template.keys
                    ],
                )
