import allure
from hamcrest import assert_that, greater_than

from framework.clients import PetStoreApiClient
from framework.helpers.asserts import assert_status_code, parse_schema
from framework.schemas.petstore import Pet

pet_store_client = PetStoreApiClient()


@allure.feature('PET')
@allure.story('GET /pet/findByTags')
@allure.title('Success')
def test_success(new_pet):
    test_tag = new_pet.tags[0].name

    with allure.step('Find pets'):
        response = pet_store_client.get_pet_by_tags(tags=[test_tag])
        assert_status_code(response)

        pets = [parse_schema(pet, Pet) for pet in response.json()]

    with allure.step('Check that all pets have correct status'):
        assert_that(len(pets), greater_than(0), 'Should find the pet')

        for pet in pets:
            tags = [tag.name == test_tag for tag in pet.tags]

            assert_that(any(tags), f'Pet {pet.id_} should have tag {tags}')


@allure.feature('PET')
@allure.story('GET /pet/findByStatus')
@allure.title('Invalid status')
def test_invalid_id():
    test_tag = 'инвалид-тег'

    response = pet_store_client.get_pet_by_tags(tags=[test_tag])
    assert_status_code(response, 400)
