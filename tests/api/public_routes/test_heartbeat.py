"""Test API availability."""
from unittest import TestCase

from mywebapp.api.flask_app import create_app


class TestPublicRoutes(TestCase):
    def test_heartbeat_success(self):
        """Should return a 204 without restriction."""
        app = create_app()
        response = app.test_client().get("/heartbeat")
        expected = 204
        self.assertEqual(response.status_code, expected)
