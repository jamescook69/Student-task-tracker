import requests
import json

def send_slack_notification(task):
    webhook_url = "your_webhook_url"
    payload = {
        "text": f"Reminder: {task['name']} is due on {task['deadline']}! Notes: {task['notes']}"
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    return response.status_code
  
