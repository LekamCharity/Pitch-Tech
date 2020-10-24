from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)