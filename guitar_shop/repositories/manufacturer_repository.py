from re import M
from db.run_sql import run_sql
from models.manufacturer import Manufacturer
from models.guitar import Guitar


def save(manufacturer):

    sql = "INSERT INTO manufacturers( company ) VALUES ( ? ) RETURNING id"
    values = [manufacturer.company]
    results = run_sql(sql, values)
    manufacturer.id = results[0]["id"]
    return manufacturer


def select_all():
    manufacturers = []

    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql)

    for row in results:
        manufacturer = Manufacturer(row["company"], row["id"])
        manufacturers.append(manufacturer)
    return manufacturers


def select(id):
    manufacturer = None
    sql = "SELECT * FROM manufacturers WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        manufacturer = Manufacturer(result["company"], result["id"])
    return manufacturer


def delete_all():
    sql = "DELETE FROM manufacturers"
    run_sql(sql)


def guitars(manufacturer):
    guitars = []

    sql = "SELECT guitars.* FROM guitars INNER JOIN shop ON guitars.id = shop.guitar_id WHERE manufacturer_id = ?"
    values = [manufacturer.id]
    results = run_sql(sql, values)

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
