from env_app import get_app_env

def test_get_app_env():
    app_env = get_app_env()
    assert app_env == 'testing'

def test_get_app_env_no_env(monkeypatch):
    monkeypatch.delenv('APP_ENV', raising=False)
    app_env = get_app_env()
    assert app_env is None