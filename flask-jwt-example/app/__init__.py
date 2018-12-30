from flask import Flask

from .conf import config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow

from .jwt import jwt

db = SQLAlchemy()
migrate = Migrate(db=db)
bcrypt = Bcrypt()
ma = Marshmallow()


def create_app():
    app = Flask(__name__)

    app.config.from_object(config[app.env])

    jwt.init_app(app)
    db.init_app(app)
    migrate.init_app(app)
    bcrypt.init_app(app)
    ma.init_app(app)

    from auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from example_service import bp as example_bp
    app.register_blueprint(example_bp)

    @app.route('/health')
    def health():
        return 'OK'

    return app
