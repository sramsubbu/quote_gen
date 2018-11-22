_app_config = {
    'DB_PATH': 'quotes.json'
}


def fetch(key):
    return _app_config[key]

