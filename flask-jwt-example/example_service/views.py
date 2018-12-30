from flask import jsonify
from flask_jwt_extended import (get_jwt_identity, get_jwt_claims,
                                jwt_required, fresh_jwt_required, jwt_optional)


@jwt_required
def protected():
    username = get_jwt_identity()
    claims = get_jwt_claims()
    return jsonify(logged_in_as=username, claims=claims), 200


@jwt_optional
def partially_protected():
    current_user = get_jwt_identity()

    if current_user:
        return jsonify(logged_in_as=current_user), 200
    else:
        return jsonify(loggeed_in_as='anonymous user'), 200


@fresh_jwt_required
def critical():
    username = get_jwt_identity()
    claims = get_jwt_claims()
    return jsonify(fresh_logged_in_as=username, claims=claims), 200
