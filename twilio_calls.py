from twilio.rest import Client

def make_call(task):
    account_sid = "your_account_sid"
    auth_token = "your_auth_token"
    from_number = "+1234567890"

    client = Client(account_sid, auth_token)

    call = client.calls.create(
        twiml=f"<Response><Say>Reminder: {task['name']} is due soon. Please complete it.</Say></Response>",
        to=task['phone_number'],
        from_=from_number
    )
    return call.sid
