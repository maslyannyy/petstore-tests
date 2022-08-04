from typing import Union

from requests import session, Response

from config import SERVICE_HOST
from framework.data.enums import PetStatus
from framework.helpers.decorators import attach_data


class PetStoreApiClient:
    def __init__(self, host: str = SERVICE_HOST):
        self.host = host
        self.session = session()
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }

    @attach_data
    def _make_request(self, method: str, path: str, **kwargs) -> Response:
        return self.session.request(
            method,
            f'{self.host}{path}',
            headers=kwargs.pop('headers', self.headers),
            **kwargs
        )

    def _get(self, path: str, **kwargs) -> Response:
        return self._make_request('GET', path, **kwargs)

    def _post(self, path: str, **kwargs) -> Response:
        return self._make_request('POST', path, **kwargs)

    def _put(self, path: str, **kwargs) -> Response:
        return self._make_request('PUT', path, **kwargs)

    def _delete(self, path: str, **kwargs) -> Response:
        return self._make_request('DELETE', path, **kwargs)

    def get_pet_by_id(self, pet_id: Union[int, str], **kwargs) -> Response:
        return self._get(f'/pet/{pet_id}', **kwargs)

    def post_pet_by_id(self, pet_id: int, name: str, status: str, **kwargs) -> Response:
        headers = self.headers.copy()
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'name': name,
            'status': status,
        }

        return self._post(f'/pet/{pet_id}', headers=headers, data=data, **kwargs)

    def delete_pet_by_id(self, pet_id: int, **kwargs) -> Response:
        return self._delete(f'/pet/{pet_id}', **kwargs)

    def upload_image_by_pet_id(self, pet_id: int, data: dict, files: dict, **kwargs) -> Response:
        return self._post(f'/pet/{pet_id}/uploadImage', headers={}, data=data, files=files, **kwargs)

    def post_pet(self, data: dict, **kwargs) -> Response:
        return self._post('/pet', json=data, **kwargs)

    def put_pet(self, data: dict, **kwargs) -> Response:
        return self._put('/pet', json=data, **kwargs)

    def get_pet_by_status(self, statuses: list[Union[PetStatus, str]], **kwargs) -> Response:
        params = {
            'status': ','.join(statuses)
        }

        return self._get('/pet/findByStatus', params=params, **kwargs)

    def get_pet_by_tags(self, tags: list[str], **kwargs) -> Response:
        params = {
            'tags': ','.join(tags)
        }

        return self._get('/pet/findByTags', params=params, **kwargs)
