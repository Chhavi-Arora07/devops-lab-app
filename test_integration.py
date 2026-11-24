from app import app

def test_metrics_endpoint_reports_requests():
    client = app.test_client()
    client.get("/")
    r = client.get("/metrics")
    assert r.status_code == 200
    assert b"flask_http_request_total" in r.data