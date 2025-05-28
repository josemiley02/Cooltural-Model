import json
import numpy as np
from googleapiclient.discovery import build
import os
import Levenshtein

API_KEY = "AIzaSyDnRPKS42UPKN6dn36pG1NSymZWx3wbMGI"
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

def find_video_info(video_name: str):
    videos = load_videos()
    for video in videos.values():
        dist = Levenshtein.distance(video_name.lower(), video['Video'].lower())
        if dist < 5:
            return video['Likes'], video['Views']

    youtube = build('youtube', 'v3', developerKey=API_KEY)
    request = youtube.search().list(q = video_name, part='snippet', type='video', maxResults=1)
    response = request.execute()

    video_id = response['items'][0]['id']['videoId']
    video_title = response['items'][0]['snippet']['title']

    video_title = clean_name(video_title)

    request = youtube.videos().list(part="statistics", id=video_id)
    response = request.execute()

    stats = response["items"][0]["statistics"]
    views = stats.get("viewCount", "Desconocido")
    likes = stats.get("likeCount", "Desconocido")

    video_data = {
        "Video": video_title,
        "URL": f"https://www.youtube.com/watch?v={video_id}",
        "Views": views,
        "Likes": likes
    }

    videos[video_title] = video_data
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(videos, f, indent=4, ensure_ascii=False)

    return likes, views

def web_rating(query: str) -> float:
    likes, views = find_video_info(query)
    return np.log(int(views) / int(likes))

def clean_name(name: str) -> str:
    clean = ""
    for c in name:
        if c == '(':
            break
        clean += c
    return clean