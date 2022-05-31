from db.run_sql import run_sql
from models.guitar import Guitar
from models.manufacturer import Manufacturer


def save(guitar):

    sql = "INSERT INTO guitars(model, body, build_price, retail_price, details) VALUES ( ?, ?, ?, ?, ? ) RETURNING id"
    values = [
        guitar.model,
        guitar.body,
        guitar.build_price,
        guitar.retail_price,
        guitar.details,
    ]
    results = run_sql(sql, values)
    guitar.id = results[0]["id"]
    return guitar


def select_all():
    guitars = []

    sql = "SELECT * FROM guitars"
    results = run_sql(sql)
    for row in results:
        guitar = Guitar(
            row["model"],
            row["body"],
            row["build_price"],
            row["retail_price"],
            row["details"],
            row["id"],
        )
        guitars.append(guitar)
    return guitars


def select(id):
    guitar = None
    sql = "SELECT * FROM guitars WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        guitar = Guitar(
            result["model"],
            result["body"],
            result["build_price"],
            result["retail_price"],
            result["details"],
            result["id"],
        )
    return guitar


def delete_all():
    sql = "DELETE FROM guitars"
    run_sql(sql)


def manufacturers(guitar):
    manufacturers = []

    sql = "SELECT manufacturers.* FROM manufacturers INNER JOIN shop ON manufacturers.id = shop.manufacturer_id WHERE guitar_id = ?"
    values = [guitar.id]
    results = run_sql(sql, values)

    for row in results:
        manufacturer = Manufacturer(row["company"], row["id"])
        manufacturers.append(manufacturer)

    return manufacturers
