import allure
import json
import httpx
import pytest
from jsonschema import validate
from core.contracts import REGISTERED_USER_SCHEMA, LOGIN_USER_SCHEMA

BASE_URL = 'https://reqres.in/'
REGISTER_USER = 'api/register'
LOGIN_USER = 'api/login'

with open('./core/new_users_data.json', 'r') as json_file:
    users_data = json.load(json_file)
    print(users_data)


@allure.suite('Проверка регистрации')
@allure.title('Проверка успешной регистрации')
@pytest.mark.parametrize('users_data', users_data)
def test_successful_register(users_data):
    responce = httpx.post(BASE_URL + REGISTER_USER, json=users_data)
    with allure.step('Проверка статуса'):
        assert responce.status_code == 200
    validate(responce.json(), REGISTERED_USER_SCHEMA)

@allure.title('Проверка неуспешной регистрации')
def test_unsuccessful_register():
    body = {
            "email": "sydney@fife"
    }
    responce = httpx.post(BASE_URL + REGISTER_USER, json=body)
    with allure.step('Проверка статуса'):
        assert responce.status_code == 400
    with allure.step('Проверка сообщения, которое приходит в ответ'):
        assert responce.text =='{"error":"Missing password"}'


@allure.title('Проверка успешной авторизации')
@pytest.mark.parametrize('users_data', users_data)
def test_successful_login(users_data):
    responce = httpx.post(BASE_URL + LOGIN_USER, json=users_data)
    with allure.step('Проверка статуса'):
        assert responce.status_code == 200
    validate(responce.json(), LOGIN_USER_SCHEMA)