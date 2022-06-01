from db.run_sql import run_sql
from models.shop import Shop
import repositories.guitar_repository as guitar_repository
import repositories.manufacturer_repository as manufacturer_repository


def save(product):
    sql = "INSERT INTO shop ( manufacturer_id, guitar_id, stock ) VALUES ( ?,?,? ) RETURNING id"
    values = [product.manufacturer.id, product.guitar.id, product.stock]
    results = run_sql(sql, values)
    product.id = results[0]["id"]
    return product


def select_all():
    products = []

    sql = "SELECT * FROM shop"
    results = run_sql(sql)

    for row in results:
        manufacturer = manufacturer_repository.select(row["manufacturer_id"])
        guitar = guitar_repository.select(row["guitar_id"])
        product = Shop(manufacturer, guitar, row["stock"], row["id"])
        products.append(product)
    return products


def select(id):
    product = None
    sql = "SELECT * FROM shop WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        guitar = guitar_repository.select(result["guitar_id"])
        manufacturer = manufacturer_repository.select(result["manufacturer_id"])
        product = Shop(
            manufacturer,
            guitar,
            result["stock"],
            result["id"],
        )
    return product


def delete_all():
    sql = "DELETE FROM shop"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM shop WHERE id = ?"
    values = [id]
    run_sql(sql, values)


def update(product):
    sql = "UPDATE shop SET (manufacturer_id, guitar_id, stock) = (?, ?, ?) WHERE id = ?"
    values = [product.manufacturer.id, product.guitar.id, product.stock]
    run_sql(sql, values)
