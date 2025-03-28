import httpx
from jsonschema import validate
from core.contracts_resource import RESOURCE_DATA_SCHEMA

BASE_URL = 'https://reqres.in/'
LIST_RESOURCE = 'api/unknown'
SINGLE_RESOURCE = 'api/unknown/2'
NOT_FOUND_RESOURCE = 'api/unknown/23'
COLOR_START = '#'

def test_list_resource():
    response = httpx.get(BASE_URL + LIST_RESOURCE)
    assert  response.status_code == 200
    data = response.json()['data']

    for item in data:
        validate(item, RESOURCE_DATA_SCHEMA)
        assert len(str(item['year'])) == 4
        assert str(item['year']).isdigit() == True
        assert len(item['color']) == 7
        assert item['color'].startswith(COLOR_START)
        assert item['color'][1:].isalnum() == True
        assert len(str(item['pantone_value'])) == 7
        assert '-' in item['pantone_value']
        assert item['pantone_value'].isalpha() == False

def test_single_resource():
    response = httpx.get(BASE_URL + SINGLE_RESOURCE)
    assert response.status_code == 200
    data = response.json()['data']
    assert len(str(data['year'])) == 4
    assert str(data['year']).isdigit() == True
    assert len(data['color']) == 7
    assert data['color'].startswith(COLOR_START)
    assert data['color'][1:].isalnum() == True
    assert len(str(data['pantone_value'])) == 7
    assert '-' in data['pantone_value']
    assert data['pantone_value'].isalpha() == False


def test_resource_not_found():
    response = httpx.get(BASE_URL+ NOT_FOUND_RESOURCE)
    assert response.status_code == 404
