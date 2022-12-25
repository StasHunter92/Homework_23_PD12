from os import path


# ----------------------------------------------------------------------------------------------------------------------
# Create configuration
class Config(object):
    BASE_DIR = path.dirname(path.abspath(__file__))
    DATA_DIR = path.join(BASE_DIR, "app", "data")
    RESTX_JSON = {"ensure_ascii": False, "indent": 4}
