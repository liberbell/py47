import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

# scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "secret.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)
    
    max_result = 50

    request = youtube.search().list(
        part="id,snippet",
        maxResults=max_result,
        # q="surfing"
        q=q
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()