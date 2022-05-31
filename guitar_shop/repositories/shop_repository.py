from db.run_sql import run_sql
from models.manufacturer import Manufacturer
from models.shop import Shop
import repositories.guitar_repository as guitar_repository
import repositories.manufacturer_repository as manufacturer_repository


def save(shop):
    sql = "INSERT INTO shop ( guitar_id, manufacturer_id ) VALUES ( ?,? ) RETURNING id"
    values = [shop.guitar.id, shop.manufacturer.id]
    results = run_sql(sql, values)
    shop.id = results[0]["id"]
    return shop


def select_all():
    products = []

    sql = "SELECT * FROM shop"
    results = run_sql(sql)

    for row in results:
        manufacturer = manufacturer_repository.select(row["manufacturer_id"])
        guitar = guitar_repository.select(row["guitar_id"])
        shop = Shop(manufacturer, guitar, row["id"])
        products.append(shop)
    return products


def delete_all():
    sql = "DELETE FROM shop"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM shop WHERE id = ?"
    values = [id]
    run_sql(sql, values)
