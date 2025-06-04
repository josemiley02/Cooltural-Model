import os
import json
JSON_FILE = os.path.join(os.path.dirname(__file__), "videos.json")

def load_videos():
    try:
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Error: El archivo JSON tiene un formato inválido.")
        return {}
    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
        return {}

VIDEOS = load_videos()