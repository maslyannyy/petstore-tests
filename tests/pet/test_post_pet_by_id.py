import allure
import pytest
from hamcrest import assert_that, equal_to

from framework.clients import PetStoreApiClient
from framework.data.constants import INVALID_PET_ID, UNKNOWN_PET_ID
from framework.helpers.asserts import assert_status_code, parse_schema
from framework.schemas.petstore import Pet

pet_store_client = PetStoreApiClient()


@allure.feature('PET')
@allure.story('POST /pet/:petId')
@allure.title('Success')
def test_success(post_pet_test_data):
    id_, name, status = post_pet_test_data['id_'], post_pet_test_data['name'], post_pet_test_data['status']

    with allure.step('Change fields'):
        response = pet_store_client.post_pet_by_id(pet_id=id_, name=name, status=status)
        assert_status_code(response)

    with allure.step('Check that fields was changed'):
        response = pet_store_client.get_pet_by_id(pet_id=id_)
        assert_status_code(response)

        pet = parse_schema(response.json(), Pet)

        assert_that(pet.name, equal_to(name), 'Name should be changed')
        assert_that(pet.status, equal_to(status), 'Status should be changed')


@allure.feature('PET')
@allure.story('POST /pet/:petId')
@allure.title('Invalid pet id')
def test_invalid_id():
    response = pet_store_client.post_pet_by_id(pet_id=INVALID_PET_ID, name='', status='')
    assert_status_code(response, status_code=405)


@pytest.mark.skip(reason='Need requirements')
@allure.feature('PET')
@allure.story('POST /pet/:petId')
@allure.title('Unknown pet id')
def test_unknown_id():
    response = pet_store_client.post_pet_by_id(pet_id=UNKNOWN_PET_ID, name='', status='')
    assert_status_code(response, status_code=404)
