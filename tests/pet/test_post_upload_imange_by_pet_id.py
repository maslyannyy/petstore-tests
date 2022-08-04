import base64

import allure
import pytest
from hamcrest import assert_that, greater_than

from framework.clients import PetStoreApiClient
from framework.data.constants import BASE64PIXEL, INVALID_PET_ID, UNKNOWN_PET_ID
from framework.helpers.asserts import assert_status_code, parse_schema
from framework.schemas.petstore import Pet

pet_store_client = PetStoreApiClient()


@allure.feature('PET')
@allure.story('POST /pet/:petId/uploadImage')
@allure.title('Success')
def test_success(new_pet):
    files = {'file': ('pixel.png', base64.decodebytes(bytes(BASE64PIXEL, 'ascii')))}
    data = {'additionalMetadata': 'some img'}

    with allure.step('Upload image'):
        response = pet_store_client.upload_image_by_pet_id(pet_id=new_pet.id_, data=data, files=files)
        assert_status_code(response)

    with allure.step('Check that image was changed'):
        response = pet_store_client.get_pet_by_id(pet_id=new_pet.id_)
        assert_status_code(response)

        pet_with_img = parse_schema(response.json(), Pet)

        assert_that(len(new_pet.photoUrls), greater_than(len(pet_with_img.photoUrls)), 'Image should be added to pet')


@pytest.mark.skip(reason='Need requirements')
@allure.feature('PET')
@allure.story('POST /pet/:petId/uploadImage')
@allure.title('Invalid pet id')
def test_invalid_id():
    response = pet_store_client.upload_image_by_pet_id(pet_id=INVALID_PET_ID, data={}, files={})
    assert_status_code(response, status_code=400)


@pytest.mark.skip(reason='Need requirements')
@allure.feature('PET')
@allure.story('POST /pet/:petId/uploadImage')
@allure.title('Unknown pet id')
def test_unknown_id():
    response = pet_store_client.upload_image_by_pet_id(pet_id=UNKNOWN_PET_ID, data={}, files={})
    assert_status_code(response, status_code=404)
