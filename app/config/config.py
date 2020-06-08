config_settings = {
    'app': {
        'host': 'localhost:5000'
    },
    'database': {
        'cool': "beans"
    }
}


def config(path):
    def deref_multi(data, keys):
        return deref_multi(data[keys[0]], keys[1:]) \
            if keys else data
    try:
        return deref_multi(config_settings, path.split('.'))
    except:
        return None