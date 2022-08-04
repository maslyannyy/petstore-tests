from datetime import datetime

import allure
import pytest

from framework.clients import PetStoreApiClient
from framework.data.enums import PetStatus
from framework.data.requests import post_pet_request
from framework.helpers.asserts import assert_status_code, parse_schema
from framework.schemas.petstore import Pet

pet_store_api_client = PetStoreApiClient()


@pytest.fixture
def new_pet():
    with allure.step('Create pet'):
        response = pet_store_api_client.post_pet(post_pet_request)
        assert_status_code(response)

        pet = parse_schema(response.json(), Pet)

    yield pet

    with allure.step('Delete pet'):
        pet_store_api_client.delete_pet_by_id(pet_id=pet.id_)


@pytest.fixture
def post_pet_test_data(new_pet):
    with allure.step('Prepare test data'):
        response = pet_store_api_client.get_pet_by_id(pet_id=new_pet.id_)
        assert_status_code(response)

        pet = parse_schema(response.json(), Pet)

    yield {
        'id_': new_pet.id_,
        'name': f'test-name-{int(datetime.now().timestamp())}',
        'status': PetStatus.available if pet.status != PetStatus.available else PetStatus.pending
    }

    with allure.step('Return params back'):
        response = pet_store_api_client.post_pet_by_id(pet_id=new_pet.id_, name=pet.name, status=pet.status)
        assert_status_code(response)
