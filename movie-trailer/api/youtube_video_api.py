import json
from hidden import passkey
import pprint
from googleapiclient.discovery import build


my_key = passkey()


def youtube_search(film):
    """Constructs the youtube search query and returns the first corresponding
        result from the result list.
    """
    service = build("youtube", "v3", developerKey=my_key)
    requested_trailer = film + ' trailer'
    request = service.search().list(q=requested_trailer,
                                    part="id",
                                    maxResults=5).execute()
    request.get("items", [])
    return request["items"][0]["id"]["videoId"]
