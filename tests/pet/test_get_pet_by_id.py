import allure
from hamcrest import assert_that, equal_to

from framework.clients import PetStoreApiClient
from framework.data.constants import INVALID_PET_ID, UNKNOWN_PET_ID
from framework.helpers.asserts import assert_status_code, parse_schema
from framework.schemas.petstore import Pet

pet_store_client = PetStoreApiClient()


@allure.feature('PET')
@allure.story('GET /pet/:petId')
@allure.title('Success')
def test_success(new_pet):
    response = pet_store_client.get_pet_by_id(pet_id=new_pet.id_)
    assert_status_code(response)

    pet = parse_schema(response.json(), Pet)

    assert_that(pet.id_, equal_to(new_pet.id_), f'ID in response should be {new_pet.id_}')


@allure.feature('PET')
@allure.story('GET /pet/:petId')
@allure.title('Invalid pet id')
def test_invalid_id():
    response = pet_store_client.get_pet_by_id(pet_id=INVALID_PET_ID)
    assert_status_code(response, status_code=400)


@allure.feature('PET')
@allure.story('GET /pet/:petId')
@allure.title('Unknown pet id')
def test_unknown_id():
    response = pet_store_client.get_pet_by_id(pet_id=UNKNOWN_PET_ID)
    assert_status_code(response, status_code=404)
