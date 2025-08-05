from fastapi.testclient import TestClient
import pytest

import os 

from app import main

tc=TestClient(main.app)

def test_home():
    res=tc.get("/")
    assert res.status_code == 200
    assert res.json() == {"message":"come to home"}

def test_users_list():
    res=tc.get("/users")
    assert  res.status_code == 200
    assert res.json() == {"name":"ram","age":23,"role":"backend"}