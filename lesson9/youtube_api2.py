import json
from googleapiclient.discovery import build

with open("secret.json") as target:
    secret = json.load(target)

api_service_name = "youtube"
api_version = "v3"
api_developer_key = secret["KEY"]

youtube = build(api_service_name, api_version, developerKey=api_developer_key)

q = "Python"
max_result = 5

request = youtube.search().list(
    part="id,snippet",
    maxResults=max_result,
    q=q,
    order="viewCount",
    type="video"
)
response = request.execute()
items = response["items"]
item = items[0]
print(item["id"]["videoId"])