import json
import numpy as np
from Services.database import *
from googleapiclient.discovery import build

import Levenshtein

API_KEY = "AIzaSyDnRPKS42UPKN6dn36pG1NSymZWx3wbMGI"

def find_video_info(video_name: str):
    for video in VIDEOS.values():
        dist = Levenshtein.distance(video_name.lower(), video['Video'].lower())
        if dist < 5:
            return video['Likes'], video['Views']

    youtube = build('youtube', 'v3', developerKey=API_KEY)
    search_response = youtube.search().list(
        q=video_name, part='snippet', type='video', maxResults=3
    ).execute()

    best_views = -1
    best_video = None

    for item in search_response["items"]:
        video_id = item["id"]["videoId"]
        video_snippet = item["snippet"]
        video_title = clean_name(video_snippet["title"])

        stats_response = youtube.videos().list(
            part="statistics", id=video_id
        ).execute()

        stats = stats_response["items"][0]["statistics"]
        views = int(stats.get("viewCount", 0))
        likes = int(stats.get("likeCount", 0))

        if views > best_views:
            best_views = views
            best_video = {
                "Video": video_title,
                "URL": f"https://www.youtube.com/watch?v={video_id}",
                "Views": views,
                "Likes": likes
            }

    if best_video:
        VIDEOS[best_video["Video"]] = best_video
        with open(JSON_FILE, "w", encoding="utf-8") as f:
            json.dump(VIDEOS, f, indent=4, ensure_ascii=False)
        return best_video["Likes"], best_video["Views"]
    
    return 1, 1

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