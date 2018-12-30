from flask_jwt_extended import JWTManager

jwt = JWTManager()


@jwt.user_claims_loader
def add_claims_to_access_token(user):
    return {'admin': user.is_admin,
            'email': user.email,
            'date_joined': user.date_joined}


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.username
