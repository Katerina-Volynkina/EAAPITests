import httpx
from jsonschema import validate
import allure
from core.contracts import RESOURCE_DATA_SCHEMA

BASE_URL = 'https://reqres.in/'
LIST_RESOURCE = 'api/unknown'
SINGLE_RESOURCE = 'api/unknown/2'
NOT_FOUND_RESOURCE = 'api/unknown/23'
COLOR_START = '#'

@allure.suite('Проверка запроса resource')
@allure.title('Проверяем получение списка resource')
def test_list_resource():
    response = httpx.get(BASE_URL + LIST_RESOURCE)
    with allure.step('Проверка статуса ответа'):
        assert  response.status_code == 200

    data = response.json()['data']
    for item in data:
        with allure.step('Проверяем элемент из списка'):
            validate(item, RESOURCE_DATA_SCHEMA)
            with allure.step('Проверяем длину года'):
                assert len(str(item['year'])) == 4

            with allure.step('Проверяем нет ли букв в году'):
                assert str(item['year']).isdigit() == True

            with allure.step('Проверяем длину цвета'):
                assert len(item['color']) == 7

            with allure.step('Проверяем начинается ли цвет с #'):
                assert item['color'].startswith(COLOR_START)

            with allure.step('Проверяем все ли цифры после #'):
                assert item['color'][1:].isalnum() == True

            with allure.step('Проверяем длину пантона'):
                assert len(str(item['pantone_value'])) == 7

            with allure.step('Проверяем входит ли в значение "-"'):
                assert '-' in item['pantone_value']

            with allure.step('Проверяем содержит ли строка только буквы'):
                assert item['pantone_value'].isalpha() == False

@allure.title('Проверяем получение одного resource')
def test_single_resource():
    response = httpx.get(BASE_URL + SINGLE_RESOURCE)
    with allure.step('Проверка статуса ответа'):
        assert response.status_code == 200
        data = response.json()['data']

    with allure.step('Проверяем длину года'):
        assert len(str(data['year'])) == 4

    with allure.step('Проверяем нет ли букв в году'):
        assert str(data['year']).isdigit() == True

    with allure.step('Проверяем длину цвета'):
        assert len(data['color']) == 7

    with allure.step('Проверяем начинается ли цвет с #'):
        assert data['color'].startswith(COLOR_START)

    with allure.step('Проверяем все ли цифры после #'):
        assert len(str(data['pantone_value'])) == 7

    with allure.step('Проверяем входит ли в значение "-"'):
        assert '-' in data['pantone_value']

@allure.title('Проверяем ситуацию, когда не найден ни один resource')
def test_resource_not_found():
    response = httpx.get(BASE_URL+ NOT_FOUND_RESOURCE)
    with allure.step('Проверка статуса ответа'):
        assert response.status_code == 404
