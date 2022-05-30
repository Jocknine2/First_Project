from db.run_sql import run_sql
from models.guitar import Guitar


def save(guitar):

    sql = "INSERT INTO guitars(model, body, build_price, retail_price, details) VALUES ( ?, ?, ?, ?, ? ) RETURNING id"
    values = [guitar.model]
    results = run_sql(sql, values)
    guitar.id = results[0]["id"]
    return guitar


def select_all():
    guitars = []

    sql = "SELECT * FROM guitars"
    results = run_sql(sql)
    for row in results:
        guitar = Guitar(row["model"], row["body"], row["build_price"], row["retail_pricde"], row["details"] row["id"])
        guitars.append(guitar)
    return guitars


def select(id):
    guitar = None
    sql = "SELECT * FROM guitars WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        guitar = Guitar(result["model"], result["id"])
    return guitar

def delete_all():
    sql = "DELETE FROM guitars"
    run_sql(sql)
