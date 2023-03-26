import re
from utils.urls import GQL_URL
from utils.header import header


def fetch_event_ids(cookies, session):
    """Fetches the event ids of the upcoming events of the user"""
    print("Fetching event ids...")
    url = GQL_URL

    headers = header(cookies)
    data = '{"operationName":"getYourUpcomingEvents","variables":{"status":"ACTIVE","first":20,"eventType":null,"lat":null,"lon":null,"radius":null,"after":""},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"f6764729a7335c8ea238096775718501f58e46e776984bc8ef27e2ba5d31711b"}}}'

    response = session.post(url, headers=headers, data=data)
    pattern = r"/events/[a-zA-Z0-9]+"
    ids = re.findall(pattern, response.text)
    event_ids = []
    for i in ids:
        event_ids.append(i.split("/")[2])

    return event_ids
