from flask_jwt_extended import jwt_required
from app import app, db
from flask import request, jsonify
from app.users.dto import AuthUsersDTO, UpdateUsersDTO
from app.users.service import UserService

UserService = UserService(db)


@app.route('/user/register', methods=['POST'])
def register_user():
    data = request.get_json()

    try:
        user_dto = AuthUsersDTO.from_request(data)
    except KeyError:
        return jsonify({"Error": "KeyError"}), 400

    user, status_code = UserService.register(user_dto)

    if user:
        return jsonify(user.to_dict()), status_code
    else:
        return jsonify({"Error": "Bad request"}), status_code


@app.route('/user/login', methods=['POST'])
def login_user():
    data = request.get_json()

    try:
        user_dto = AuthUsersDTO.from_request(data)
    except KeyError:
        return jsonify({"error": "KeyError"}), 400

    access_token, status_code = UserService.login(user_dto)

    if access_token:
        return jsonify({"access_token": access_token}), status_code
    else:
        return jsonify({"Error": "Bad request"}), status_code


@app.route('/user/update', methods=['PUT'])
@jwt_required()
def update_user():
    data = request.get_json()

    try:
        user_dto = UpdateUsersDTO.from_request(data)
    except KeyError:
        return jsonify({"error": "KeyError"}), 400

    user, status_code = UserService.update(user_dto)

    if user:
        return jsonify(user.to_dict()), status_code
    else:
        return jsonify({"Error": "Bad request"}), status_code
