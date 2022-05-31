from flask import Flask, render_template

from controllers.guitar_controller import guitar_blueprint
from controllers.manufacturer_controller import manufacturer_blueprint
from controllers.shop_controller import shop_blueprint

app = Flask(__name__)

app.register_blueprint(shop_blueprint)
app.register_blueprint(guitar_blueprint)
app.register_blueprint(manufacturer_blueprint)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
