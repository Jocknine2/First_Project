PRAGMA FOREIGN_KEYS = ON;

DROP TABLE shop;
DROP TABLE manufacturers;
DROP TABLE guitars;

CREATE TABLE manufacturers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company VARCHAR
);

CREATE TABLE guitars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    model VARCHAR,
    body shape VARCHAR,
    build_price INTEGER,
    retail_price INTEGER,
    details VARCHAR

);

CREATE TABLE shop (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    manufacturer_id INTEGER NOT NULL,
    guitar_id INTEGER NOT NULL,
        FOREIGN KEY (guitar_id)
            REFERENCES guitars(id) ON DELETE CASCADE,
        FOREIGN KEY (manufacturer_id)
            REFERENCES manufacturers(id) ON DELETE CASCADE
);