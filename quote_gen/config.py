from pathlib import Path
from string import Template

Paths = {
    "DB_PATH": "{USER_HOME}/quotes.json",
    "PICKLE_PATH": "{USER_HOME}/qpersist",
}

# _DEFAULT_QGEN_PATH = Path.home() / ".quote_gen"
_DEFAULT_QGEN_PATH = "./.quotegen" #DEV ONLY

class InvalidConfigName(Exception):
    pass

class Config:
    def __init__(self, qgen_home):
        self._path_prefix = qgen_home
        self._data = {name: value.format(USER_HOME=qgen_home) for name,value in Paths.items()}

    def __call__(self, config_name):
        try:
            return self._data[config_name]
        except KeyError:
            msg = f"Cannot find config name: {config_name}"
            raise InvalidConfigName(msg) from None
            

get_config = Config(_DEFAULT_QGEN_PATH)


def set_app_path(path):
    global _DEFAULT_QGEN_PATH
    path = Path(path)
    if not path.exists():
        raise ValueError(f"Path '{path}' does not exist")
    _DEFAULT_QGEN_PATH = path
    get_config = Config(path)
