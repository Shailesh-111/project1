from flask import Flask, request, jsonify, Blueprint
from src.model.user import User
from src.database import db

user = Blueprint("user", __name__)


@user.route("/create_user", methods=["POST"])
def create_user():
    data = request.json
    try:
        user = User(first_name=data['first_name'], last_name=data['last_name'], status=data['status'], email = data['email'])
        db.session.add(user)
        db.session.commit()

        return jsonify({
            "success": True,
            "message": "User created successfully"
        }), 201
    except Exception as e:
        return jsonify({
            "success": False,
            "message": "Internal Server Error"
        }), 500


@user.route("/update_user/<user_id>", methods=["POST"])
def update_user(user_id):
    data = request.json
    user = User.query.get(user_id)
    if not user:
        return jsonify({
            "success": False,
            "message": "User not found"
        }), 404

    try:
        for field, value in data.items():
            setattr(user, field, value)
        db.session.commit()

        return jsonify({
            "success": True,
            "message": "User updated successfully"
        }), 200
    except Exception as e:
        return jsonify({
            "success": False,
            "message": "Internal Server Error"
        }), 500


@user.route("/delete_user/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({
            "success": False,
            "message": "User not found"
        }), 404

    try:
        db.session.delete(user)
        db.session.commit()

        return jsonify({
            "success": True,
            "message": "User deleted successfully"
        }), 200
    except Exception as e:
        return jsonify({
            "success": False,
            "message": "Internal Server Error"
        }), 500


@user.route("/get_all_users", methods=["GET"])
def get_all_users():
    try:
        users = User.query.all()
        users_list = [
            {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "status": user.status,
            }
            for user in users
        ]

        return jsonify({
            "success": True,
            "data": users_list,
            "message": "Users fetched successfully"
        }), 200
    except Exception as e:
        return jsonify({
            "success": False,
            "message": "Internal Server Error"
        }), 500