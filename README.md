# **Student Task Organizer**

**Helping students manage assignments, deadlines, and tasks effortlessly.**

---

## **Project Overview**

The **Student Task Organizer** is a personal project designed to help students keep track of their assignments, deadlines, and tasks. By integrating with popular tools like **Google Calendar**, **Gmail**, and **Slack**, this system ensures that students stay organized and notified about their pending tasks.

### **Core Features:**
1. **Task Input & Management:** Students can input tasks and manage them within the system.
2. **Calendar Sync:** Automatically sync tasks with Google Calendar for easy access and tracking.
3. **Digital Notifications:** Receive reminders via email or Slack as deadlines approach.
4. **Voice Alerts via Calls:** 
   - On due dates, the system places automated calls (via Twilio) to students.
   - Calls deliver voice messages describing the task that needs to be completed.

This project aims to simplify task management for students and ensure they never miss an important deadline.

---

## **Installation**

Follow these steps to set up the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/student-task-organizer.git
   cd student-task-organizer
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure API credentials:
   - Obtain credentials for:
     - **Google Calendar API**
     - **Gmail API**
     - **Slack Webhooks**
     - **Twilio**
   - Place these credentials in the `config.json` file in the following format:
     ```json
     {
       "google_calendar": {
         "client_id": "your_client_id",
         "client_secret": "your_client_secret"
       },
       "gmail": {
         "api_key": "your_gmail_api_key"
       },
       "slack": {
         "webhook_url": "your_webhook_url"
       },
       "twilio": {
         "account_sid": "your_account_sid",
         "auth_token": "your_auth_token",
         "from_number": "+1234567890"
       }
     }
     ```

4. Run the application:
   ```bash
   python app.py
   ```

---

## **Usage**

### **Adding Tasks**
1. Open the application and log in with your Google account.
2. Input the task details, including:
   - Task name
   - Deadline
   - Additional notes

### **Receiving Notifications**
- **Email & Slack:** Receive reminders as deadlines approach.
- **Voice Calls:** On due dates, receive a voice call detailing the task.

---

## **Project Architecture**

```plaintext
- app.py                # Main application script
- /templates            # Frontend HTML templates
- /static               # CSS and JavaScript files
- /api                  # API integration scripts for Google, Gmail, Slack, and Twilio
- /utils                # Helper functions and utilities
- config.json           # Configuration file for API credentials
- requirements.txt      # List of required Python libraries
```

---

## **Technologies Used**

- **Backend:** Python (Flask Framework)
- **APIs:** 
  - Google Calendar API
  - Gmail API
  - Slack Webhooks
  - Twilio Voice
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite for local task storage
- **Other Tools:** 
  - `Flask-Mail` for sending emails
  - `Twilio` for making automated voice calls

---

## **License**

This project is licensed under the [MIT License](LICENSE).

---

## **Contributing**

Contributions are welcome! Here's how you can help:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

