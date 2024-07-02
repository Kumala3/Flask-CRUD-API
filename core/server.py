from flask import Flask, jsonify, request
from json import loads
from flask_cors import CORS
from constants import products

app = Flask("Product Server")
CORS(app)


@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)


@app.route("/products/<int:product_id>", methods=["GET"])
def get_product_by_id(product_id: int):
    for product in products:
        if product["product_id"] == product_id:
            return jsonify(product), 200
    return jsonify({"error": "Product not found"}), 404


@app.route("/create-product", methods=["POST"])
def create_product():
    json_data = request.json

    if not json_data:
        return jsonify({"error": "No data provided"}), 400

    if not json_data.get("name") or not json_data.get("price"):
        return jsonify({"error": "Name and price are required"}), 400

    for product in products:
        if product["product_id"] == json_data["product_id"]:
            return jsonify(
                {"error": f"Product with id: {json_data['product_id']} already exists"}
            ), 400

    products.append(json_data)
    return (
        f"Product with id: {json_data['product_id']} has been successfully created!",
        201,
    )


@app.route("/update-product/<int:product_id>", methods=["PUT"])
def update_product(product_id: int):
    product = next((p for p in products if p["product_id"] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    json_data = loads(request.data.decode("utf-8"))
    if not json_data:
        return jsonify({"error": "No data to update"}), 400

    updated_keys = []

    for key, value in json_data.items():
        if key != "product_id" and key in product:
            updated_keys.append(key)
            product[key] = value

    if len(updated_keys) == 1:
        return f"{', '.join(updated_keys)} has been updated!", 200
    elif len(updated_keys) > 1:
        return f"{', '.join(updated_keys)} have been updated!", 200
    else:
        return "No parameters were updated!", 200


@app.route("/delete-product/<int:product_id>", methods=["DELETE"])
def delete_product(product_id: int):
    product = next((p for p in products if p["product_id"] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    products.remove(product)
    return jsonify({"message": "Product has been successfully deleted"}), 200


if __name__ == "__main__":
    app.run(port=5000, debug=True)
