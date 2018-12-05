from pathlib import Path
from string import Template

Paths = {
    "DB_PATH": "${USER_HOME}/quotes.json",
    "PICKLE_PATH": "${USER_HOME}/qpersist",
}


class InvalidConfigName(Exception):
    pass


def get_config(config_name):
    user_home = Path.home()
    try:
        path = Paths[config_name]
    except KeyError:
        raise InvalidConfigName()
    else:
        path = Template(path)
        return path.substitute({'USER_HOME': user_home})
