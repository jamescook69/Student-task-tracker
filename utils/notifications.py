from .email_utils import send_email
from ..api.slack_notifications import send_slack_notification
from ..api.twilio_calls import make_call

def notify_task(task):
    if task.get('email'):
        send_email(task['email'], "Task Reminder", f"Reminder: {task['name']} is due on {task['deadline']}.")
    if task.get('slack'): 
        send_slack_notification(task)
    if task.get('phone_number'):
        make_call(task)
