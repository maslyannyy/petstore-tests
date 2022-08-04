import allure
import pytest

from framework.clients import PetStoreApiClient
from framework.data.constants import INVALID_PET_ID, UNKNOWN_PET_ID
from framework.helpers.asserts import assert_status_code

pet_store_client = PetStoreApiClient()


@allure.feature('PET')
@allure.story('DELETE /pet/:petId')
@allure.title('Success')
def test_success(new_pet):
    with allure.step('Delete pet'):
        response = pet_store_client.delete_pet_by_id(pet_id=new_pet.id_)
        assert_status_code(response)

    with allure.step('Check that pet was deleted'):
        response = pet_store_client.get_pet_by_id(pet_id=new_pet.id_)
        assert_status_code(response, 404)


@allure.feature('PET')
@allure.story('DELETE /pet/:petId')
@allure.title('Invalid pet id')
def test_invalid_id():
    response = pet_store_client.delete_pet_by_id(pet_id=INVALID_PET_ID)
    assert_status_code(response, status_code=400)


@pytest.mark.skip(reason='Need requirements')
@allure.feature('PET')
@allure.story('DELETE /pet/:petId')
@allure.title('Unknown pet id')
def test_unknown_id():
    response = pet_store_client.delete_pet_by_id(pet_id=UNKNOWN_PET_ID)
    assert_status_code(response, status_code=404)
