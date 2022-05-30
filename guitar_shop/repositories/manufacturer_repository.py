from db.run_sql import run_sql
from models.manufacturer import Manufacturer


def save(manufacturer):

    sql = "INSERT INTO users( name ) VALUES ( ? ) RETURNING id"
    values = [manufacturer.name]
    results = run_sql(sql, values)
    manufacturer.id = results[0]["id"]
    return manufacturer
