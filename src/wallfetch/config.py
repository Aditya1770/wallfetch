import tomllib
from pathlib import Path


config_path = Path("~/.config/wallfetch/config.toml").expanduser()


def getAPI_key():
    if config_path.exists():
        with config_path.open(mode="rb") as file:
            config = tomllib.load(file)
        return config["api_key"]
    else:
        return None


# print(getAPI_key())


def saveAPI_key(api_key):
    config_path.parent.mkdir(parents=True, exist_ok=True)

    with config_path.open(mode="w") as file:
        file.write(f'api_key = "{api_key}"\n')
