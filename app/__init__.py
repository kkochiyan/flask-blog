from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    from app.routes.main import main_bp
    from app.routes.articles import articles_bp
    from app.routes.search import search_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(articles_bp)  # БЕЗ url_prefix
    app.register_blueprint(search_bp)

    return app