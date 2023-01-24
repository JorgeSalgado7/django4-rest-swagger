from django.conf import settings
from rest_framework.settings import APISettings

DEFAULTS = {
    'USE_SESSION_AUTH': True,
    'SECURITY_DEFINITIONS': {
        'basic': {
            'type': 'basic'
        }
    },
    'LOGIN_URL': getattr(settings, 'LOGIN_URL', None),
    'LOGOUT_URL': getattr(settings, 'LOGOUT_URL', None),
    'DOC_EXPANSION': None,
    'APIS_SORTER': None,
    'OPERATIONS_SORTER': None,
    'JSON_EDITOR': False,
    'SHOW_REQUEST_HEADERS': False,
    'SUPPORTED_SUBMIT_METHODS': [
        'get',
        'post',
        'put',
        'delete',
        'patch'
    ],
    'VALIDATOR_URL': '',
    'ACCEPT_HEADER_VERSION': None,
    'CUSTOM_HEADERS': {},
}

IMPORT_STRINGS = []

swagger_settings = APISettings(
    user_settings=getattr(settings, 'SWAGGER_SETTINGS', {}),
    defaults=DEFAULTS,
    import_strings=IMPORT_STRINGS,
)