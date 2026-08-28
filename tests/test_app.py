import pytest
from app import create_app
from app.extensions import db
from app.data.seed import seed_demo_data
from app.models import Product


@pytest.fixture()
def client():
    app = create_app({"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:", "SECRET_KEY": "test"})
    with app.app_context():
        seed_demo_data()
        yield app.test_client()
        db.drop_all()


def test_health(client):
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json["database"] == "ok"


def test_artisan_flow_and_listing_fix(client):
    response = client.get("/")
    assert response.status_code == 200
    product_id = Product.query.first().id
    response = client.post(f"/products/{product_id}/fix", follow_redirects=True)
    assert response.status_code == 200
    assert b"94" in response.data


def test_officer_dashboard(client):
    response = client.get("/officer")
    assert response.status_code == 200
    assert b"District artisan intelligence" in response.data
