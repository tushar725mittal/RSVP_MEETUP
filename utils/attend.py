from utils.header import header


def attend(event_ids, cookies, session):
    """Attends the events with the given ids"""
    print("RSVPing events...")
    for id in event_ids:
        headers = header(cookies)
        data = (
            '{"operationName":"rsvpToEvent","variables":{"input":{"eventId":"'
            + id
            + '","response":"YES","proEmailShareOptin":false,"proSurveyAnswers":[]}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"caeae323505e7f544fb3aa0ca3ea8398c342ab0504143ed9b49af85cfd8b4c38"}}}'
        )
        response = session.post(
            "https://www.meetup.com/gql", headers=headers, data=data
        )
        if response.status_code == 200:
            print("Successfully RSVP'd to event with id: " + id)
