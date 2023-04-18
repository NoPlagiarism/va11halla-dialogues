import os
import pathlib
from collections import defaultdict
import json

ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
DEFAULT_RAW_URL = "https://raw.githubusercontent.com/NoPlagiarism/va11halla-dialogues/master"


def gen_standard_info(lang, raw_url):
    return {file: "/".join((raw_url, lang, file)) for file in ("dialogue_scripts.json", "dialogue_grouped.json", "names.json")}


def create_info_json(root_path=None, raw_url=None):
    if root_path is None:
        root_path = ROOT_PATH
    if raw_url is None:
        raw_url = DEFAULT_RAW_URL
    info = defaultdict(dict)
    for path in pathlib.Path(root_path).iterdir():
        if not path.is_dir() or path.name.startswith("."):
            continue
        lang = path.name
        info[lang].update(gen_standard_info(lang, raw_url))
    
    with open(os.path.join(root_path, "info.json"), encoding="utf-8", mode="w+") as f:
        json.dump(info, f, indent=4)


if __name__ == "__main__":
    create_info_json(root_path=os.environ.get("VA11_ROOT") or ROOT_PATH,
                     raw_url=os.environ.get("VA11_DEF_URL") or DEFAULT_RAW_URL)
