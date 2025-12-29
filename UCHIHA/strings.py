import yaml
import os

LANG_PATH = os.path.join(os.getcwd(), "langs")


def get_string(lang: str = "en"):
    file_path = os.path.join(LANG_PATH, f"{lang}.yml")

    if not os.path.exists(file_path):
        file_path = os.path.join(LANG_PATH, "en.yml")

    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
