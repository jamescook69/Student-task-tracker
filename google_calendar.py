from google.oauth2 import service_account
from googleapiclient.discovery import build

def sync_to_calendar(task):
    credentials = service_account.Credentials.from_service_account_file(
        'path/to/your/service_account.json',
        scopes=['https://www.googleapis.com/auth/calendar']
    )

    service = build('calendar', 'v3', credentials=credentials)

    event = {
        'summary': task['name'],
        'description': task['notes'],
        'start': {
            'dateTime': task['deadline'],
            'timeZone': 'UTC',
        },
        'end': {
            'dateTime': task['deadline'],
            'timeZone': 'UTC',
        },
    }

    calendar_id = 'primary'
    event_result = service.events().insert(calendarId=calendar_id, body=event).execute()
    return event_result

