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

    @app.route('/home')
    def home():
        return render_template('home.html', title="Home")
    app.add_url_rule('/', endpoint='home')

    return app
