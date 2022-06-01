from click import edit
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from controllers.manufacturer_controller import manufacturer
from models.shop import Shop
import repositories.guitar_repository as guitar_repository
import repositories.manufacturer_repository as manufacturer_repository
import repositories.shop_repository as shop_repository
from controllers.guitar_controller import create_guitar
from controllers.manufacturer_controller import create_manufacturer

shop_blueprint = Blueprint("/shop", __name__)

# get products


@shop_blueprint.route("/shop")
def shop():
    products = shop_repository.select_all()
    return render_template("/shop/index.html", products=products)


# Show


@shop_blueprint.route("/shop/<id>", methods=["GET"])
def show_product(id):
    product = shop_repository.select(id)
    return render_template("/shop/show.html", product=product)


# new product


@shop_blueprint.route("/shop/new", methods=["GET"])
def new_product():
    guitars = guitar_repository.select_all()
    manufacturers = manufacturer_repository.select_all()
    return render_template(
        "shop/new.html", guitars=guitars, manufacturers=manufacturers
    )


# ------------------------------------------------------------------------
# Create product


@shop_blueprint.route("/shop/new", methods=["POST"])
def create_product(id):
    guitar = request.form["model, body, build_price, retail_price, details"]
    manufacturer = request.form["company"]
    stock = request.form["stock"]

    guitar = guitar_repository.select(guitar)
    manufacturer = manufacturer_repository.select(manufacturer)
    shop = shop(guitar, manufacturer, stock)

    create_manufacturer(manufacturer)
    create_guitar(guitar)

    shop_repository.save(shop)
    return redirect("/shop")


# ------------------------------------------------------------------------
# delete


@shop_blueprint.route("/shop/<id>/delete", methods=["POST"])
def delete_product(id):
    shop_repository.delete(id)
    return redirect("/shop")


# edit


@shop_blueprint.route("/shop/<id>/edit", methods=["GET"])
def edit_product(id):
    product = shop_repository.select(id)
    guitar = guitar_repository.select_all()
    manufacturer = manufacturer_repository.select_all()
    return render_template(
        "/tasks/edit.html", product=product, guitar=guitar, manufacturers=manufacturer
    )
