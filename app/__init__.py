from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from config import Config


def create_app(test_config=None):
    #
    # create and configure the app
    #
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)
    bootstrap = Bootstrap(app)

    #
    # Blueprints
    #
    from . import inscription
    app.register_blueprint(inscription.bp)

    #
    # Routes
    #
    @app.route('/home')
    def home():
        return render_template('home.html', title="Home")
    app.add_url_rule('/', endpoint='home')

    #
    # 404 page
    #
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    return app
