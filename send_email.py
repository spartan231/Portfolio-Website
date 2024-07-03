import os
import smtplib
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "howardmilleriv23@gmail.com"
    password = os.getenv("PASSWORD")
    receiver = "howardmilleriv23@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


send_email()

"qsdk ktke wlsp xbbn"