import tomllib
import tomli_w
from importlib.resources import files
from pathlib import Path

config_path = Path("~/.config/wallfetch/config.toml").expanduser()

def create_config():
    config_path.parent.mkdir(parents=True, exist_ok=True)

    default_config = (
        files("wallfetch")
        .joinpath("default_config.toml")
        .read_text()
    )

    config_path.write_text(default_config)

def load_config():
    if not config_path.exists():
        create_config()

    with config_path.open("rb") as file:
        return tomllib.load(file)


def save_config(config):
    config_path.parent.mkdir(parents=True, exist_ok=True)

    with config_path.open("wb") as file:
        tomli_w.dump(config, file)


def getAPI_key():
    config = load_config()
    return config["api"]["api_key"]


def getDefaults():
    config = load_config()
    return config["defaults"]


def saveAPI_key(api_key):
    config = load_config()

    config["api"]["api_key"] = api_key

    save_config(config)


def saveDownload(path):
    config = load_config()

    config["defaults"]["folder"] = path

    save_config(config)
