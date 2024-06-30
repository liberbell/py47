import json
from googleapiclient.discovery import build
import pandas as pd

with open("secret.json") as target:
    secret = json.load(target)

api_service_name = "youtube"
api_version = "v3"
api_developer_key = secret["KEY"]

youtube = build(api_service_name, api_version, developerKey=api_developer_key)

q = "Python"
max_result = 30

items = response["items"]
items_id = []
for item in items:
    item_id = {}
    item_id["video_id"] = item["id"]["videoId"]
    item_id["channel_id"] = item["snippet"]["channelId"]
    items_id.append(item_id)


def search_video(youtube, q="automate", max_result=50):
    request = youtube.search().list(
        part="id,snippet",
        maxResults=max_result,
        q=q,
        order="viewCount",
        type="video"
    )
    response = request.execute()

# print(items_id)

df_video = pd.DataFrame(items_id)
print(df_video)