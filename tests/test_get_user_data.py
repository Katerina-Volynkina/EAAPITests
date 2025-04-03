import allure
import httpx
from jsonschema import validate
import allure
from core.contracts import USER_DATA_SCHEMA


BASE_URL = 'https://reqres.in/'
LIST_USERS = 'api/users?page2'
SINGLE_USER = 'api/users/2'
NOT_FOUND_USER = 'api/users/23'
EMAIL_ENDS = '@reqres.in'
AVATAR_ENDS = '-image.jpg'

@allure.suite('Проверка запроса данных пользователя')
@allure.title('Проверка списка пользователей')
def test_list_users():
    response = httpx.get(BASE_URL + LIST_USERS)
    with allure.step('Проверка статуса'):
        assert  response.status_code == 200
    data = response.json()['data']

    for item in data:
        validate(item, USER_DATA_SCHEMA)
        with allure.step('Проверяем окончание EMAIL'):
            assert item['email'].endswith(EMAIL_ENDS)
        with allure.step('Проверяем есть ли в avatar id пользователя'):
            assert item['avatar'].endswith(str(item['id']) + AVATAR_ENDS)

@allure.title('Проверка одного пользователя')
def test_single_user():
    response = httpx.get(BASE_URL + SINGLE_USER)
    with allure.step('Проверка статуса'):
        assert response.status_code == 200
    data = response.json()['data']
    with allure.step('Проверяем окончание EMAIL'):
        assert data['email'].endswith(EMAIL_ENDS)
    with allure.step('Проверяем есть ли в avatar id пользователя'):
        assert data['avatar'].endswith(str(data['id']) + AVATAR_ENDS)

@allure.title('Удаление пользователя')
def test_user_not_found():
    response = httpx.get(BASE_URL+ NOT_FOUND_USER)
        with allure.step('Проверка статуса ответа'):
        assert  response.status_code == 200
        data = response.json()['data']

    for item in data:
        validate(item, USER_DATA_SCHEMA)
        with allure.step('Проверка окончание email адреса'):
            assert item['email'].endswith(EMAIL_ENDS)

        with allure.step('Проверка наличия id в ссылке на аватарку'):
            assert item['avatar'].endswith(str(item['id']) + AVATAR_ENDS)

@allure.title('Проверка 1 пользователя')
def test_single_user():
    response = httpx.get(BASE_URL + SINGLE_USER)
    with allure.step('Проверка статуса ответа'):
        assert response.status_code == 200
        data = response.json()['data']

    with allure.step('Проверка окончание email адреса'):
        assert data['email'].endswith(EMAIL_ENDS)

    with allure.step('Проверка наличия id в ссылке на аватарку'):
        assert data['avatar'].endswith(str(data['id']) + AVATAR_ENDS)

@allure.title('Проверяем ситуацию, когда не найден ни один пользователь')
def test_user_not_found():
    response = httpx.get(BASE_URL+ NOT_FOUND_USER)
    with allure.step('Проверка статуса ответа'):
        assert response.status_code == 404
