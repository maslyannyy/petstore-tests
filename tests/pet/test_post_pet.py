import allure
import pytest
from hamcrest import assert_that, has_entries

from framework.clients import PetStoreApiClient
from framework.data.requests import post_pet_request
from framework.helpers.asserts import assert_status_code

pet_store_client = PetStoreApiClient()


@allure.feature('PET')
@allure.story('POST /pet')
@allure.title('Success')
def test_success(new_pet):
    input_ = post_pet_request.copy()
    output = new_pet.dict(by_alias=True)

    output.pop('id')
    assert_that(input_, has_entries(output), 'All fields should be equal')


@pytest.mark.skip(reason='Need requirements')
@allure.feature('PET')
@allure.story('POST /pet')
@allure.title('Invalid pet id')
def test_invalid_id():
    response = pet_store_client.post_pet(data={})
    assert_status_code(response, status_code=400)
