from flask_mail import Message

def send_email(mail, recipient, subject, body):
    msg = Message(subject, recipients=[recipient], body=body)
    mail.send(msg)
