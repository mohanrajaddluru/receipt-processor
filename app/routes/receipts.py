from flask import Blueprint, request, jsonify, make_response
from app.utils.hash_utils import generate_hash
from app.utils.calculate_points import calculate_points

receipts_bp = Blueprint("receipts", __name__)

## Dictionary to store the points for each receipt
points_store = {}

@receipts_bp.route("/receipts/process", methods=["POST"])
def process_receipt():
    data = request.get_json()

    retailer, purchaseTime, purchaseDate, total = data["retailer"], data["purchaseTime"], data["purchaseDate"], data["total"]
    
    receipt_id = generate_hash(retailer, purchaseTime, purchaseDate, total)
    
    if receipt_id in points_store:
        return make_response(jsonify({"id": receipt_id}), 200)
   
    points = calculate_points(data)
    points_store[receipt_id] = points
    print(points_store)
    return  make_response(jsonify({"id": receipt_id}), 201)


@receipts_bp.route("/receipts/<string:receipt_id>/points", methods=["GET"])
def get_receipt_points(receipt_id):
    print(points_store)
    if not points_store or receipt_id not in points_store:
        return make_response(jsonify({"message" : "receipt_id not found"}), 404)
    points = points_store[receipt_id]
    return make_response(jsonify({"points": points}), 200)
