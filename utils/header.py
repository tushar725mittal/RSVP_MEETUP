def header(cookies):
    """Returns the headers for the requests"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
        "Accept": "*/*",
        "Accept-Language": "en-US",
        "Content-Type": "application/json",
        "apollographql-client-name": "nextjs-web",
        "x-meetup-view-id": "95ba3a43-bfb5-496c-9de6-90a11b6a62cc",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Connection": "keep-alive",
        "Cookie": "MEETUP_CSRF=88c272ae-45f5-4ea9-b284-d0c605d6ee7f; _lr_retry_request=true; enable_fundraising_pledge_banner_show=true; fs.bot.check=true",
        "TE": "trailers",
    }
    # Update headers with cookies
    headers["Cookie"] += "; ".join([f"{c.name}={c.value}" for c in cookies])

    return headers
