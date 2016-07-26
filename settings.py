RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

schema = {
    'name': {
        'type': 'string',
        'minlength': 3,
        'maxlength': 50,
        'required': True,
    },
    'date': {
        'type': 'datetime',
    },
    'reference': {
        'type': 'string',
        'minlength': 2,
        'maxlength': 50,
        'required': True,
    },
    'details': {
        'type': 'string',
        'minlength': 0,
        'maxlength': 300,
        'required': False
    },
    'reporter': {
        'type': 'string',
        'minlength': 3,
        'maxlength': 20,
        'required': True,
    },
}

event = {
    'item_title': 'event',
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'name',
    },
    'cache_control': 'max-age=10, must-revalidate',
    'cache_expires': 10,
    'resource_methods': ['GET', 'POST'],
    'schema': schema
}

DOMAIN = {
    'event': event,
}

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_USERNAME = ''
MONGO_PASSWORD = ''
MONGO_DBNAME = 'historia'
