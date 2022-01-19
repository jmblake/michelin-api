from flask import Flask, jsonify

from api import utils
from api.data_access import collection

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_initial_response():
    message = {
        "apiVersion": "v1.0",
        "status": "200",
    }
    response = jsonify(message)
    return response, 200


@app.route("/api/v1/editions", methods=["GET"])
def fetch_edition_names():
    """
    Get a list of all editions.
    :return:
    """
    full_edition_names: list[str] = collection.distinct("edition")
    simplified_names: list[str] = [utils.simplify_edition_name(edition_name)
                                   for edition_name in full_edition_names]
    if simplified_names:
        return jsonify({'editions': simplified_names}), 200
    else:
        return jsonify({'editions': []}), 200


@app.route("/api/v1/edition/<edition>", methods=["GET"])
def get_restaurants(edition):
    """
    Function to get a list of restaurants by specifying the edition.
    :param edition:
    :return:
    """
    restaurants = collection.find(
        {'edition': utils.complicate_edition_name(edition)},
        {'_id': False}
    )
    if restaurants.count() > 0:
        return jsonify(list(restaurants)), 200
    else:
        return "", 404


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


if __name__ == "__main__":
    app.run()
