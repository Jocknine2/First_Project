from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository

manufacturer_blueprint = Blueprint("manufacturer", __name__)

# index
@manufacturer_blueprint.route("/manufacturers")
def manufacturer():
    manufacturers = manufacturer_repository.select_all()
    return render_template("manufacturers/index.html", manufacturers=manufacturers)


# show


@manufacturer_blueprint.route("/manufacturers/<id>")
def show(id):
    manufacturer = manufacturer_repository.select(id)
    guitars = manufacturer_repository.guitars(manufacturer)
    return render_template(
        "manufacturers/show.html", manufacturer=manufacturer, guitars=guitars
    )


@manufacturer_blueprint.route("/manufacturers/new", methods=["GET"])
def new_manufacturer():
    manufacturer = manufacturer_repository.select_all()
    return render_template("tasks/new.html", manufacturers=manufacturer)


# create


@manufacturer_blueprint.route("/manufacturer", methods=["POST"])
def create_manufacturer():
    company = request.form["company"]

    manufacturer = Manufacturer(company)

    manufacturer_repository.save(manufacturer)
    return redirect("/manufacturers")


# edit


@manufacturer_blueprint.route("/manufacturer/<id>/edit", methods=["GET"])
def edit_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template("/tasks/edit.html", manufacturer=manufacturer)


# update


@manufacturer_blueprint.route("/manufacturer/<id>", methods=["POST"])
def update_manufacturer(id):

    company = request.form("company")

    manufacturer = Manufacturer(company, id)

    manufacturer_repository.update(manufacturer)
    return redirect("/tasks")
