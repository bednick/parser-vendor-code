CREATE TABLE IF NOT EXISTS templates (
    template_id INTEGER NOT NULL PRIMARY KEY
    , name      TEXT    NOT NULL UNIQUE
    , mask      TEXT    NOT NULL
    , value     TEXT    NOT NULL
);

CREATE TABLE IF NOT EXISTS directories (
    directory_id    INTEGER NOT NULL PRIMARY KEY
    , name          TEXT    NOT NULL UNIQUE

    , FOREIGN KEY (directory_id) REFERENCES directories (directory_id)
);

CREATE TABLE IF NOT EXISTS directory_values (
    directory_id BIGINT NOT NULL
    , key        TEXT   NOT NULL
    , value      TEXT   NOT NULL

    , PRIMARY KEY (directory_id, key)
    , FOREIGN KEY (directory_id) REFERENCES directories (directory_id)
);

CREATE TABLE IF NOT EXISTS template_keys (
    template_id           BIGINT NOT NULL
    , name                TEXT   NOT NULL
    , description         TEXT   NOT NULL
    , pattern             TEXT   NOT NULL  -- f string, default value
    , directory_id        BIGINT     NULL

    , PRIMARY KEY (template_id, name)
    , FOREIGN KEY (template_id)  REFERENCES templates (template_id)
    , FOREIGN KEY (directory_id) REFERENCES directories (directory_id)
);
