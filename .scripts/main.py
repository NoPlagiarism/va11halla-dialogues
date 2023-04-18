import os
try:
    from .info import create_info_json
except ImportError:
    from info import create_info_json

ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
DEFAULT_RAW_URL = "https://raw.githubusercontent.com/NoPlagiarism/va11halla-dialogues/master"


def main(root_path, raw_url):
    create_info_json(root_path, raw_url)


if __name__ == "__main__":
    main(root_path=os.environ.get("VA11_ROOT") or ROOT_PATH,
         raw_url=os.environ.get("VA11_DEF_URL") or DEFAULT_RAW_URL)
