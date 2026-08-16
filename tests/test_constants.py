from web import constants


def test_api_headers_sin_key(monkeypatch):
    monkeypatch.setattr(constants, 'API_KEY', '')

    assert constants.api_headers() == {}
    assert constants.api_headers({'Authorization': 'Bearer x'}) == {'Authorization': 'Bearer x'}


def test_api_headers_con_key(monkeypatch):
    monkeypatch.setattr(constants, 'API_KEY', 'secreta')

    assert constants.api_headers() == {'X-API-Key': 'secreta'}
    assert constants.api_headers({'Authorization': 'Bearer x'}) == {
        'Authorization': 'Bearer x', 'X-API-Key': 'secreta',
    }
