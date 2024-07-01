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
# print(df_video["channel_id"].unique().tolist())
channel_ids = df_video["channel_id"].unique().tolist()
# print(",".join(channel_ids))

response = youtube.channels().list(
        part="statistics",
        id=",".join(channel_ids),
        fields="items(id, statistics(subscriberCount))"
    )
subscribers_list = response.execute()
# print(subscribers["items"][:5])

subscribers = []
for item in subscribers_list["items"]:
    # print(item)
    subscriber = {}
    subscriber["channel_id"] = item["id"]
    subscriber["subscriber_count"] = int(item["statistics"]["subscriberCount"])
    subscribers.append(subscriber)

df_subscribers = pd.DataFrame(subscribers)
# print(df_subscribers)

df_videosubscribe = pd.merge(left=df_video, right=df_subscribers, on="channel_id")
# print(df_videosubscribe)

df_extracted = df_videosubscribe[df_videosubscribe["subscriber_count"] < 10000]
# df_extracted = df_videosubscribe[df_videosubscribe["subscriber_count"]] < 5000

video_ids = df_extracted["video_id"].tolist()
videos_response = youtube.videos().list(
        part="snippet, statistics",
        id=",".join(video_ids),
        fields="items(id, snippet(title), statistics(viewCount))"
    )
videos_details = videos_response.execute()
# print(videos_details["items"])

videos_info = []
items = videos_details["items"]
for item in items:
    video_info = {}
    video_info["video_id"] = item["id"]
    video_info["title"] = item["snippet"]["title"]
    video_info["view_count"] = item["statistics"]["viewCount"]
    videos_info.append(video_info)

df_videos_info = pd.DataFrame(videos_info)
# print(df_videos_info)
# print(df_extracted)

result = pd.merge(left=df_extracted, right=df_videos_info, on="video_id")
print(result)