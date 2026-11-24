import app as app_module

def test_greeting_flag_off(monkeypatch):
    monkeypatch.setattr(app_module, "FEATURE_NEW_GREETING", False)
    r = app_module.app.test_client().get("/")
    assert r.status_code == 200
    assert b"nope" in r.data
    assert b"new feature" not in r.data

def test_greeting_flag_on(monkeypatch):
    monkeypatch.setattr(app_module, "FEATURE_NEW_GREETING", True)
    r = app_module.app.test_client().get("/")
    assert b"new feature ON" in r.data