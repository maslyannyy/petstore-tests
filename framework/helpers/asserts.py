import allure
import pytest
from hamcrest import assert_that, equal_to
from requests import Response


def assert_status_code(response: Response, status_code=200):
    with allure.step('Check status code'):
        assert_that(response.status_code, equal_to(status_code), f'Status code should be {status_code}')


def parse_schema(d: dict, cls):
    try:
        return cls(**d)
    except ValueError as e:
        pytest.fail(str(e))
