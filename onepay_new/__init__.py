# -*- coding: utf-8 -*-

from flask import Flask

from onepay_new.blueprints.view import view_bp
from onepay_new.models import bootstrap, db, moment

def create_app(config_name=None):
    app = Flask('onepay_new')
    app.config.from_pyfile('settings.py')
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True
    bootstrap.init_app(app)
    db.init_app(app)
    moment.init_app(app)
    app.register_blueprint(view_bp)
    return app


