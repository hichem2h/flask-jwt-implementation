from .models import User


def authenticate_user(username, email, password):
    if username is not None:
        user = _authenticate_username(username, password)
    elif email is not None:
        user = _authenticate_email(email, password)

    if user is not None:
        if user.check_password(password):
            return user
    else:
        User().set_password(password)


def _authenticate_username(username, password):
    user = User.query.filter_by(username=username).first()

    if user is not None:
        return user


def _authenticate_email(email, password):
    user = User.query.filter_by(email=email).first()

    if user is not None:
        return user
