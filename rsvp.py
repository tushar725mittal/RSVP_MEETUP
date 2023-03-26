from utils import auth, fetchids, attend


def main():
    cookies, session = auth.auth()
    event_ids = fetchids.fetch_event_ids(cookies, session)
    attend.attend(event_ids, cookies, session)


if __name__ == "__main__":
    main()
