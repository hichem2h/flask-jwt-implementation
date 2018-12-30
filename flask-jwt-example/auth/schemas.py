from app import ma
from marshmallow import validates_schema, ValidationError, post_load
from .validators import is_valid_email


class LoginSchema(ma.Schema):
    username = ma.Str()
    email = ma.Str()
    password = ma.Str()

    @validates_schema()
    def check_password_provided(self, data):
        password = data.get('password', None)

        if password is None or password.strip() == '':
            raise ValidationError('Password is required',
                                  field_names=['password'])

    @validates_schema()
    def check_username_or_email_provided(self, data):
        username = data.get('username', None)
        email = data.get('email', None)

        if username is None or username.strip() == '':
            if email is None or email.strip() == '':
                raise ValidationError('Username or Email is required',
                                      field_names=['username_email'])
            elif not is_valid_email(email.strip()):
                raise ValidationError('Not a valid email address',
                                      field_names=['email'])

    @post_load
    def strip_data(self, data):
        for field, value in data.items():
            data[field] = value.strip()
