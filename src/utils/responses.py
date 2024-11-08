from flask import jsonify

def success_response(data, message="Success", status_code=200):
    return jsonify({"success": True, "message": message, "payload": data}), status_code

def error_response(message="Error", status_code=500):
    return jsonify({"success": False, "message": message}), status_code
