from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.shop import Shop
import repositories.guitar_repository as guitar_repository
import repositories.manufacturer_repository as manufacturer_repository
import repositories.shop_repository as shop_repository

shop_blueprint = Blueprint("/shop", __name__)


@shop_blueprint.route("/shop")
def shop():
    products = shop_repository.select_all()
    return render_template("/shop/index.html", products=products)


@shop_blueprint.route("/shop/new", methods=["GET"])
def new_product():
    guitars = guitar_repository.select_all()
    manufacturers = manufacturer_repository.select_all()
    return render_template(
        "shop/new.html", guitars=guitars, manufacturers=manufacturers
    )


@shop_blueprint.route("/shop", methods=["POST"])
def create_task():
    guitar_id = request.form["guitar_id"]
    manufacturer_id = request.form["manufacturer_id"]
    guitar = guitar_repository.select(guitar_id)
    manufacturer = manufacturer_repository.select(manufacturer_id)
    shop = shop(guitar, manufacturer)
    shop_repository.save(shop)
    return redirect("/shop")


@shop_blueprint.route("/shop/<id>/delete", methods=["POST"])
def delete_task(id):
    shop_repository.delete(id)
    return redirect("/shop")
