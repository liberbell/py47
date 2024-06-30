import json
from googleapiclient.discovery import build
import pandas as pd

with open("secret.json") as target:
    secret = json.load(target)

api_service_name = "youtube"
api_version = "v3"
api_developer_key = secret["KEY"]

youtube = build(api_service_name, api_version, developerKey=api_developer_key)

def search_video(youtube, q="automate", max_result=50):
    request = youtube.search().list(
        part="id,snippet",
        maxResults=max_result,
        q=q,
        order="viewCount",
        type="video"
    )
    response = request.execute()

    items = response["items"]
    items_id = []
    for item in items:
        item_id = {}
        item_id["video_id"] = item["id"]["videoId"]
        item_id["channel_id"] = item["snippet"]["channelId"]
        items_id.append(item_id)

    df_video = pd.DataFrame(items_id)
    return df_video

df_video = search_video(youtube, q="Python automate", max_result=50)
# print(df_video[:5])
print(df_video["channel_id"].unique().tolist())
channel_ids = df_video["channel_id"].unique().tolist()
print(",".join(channel_ids))

# request = youtube.channels().list(
#         part="statistics",
#         id=""
#         maxResults=max_result,
#         order="viewCount",
#         type="video"
#     )