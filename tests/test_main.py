import pytest
# from fastapi.testclient import TestClient
from starlette.testclient import TestClient
from app.main import app
from datetime import datetime

client = TestClient(app)


def test_now_endpoint_returns_iso_datetime():
    resp = client.get("/now")
    assert resp.status_code == 200
    data = resp.json()
    assert "now" in data
    assert isinstance(data["now"], str)
    try:
        # datetime.fromisoformat will raise if the string is not a valid ISO format
        datetime.fromisoformat(data["now"])
    except Exception as e:
        pytest.fail(f"Invalid ISO datetime returned: {e}")