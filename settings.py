MONGO_HOST = "ds043338.mlab.com"
MONGO_PORT = 43338
MONGO_USERNAME = 'eric'
MONGO_PASSWORD = 'nanjing1'
MONGO_DBNAME = 'testdb'

XML = False
# CORS
X_DOMAINS = '*'

ALLOW_UNKNOWN = True

schema = {
    'username': {
        'type': 'string',
        'required': True,
        'unique': True
    },
    'password': {
        'type': 'string',
        'required': True
    },
    'role': {
        'allowed': ['user', 'superuser', 'admin'],
    },
    'token': {
        'type': 'string',
        'required': True,
    }
}

accounts = {
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'username'
    },
    'cache_control': '',
    'cache_expires': 0,
    'resource_methods': ['GET', 'POST'],
    'public_methods': ['GET, PUT'],
    'public_item_methods': ['GET', 'PUT', 'PATCH'],
    'item_methods': ['GET', 'PUT', "DELETE"],
    'allowed_roles': ['superuser', 'admin'],
    'extra_response_fields': ['token'],
    'schema': schema

}

DOMAIN = {'accounts': accounts}
