from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository

manufacturer_blueprint = Blueprint("manufacturer", __name__)


@manufacturer_blueprint.route("/manufacturers")
def manufacturer():
    manufacturers = manufacturer_repository.select_all()
    return render_template("manufacturers/index.html", manufacturers=manufacturers)


@manufacturer_blueprint.route("/manufacturers/<id>")
def show(id):
    manufacturer = manufacturer_repository.select(id)
    guitars = manufacturer_repository.guitars(manufacturer)
    return render_template(
        "manufacturers/show.html", manufacturer=manufacturer, guitars=guitars
    )
