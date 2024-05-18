from models.history_model import HistoryModel
from flask import Blueprint, jsonify

history_controller = Blueprint("history_controller", __name__)


@history_controller.route("/", methods=["GET"])
def history():
    try:
        history_list = HistoryModel.list_as_json()
        return jsonify(history_list), 200
    except Exception as error:
        return jsonify({"error": str(error)}), 500
