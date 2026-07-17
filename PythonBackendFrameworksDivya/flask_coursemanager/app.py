from flask import Flask
from config import Config
from extensions import db, migrate
from courses.routes import courses_bp
import courses.models


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(courses_bp)

    @app.errorhandler(404)
    def not_found(error):
        return {
            "status": "error",
            "message": "Resource not found"
        }, 404

    @app.errorhandler(500)
    def internal_error(error):
        return {
            "status": "error",
            "message": "Internal server error"
        }, 500

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)