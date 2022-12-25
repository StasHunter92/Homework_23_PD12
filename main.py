from flask import Flask
from flask_restx import Api

from config import Config
from app.views.perform_query_view import perform_query_ns

api = Api()


# ----------------------------------------------------------------------------------------------------------------------
# Create application
def create_application(config_object: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config_object)
    register_extensions()
    api.init_app(application)
    return application


def register_extensions() -> None:
    api.add_namespace(perform_query_ns)


app = create_application(Config())


# ----------------------------------------------------------------------------------------------------------------------
# Error handlers
@app.errorhandler(404)
def error_404(error):
    """Page 404 error"""
    return f"OOPS! Error {error}, page not found", 404


@app.errorhandler(500)
def error_500(error):
    """Internal server error"""
    return f"OOPS! Error {error}, server have a problem", 500


# ----------------------------------------------------------------------------------------------------------------------
# Run application
if __name__ == '__main__':
    app.run()
