from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.manufacturer import Manufacturer
from models.guitar import Guitar
import repositories.guitar_repository as guitar_repository

guitar_blueprint = Blueprint("guitar", __name__)


@guitar_blueprint.route("/guitars")
def guitars():
    guitars = guitar_repository.select_all()  # NEW
    return render_template("guitars/index.html", guitars=guitars)


@guitar_blueprint.route("/guitars/<id>")
def show(id):
    guitar = guitar_repository.select(id)
    manufacturers = guitar_repository.manufacturers(guitar)
    return render_template(
        "guitars/show.html", guitar=guitar, manufacturers=manufacturers
    )
