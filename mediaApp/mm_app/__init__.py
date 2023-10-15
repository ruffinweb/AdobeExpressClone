
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from mediaApp.mm_app.config import ProductionConfig

db = SQLAlchemy()
bcrypt = Bcrypt()
mail = Mail()


def create_app(config_class=ProductionConfig, static_database_url="/mm_app/static"):
    app = Flask(__name__, static_url_path=static_database_url)
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)

    # Importing routes after the app is initialized to prevent a circular import.
    from mediaApp.mm_app.main.routes import main_bp
    from mediaApp.mm_app.faqs.routes import faqs_bp
    from mediaApp.mm_app.contact.routes import contact_bp
    from mediaApp.mm_app.errors.routes import errors_bp
    from mediaApp.mm_app.gallery.routes import gallery_bp
    from mediaApp.mm_app.explore.routes import explore_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(faqs_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(errors_bp)
    app.register_blueprint(gallery_bp)
    app.register_blueprint(explore_bp)

    return app
