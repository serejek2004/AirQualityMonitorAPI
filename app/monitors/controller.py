from flask_jwt_extended import jwt_required
from app import app, db
from flask import request, jsonify
from app.monitors.dto import MonitorsDTO
from app.monitors.service import MonitorService

MonitorService = MonitorService(db)


@app.route('/monitor/register', methods=['POST'])
def register_monitor():
    data = request.get_json()

    try:
        monitor_dto = MonitorsDTO.from_request(data)
    except KeyError:
        return jsonify({"error": "KeyError"}), 400

    monitor_id, status_code = MonitorService.register(monitor_dto)

    return jsonify({"id": monitor_id}), status_code


@app.route('/monitor/<int:monitor_id>', methods=['PUT'])
@jwt_required()
def update_monitor_data(monitor_id: int):
    data = request.get_json()

    try:
        monitor_dto = MonitorsDTO.from_request(data)
    except KeyError:
        return jsonify({"error": "KeyError"}), 400

    monitor, status_code = MonitorService.update_monitor_data(monitor_id, monitor_dto)

    if monitor:
        return jsonify(monitor.to_dict()), status_code
    else:
        return jsonify({"Error": "Bad request"}), status_code


@app.route('/monitor/<int:id>', methods=['GET'])
@jwt_required()
def get_data(id: int):
    monitor, status_code = MonitorService.get_data(id)

    if monitor:
        return jsonify(monitor.to_dict()), status_code
    else:
        return jsonify({"Error": "Bad request"}), status_code
