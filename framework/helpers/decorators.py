import json
from http import HTTPStatus
from urllib.parse import urlparse

import allure
from allure import attach, attachment_type


def attach_data(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)

        with allure.step(f'{response.request.method} {urlparse(response.request.url).path}'):
            with allure.step('Request'):
                attach(response.request.url, name='path')
                attach(json.dumps(dict(response.request.headers), indent=4), name='headers',
                       attachment_type=attachment_type.JSON)

                if response.request.body:
                    try:
                        attach(json.dumps(json.loads(response.request.body), indent=4), name='body',
                               attachment_type=attachment_type.JSON)
                    except (json.decoder.JSONDecodeError, UnicodeDecodeError):
                        attach(response.request.body, name='body')

            with allure.step('Response'):
                attach(str(HTTPStatus(response.status_code)), name=f'status code: {response.status_code}')
                attach(str(int(response.elapsed.microseconds / 1000)), name='time (milliseconds)')
                attach(json.dumps(dict(response.headers), indent=4), name='headers',
                       attachment_type=attachment_type.JSON)

                try:
                    attach(json.dumps(response.json(), indent=4), name='body', attachment_type=attachment_type.JSON)
                except json.decoder.JSONDecodeError:
                    attach(response.text, name='body')
        return response

    return wrapper
