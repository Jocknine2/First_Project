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

    return render_template("guitars/show.html", guitar=guitar)


# create


@guitar_blueprint.route("/guitar", methods=["POST"])
def create_guitar():
    model = request.form["model"]
    body = request.form["body"]
    build_price = request.form["build_price"]
    retail_price = request.form["retail_price"]
    details = request.form["details"]

    guitar = Guitar(model, body, build_price, retail_price, details)

    guitar_repository.save(guitar)
    return redirect("/guitar")


# edit


@guitar_blueprint.route("/guitar/<id>/edit", methods=["GET"])
def edit_guitar(id):
    guitar = guitar_repository.select(id)
    return render_template("/guitar/edit.html", guitar=guitar)


# update


@guitar_blueprint.route("/guitar/<id>", methods=["POST"])
def update_guitar(id):

    model = request.form["model"]
    body = request.form["body"]
    build_price = request.form["build_price"]
    retail_price = request.form["retail_price"]
    details = request.form["details"]

    guitar = Guitar(model, body, build_price, retail_price, details)

    guitar_repository.update(guitar)
    return redirect("/guitar")
