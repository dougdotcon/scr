import os
from flask import Flask, render_template, request, redirect, url_for, send_file
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import DataRequired, Length, NumberRange
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from flask_babel import Babel
from flask_caching import Cache

# Funcão para criar o aplicativo Flask
def create_app(test_config=None):
    # Cria e configura o aplicativo
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    cache = Cache(app, config={'CACHE_TYPE': 'simple'})

    sentry_sdk.init(
        dsn='your-sentry-dns',
        integrations=[FlaskIntegration()],
        traces_sample_rate=1.0
    )
    babel = Babel(app)

    from .. import auth
    app.register_blueprint(auth.bp)

    from .. import views
    app.register_blueprint(views.bp)

    @babel.localeselector
    def get_locale():
        return request.accept_languages.best_match(['en', 'es'])

    return app


app = create_app()
