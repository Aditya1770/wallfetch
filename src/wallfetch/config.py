import tomllib
import tomli_w
from pathlib import Path


config_path = Path("~/.config/wallfetch/config.toml").expanduser()


def getAPI_key():
    if config_path.exists():
        with config_path.open(mode="rb") as file:
            config = tomllib.load(file)
        return config["api"]["api_key"]
    else:
        return None


# print(getAPI_key())


def getDefaults():
    if config_path.exists():
        with config_path.open(mode="rb") as file:
            config = tomllib.load(file)
        return config["defaults"]
    else:
        return None


def saveAPI_key(api_key):
    config_path.parent.mkdir(parents=True, exist_ok=True)

    config = {}
    
    if config_path.exists():
        with config_path.open(mode="rb") as file:
            config = tomllib.load(file)

    if "api" not in config:
        config["api"] = {}

    config["api"]["api_key"] = api_key
    
    with config_path.open(mode="wb") as file:
        tomli_w.dump(config, file)

def saveDownload(path):
    config_path.parent.mkdir(parents=True, exist_ok=True)

    config = {}
    
    if config_path.exists():
        with config_path.open(mode="rb") as file:
            config = tomllib.load(file)

    if "api" not in config:
        config["api"] = {}

    config["defaults"]["folder"] = path
    
    with config_path.open(mode="wb") as file:
        tomli_w.dump(config, file)
