"""Register all routes under the /api prefixes (route /heartbeat is not included)."""
from flask import Blueprint

def create_api() -> Blueprint:
    """Return the collection of routes and other app-related functions."""
    api = Blueprint("api", __name__, url_prefix="/api")

    return api
