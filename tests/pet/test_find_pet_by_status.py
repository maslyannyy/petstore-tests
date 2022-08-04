import allure
from hamcrest import assert_that, equal_to

from framework.clients import PetStoreApiClient
from framework.data.enums import PetStatus
from framework.helpers.asserts import assert_status_code, parse_schema
from framework.schemas.petstore import Pet

pet_store_client = PetStoreApiClient()


@allure.feature('PET')
@allure.story('GET /pet/findByStatus')
@allure.title('Success')
def test_success():
    test_status = PetStatus.sold

    with allure.step('Find pets'):
        response = pet_store_client.get_pet_by_status(statuses=[test_status])
        assert_status_code(response)

        pets = [parse_schema(pet, Pet) for pet in response.json()]

    with allure.step('Check that all pets have correct status'):
        for pet in pets:
            assert_that(pet.status, equal_to(test_status), f'Pet {pet.id_} should have status {test_status}')


@allure.feature('PET')
@allure.story('GET /pet/findByStatus')
@allure.title('Invalid status')
def test_invalid_id():
    test_status = 'invalid-status'

    response = pet_store_client.get_pet_by_status(statuses=[test_status])
    assert_status_code(response, 400)
