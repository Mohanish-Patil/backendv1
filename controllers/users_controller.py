
from flask import Blueprint, jsonify, request
from extensions import db
from models.user import User

users_bp = Blueprint("users", __name__)



@users_bp.route("/users", methods=["GET"])
def index():
    return jsonify({
        "message": "Users controller is working!",
        "method": request.method
    })


@users_bp.route("/users", methods=["POST"])
def create():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "JSON request body required"}), 400

    print("data is : ",data)

    name = data.get("name")
    email = data.get("email")

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already exists"}), 409

    user = User(name=name, email=email)
    user.set_password(data.get("password", ""))

    db.session.add(user)
    db.session.commit()

    if not name or not email:
        return jsonify({
            "error": "name and email are required"
        }), 400

    return jsonify({
        "message": "Request received successfully",
        "user": {
            "name": name,
            "email": email
        }
    }), 201

    # data = request.get_json(silent=True)

    # if not data:
    #     return jsonify({"error": "JSON request body required"}), 400

    # name = data.get("name")
    # email = data.get("email")

    # if not name or not email:
    #     return jsonify({"error": "name and email are required"}), 400

    # if User.query.filter_by(email=email).first():
    #     return jsonify({"error": "Email already exists"}), 409

    # user = User(name=name, email=email)
    # user.set_password(data.get("password", ""))

    # if not data.get("password"):
    #     return jsonify({"error": "password is required"}), 400

    # try:
    #     db.session.add(user)
    #     db.session.commit()

    #     return jsonify({
    #         "message": "User created successfully",
    #         "user": {
    #             "id": user.id,
    #             "name": user.name,
    #             "email": user.email
    #         }
    #     }), 201

    # except Exception:
    #     db.session.rollback()
    #     return jsonify({"error": "Failed to create user"}), 500
