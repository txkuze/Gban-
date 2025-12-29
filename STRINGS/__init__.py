import yaml
import os

BASE_DIR = os.path.dirname(__file__)
LANG_PATH = os.path.join(BASE_DIR, "langs", "en.yml")

def get_string(key, default=None):
    try:
        with open(LANG_PATH, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        return data.get(key, default or key)
    except Exception:
        return default or key
