import json
import os

def save_data(filepath: str, new_data, overwrite=False):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    if not overwrite:
        existing = load_data(filepath)
        existing.append(new_data)
        new_data = existing
    with open(filepath, "w", encoding="utf-8") as f:
        for item in new_data:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

def load_data(filepath: str) -> list:
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return [json.loads(line) for line in f.readlines()]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def load_json_list(filepath: str) -> list:
    try:
        with open(filepath, encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
