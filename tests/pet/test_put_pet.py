import allure
import pytest
from hamcrest import assert_that, has_entries

from framework.clients import PetStoreApiClient
from framework.data.constants import INVALID_PET_ID, UNKNOWN_PET_ID
from framework.data.requests import put_pet_request
from framework.helpers.asserts import assert_status_code, parse_schema
from framework.schemas.petstore import Pet

pet_store_client = PetStoreApiClient()


@allure.feature('PET')
@allure.story('PUT /pet')
@allure.title('Success')
def test_success(new_pet):
    put_pet_request['id'] = new_pet.id_

    with allure.step('Change pet'):
        response = pet_store_client.put_pet(data=put_pet_request)
        assert_status_code(response)

        pet = parse_schema(response.json(), Pet)

    with allure.step('Check that all fields was changed'):
        assert_that(pet.dict(by_alias=True), has_entries(put_pet_request), 'All fields should be equal')


@allure.feature('PET')
@allure.story('PUT /pet')
@allure.title('Invalid pet id')
def test_invalid_id():
    data = {
        'id': INVALID_PET_ID
    }

    response = pet_store_client.put_pet(data=data)
    assert_status_code(response, status_code=400)


@allure.feature('PET')
@allure.story('PUT /pet')
@allure.title('Unknown pet id')
def test_unknown_id(new_pet):
    data = {
        'id': UNKNOWN_PET_ID
    }

    response = pet_store_client.put_pet(data=data)
    assert_status_code(response, status_code=404)


@pytest.mark.skip(reason='Need requirements')
@allure.feature('PET')
@allure.story('PUT /pet')
@allure.title('Validation error')
def test_validation_err(new_pet):
    data = {
        'id': new_pet.id_,
        'status': 'invalid-status'
    }

    response = pet_store_client.put_pet(data=data)
    assert_status_code(response, status_code=405)
