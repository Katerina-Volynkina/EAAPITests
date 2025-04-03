import datetime

import allure
import httpx
from jsonschema import validate
from core.contracts import CREATED_USER_SCHEMA, UPDATED_USER_SCHEMA

BASE_URL = 'https://reqres.in/'
CREATE_USER = 'api/users'
PUT_USER = 'api/users/2'
PATCH_USER = 'api/users/2'
DELETE_USER = 'api/users/2'


@allure.suite('Создание, изменение и удаление пользователя')
@allure.title('Создание пользователя с именем и занятием')
def test_create_user_with_name_and_job():
    body = {
    "name": "morpheus",
    "job": "leader"
}
    response = httpx.post(BASE_URL + CREATE_USER, json=body)
    with allure.step('Проверка статуса'):
        assert  response.status_code == 201

    response_json = response.json()
    creation_date = response_json['createdAt'].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())
    with allure.step('Проверка формата даты'):
        assert creation_date[0:16] == current_date[0:16]

    validate(response_json, CREATED_USER_SCHEMA)
    with allure.step('Проверка имени в запросе'):
        assert response_json['name'] == body['name']
    with allure.step('Проверка занятия в запросе'):
        assert response_json['job'] == body['job']


@allure.title('Создание пользователя с именем')
def test_create_user_with_name():
    body = {
    "name": "morpheus"
    }
    response = httpx.post(BASE_URL + CREATE_USER, json=body)
    with allure.step('Проверка статуса'):
        assert  response.status_code == 201

    response_json = response.json()
    creation_date = response_json['createdAt'].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())
    with allure.step('Проверка формата даты'):
        assert creation_date[0:16] == current_date[0:16]

    validate(response_json, CREATED_USER_SCHEMA)
    with allure.step('Проверка имени в запросе'):
        assert response_json['name'] == body['name']


@allure.title('Создание пользователя с занятием')
def test_create_user_with_job():
    body = {
    "job": "leader"
}
    response = httpx.post(BASE_URL + CREATE_USER, json=body)
    with allure.step('Проверка статуса'):
        assert  response.status_code == 201

    response_json = response.json()
    creation_date = response_json['createdAt'].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())
    with allure.step('Проверка формата даты'):
        assert creation_date[0:16] == current_date[0:16]

    validate(response_json, CREATED_USER_SCHEMA)
    with allure.step('Проверка занятия в запросе'):
        assert response_json['job'] == body['job']


@allure.title('Изменение пользователя')
def test_update_user():
    body = {
    "name": "morpheus555",
    "job": "zion 5555"
    }
    response = httpx.put(BASE_URL + PUT_USER, json=body)
    with allure.step('Проверка статуса'):
        assert  response.status_code == 200

    response_json = response.json()
    updation_date = response_json['updatedAt'].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())
    with allure.step('Проверка формата даты'):
        assert updation_date[0:16] == current_date[0:16]

    validate(response_json, UPDATED_USER_SCHEMA)
    with allure.step('Проверка имени в запросе'):
        assert response_json['name'] == body['name']
    with allure.step('Проверка занятия в запросе'):
        assert response_json['job'] == body['job']


@allure.title('Частичное изменение пользователя')
def test_patch_user():
    body = {
    "name": "morpheus",
    "job": "0204 resident"
    }
    response = httpx.patch(BASE_URL + PATCH_USER, json=body)
    with allure.step('Проверка статуса'):
        assert  response.status_code == 200

    response_json = response.json()
    updation_date = response_json['updatedAt'].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())
    with allure.step('Проверка формата даты'):
        assert updation_date[0:16] == current_date[0:16]

    validate(response_json, UPDATED_USER_SCHEMA)
    with allure.step('Проверка имени в запросе'):
        assert response_json['name'] == body['name']
    with allure.step('Проверка занятия в запросе'):
        assert response_json['job'] == body['job']


@allure.title('Удаление пользователя')
def test_delete_user():
    response = httpx.delete(BASE_URL + DELETE_USER)
    with allure.step('Проверка статуса'):
        assert  response.status_code == 204

