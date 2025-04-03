import allure
import httpx
from jsonschema import validate
from core.contracts import RESOURCE_DATA_SCHEMA

BASE_URL = 'https://reqres.in/'
LIST_RESOURCE = 'api/unknown'
SINGLE_RESOURCE = 'api/unknown/2'
NOT_FOUND_RESOURCE = 'api/unknown/23'
COLOR_START = '#'

@allure.suite('RESOURCE')
@allure.title('Проверка списка resource')
def test_list_resource():
    response = httpx.get(BASE_URL + LIST_RESOURCE)
    with allure.step('Проверка статуса'):
        assert  response.status_code == 200
        data = response.json()['data']

    for item in data:
        validate(item, RESOURCE_DATA_SCHEMA)
        with allure.step('Проверяем количество символов в year'):
            assert len(str(item['year'])) == 4
        with allure.step('Проверяем все ли цифры в year'):
            assert str(item['year']).isdigit() == True
        with allure.step('Проверяем количество символов в color'):
            assert len(item['color']) == 7
        with allure.step('Проверяем, что color начинается с "#"'):
            assert item['color'].startswith(COLOR_START)
        with allure.step('Проверяем количество символов в pantone_value'):
            assert len(str(item['pantone_value'])) == 7
        with allure.step('Проверяем количество символов в pantone_value'):
            assert '-' in item['pantone_value']
@allure.title('Проверка одного resource')
def test_single_resource():
    response = httpx.get(BASE_URL + SINGLE_RESOURCE)
    with allure.step('Проверка статуса'):
        assert response.status_code == 200
    data = response.json()['data']
    with allure.step('Проверяем количество символов в year'):
        assert len(str(data['year'])) == 4
    with allure.step('Проверяем все ли цифры в year'):
        assert str(data['year']).isdigit() == True
    with allure.step('Проверяем количество символов в color'):
        assert len(data['color']) == 7
    with allure.step('Проверяем, что color начинается с "#"'):
        assert data['color'].startswith(COLOR_START)
    with allure.step('Проверяем количество символов в pantone_value'):
        assert len(str(data['pantone_value'])) == 7
    with allure.step('Проверяем количество символов в pantone_value'):
        assert '-' in data['pantone_value']

@allure.title('Удаление ресурса')
def test_resource_not_found():
    response = httpx.get(BASE_URL+ NOT_FOUND_RESOURCE)
    with allure.step('Проверка статуса'):
        assert response.status_code == 404
