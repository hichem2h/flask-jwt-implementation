from flask import request, jsonify
from flask.views import MethodView
from marshmallow import ValidationError

from flask_jwt_extended import (create_access_token, create_refresh_token,
                                get_jwt_identity, jwt_refresh_token_required)

from .schemas import LoginSchema
from .auth_backends import authenticate_user

from .models import User


class LoginView(MethodView):
    schema = LoginSchema(strict=True)

    def post(self):
        json_data = request.get_json(force=True, silent=True)

        if json_data is None:
            json_data = {}

        try:
            data = self.schema.load(json_data).data
        except ValidationError as err:
            return jsonify(err.messages), 400

        username = data.get('username', None)
        email = data.get('email', None)
        password = data.get('password', None)

        user = authenticate_user(username, email, password)

        if user is None:
            description = 'Bad credentials'
            return jsonify(description=description), 401

        if not user.is_active:
            description = 'Account has been deactivated'
            return jsonify(description=description), 401

        response = self.create_tokens(user)
        return response

    def create_tokens(self, user):
        access_token = create_access_token(user)
        refresh_token = create_refresh_token(user)

        return jsonify(access_token=access_token,
                       refresh_token=refresh_token), 200


class FreshLoginView(LoginView):
    def create_tokens(self, user):
        fresh_access_token = create_access_token(user, fresh=True)

        return jsonify(fresh_access_token=fresh_access_token), 200


class RefreshView(MethodView):
    decorators = [jwt_refresh_token_required]

    def post(self):
        username = get_jwt_identity()
        user = User.query.filter_by(username=username).first()

        access_token = create_access_token(user)

        return jsonify(access_token=access_token), 200
