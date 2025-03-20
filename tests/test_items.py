# 테스트 코드 
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from main import app
from database import Base, engine

client = TestClient(app)

def setup_module():
    Base.metadata.create_all(bind=engine)

def test_create_item():
    response = client.post("/v1/items/", json={"name": "Test Item", "price": 10.5})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Item"
    assert data["price"] == 10.5
    assert "id" in data

def test_get_item():
    # 먼저 아이템 생성
    create_response = client.post("/v1/items/", json={"name": "Test Item", "price": 10.5})
    item_id = create_response.json()["id"]
    
    # 아이템 조회
    response = client.get(f"/v1/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == item_id
    assert data["name"] == "Test Item"