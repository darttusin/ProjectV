import sys
import os

sys.path.append(sys.path[0][0:sys.path[0].rindex(os.sep)])


from app import app


class TestHomepage:
    def setup(self) -> None:
        app.testing = True
        self.client = app.test_client()
    def test_home(self) -> None:
        response=self.client.get("/")
        assert response.status_code == 200
        assert response.content_type == "text/html; charset=utf-8"

class TestStreampage:
    def setup(self) -> None:
        app.testing = True
        self.client = app.test_client()
    def test_home(self) -> None:
        response=self.client.get("/index")
        assert response.status_code == 200
        assert response.content_type == "text/html; charset=utf-8"
    