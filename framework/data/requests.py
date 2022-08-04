from framework.data.enums import PetStatus

post_pet_request = {
    'name': 'kitty',
    'photoUrls': [
        'https://ya.ru/some-img',
    ],
    'category': {
        'id': 111,
        'name': 'some-category'
    },
    'tags': [
        {
            'id': 222,
            'name': 'some-tags'
        }
    ],
    'status': PetStatus.pending
}

put_pet_request = {
    'name': 'doggie',
    'photoUrls': [
        'https://ya.ru/some-img2',
    ],
    'category': {
        'id': 333,
        'name': 'some-category2'
    },
    'tags': [
        {
            'id': 444,
            'name': 'some-tags2'
        }
    ],
    'status': PetStatus.sold
}
