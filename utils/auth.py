import requests
from utils.urls import GQL_URL
from utils.creds import get_credentials


def auth():
    """Authenticates the user and returns the cookie and session"""
    email, password = get_credentials()

    url = GQL_URL

    payload = (
        '{"operationName":"login","variables":{"input":{"email":"'
        + email
        + '","password":"'
        + password
        + '","rememberMe":true}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"27c2dcd3fe18741b545abf6918eb37aee203463028503aa8b2b959dc1c7aa007"}}}'
    )
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
        "Accept": "*/*",
        "Accept-Language": "undefined",
        "Content-Type": "application/json",
        "apollographql-client-name": "nextjs-web",
        "x-tracking-request-id": "434715ef-e66b-443d-bea9-fb00340cf1ea",
        "x-meetup-view-id": "4dfc3e89-2f23-461c-9c47-1250d3748932",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "referrer": "https://www.meetup.com/login/",
        "Connection": "keep-alive",
    }
    session = requests.Session()

    # First request to get cookies
    response = session.get("https://www.meetup.com/login/", headers=headers)

    # Update headers with cookies
    headers["Cookie"] = "; ".join([f"{c.name}={c.value}" for c in response.cookies])
    c1 = response.cookies.get_dict()

    # Second request to login
    response = session.post(url, headers=headers, data=payload)
    c2 = response.cookies.get_dict()
    if response.status_code != 200:
        print("Error logging in. Check your credentials.")
        exit()
    else:
        print("Successfully logged in.")

    # add both the cookies into one cookie
    cookie = {**c1, **c2}
    #  convert the cookie into <RequestsCookieJar>[] format
    jar = requests.cookies.RequestsCookieJar()
    for key, value in cookie.items():
        jar.set(key, value)

    return jar, session
