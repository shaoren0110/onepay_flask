# -*- coding: utf-8 -*-

from flask import Flask
import click
from onepay_new.blueprints.view import view_bp
from onepay_new.models import bootstrap, db, moment
from onepay_new.models import Payflag

def create_app(config_name=None):
    app = Flask('onepay_new')
    app.config.from_pyfile('settings.py')
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True
    bootstrap.init_app(app)
    db.init_app(app)
    moment.init_app(app)
    app.register_blueprint(view_bp)
    register_commands(app)
    return app

def register_commands(app):
    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Create after drop.')
    def initdb(drop):
        """Initialize the database."""
        if drop:
            click.confirm('This operation will delete the database, do you want to continue?', abort=True)
            db.drop_all()
            click.echo('Drop tables.')
        db.create_all()
        payflag = Payflag(flag=0)
        db.session.add(payflag)
        db.session.commit()
        click.echo('Initialized database.')
