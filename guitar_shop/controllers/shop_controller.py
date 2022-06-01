from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.shop import Shop
import repositories.guitar_repository as guitar_repository
import repositories.manufacturer_repository as manufacturer_repository
import repositories.shop_repository as shop_repository

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


@shop_blueprint.route("/shop", methods=["POST"])
def create_product():
    manufacturer = request.form["manufacturer_id"]
    guitar = request.form["guitar_id"]
    stock = request.form["stock"]

    guitar = guitar_repository.select(guitar)
    manufacturer = manufacturer_repository.select(manufacturer)
    shop = Shop(guitar, manufacturer, stock)
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
    guitars = guitar_repository.select_all()
    manufacturers = manufacturer_repository.select_all()
    return render_template(
        "/shop/edit.html",
        product=product,
        all_guitars=guitars,
        all_manufacturers=manufacturers,
    )


# update


@shop_blueprint.route("/shop/<id>", methods=["POST"])
def update_product(id):
    manufacturer_id = request.form["manufacturer_id"]
    guitar_id = request.form["guitar_id"]
    stock = request.form["stock"]

    guitar = guitar_repository.select(guitar_id)
    manufacturer = manufacturer_repository.select(manufacturer_id)
    shop = Shop(manufacturer, guitar, stock, id)
    shop_repository.update(shop)
    return redirect("/shop")
