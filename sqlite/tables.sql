CREATE TABLE IF NOT EXISTS templates (
    template_id TEXT NOT NULL PRIMARY KEY
    , name      TEXT NOT NULL UNIQUE
    , mask      TEXT NOT NULL
    , value     TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS directories (
    directory_id TEXT NOT NULL PRIMARY KEY
    , name       TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS directory_values (
    directory_id TEXT NOT NULL
    , key        TEXT NOT NULL
    , value      TEXT NOT NULL

    , PRIMARY KEY (directory_id, key)
    , FOREIGN KEY (directory_id) REFERENCES directories (directory_id)
);

CREATE TABLE IF NOT EXISTS template_keys (
    template_id     TEXT NOT NULL
    , name          TEXT NOT NULL
    , description   TEXT NOT NULL
    , pattern       TEXT NOT NULL  -- f string
    , default_value TEXT NOT NULL  -- default value - if key value in None
    , directory_id  TEXT     NULL

    , PRIMARY KEY (template_id, name)
    , FOREIGN KEY (template_id)  REFERENCES templates (template_id)
    , FOREIGN KEY (directory_id) REFERENCES directories (directory_id)
);
