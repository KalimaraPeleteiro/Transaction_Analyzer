import smtplib
import ssl

def send_email(receiver, password, username):

    print("Chegou na Função!")

    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "moneyanalyzer.team@gmail.com"

    # This is a generated password, don't try to use it to log in into the account, it wont work.
    email_password = "nmmmzzdggfltbwpy"

    context = ssl.create_default_context()

    message = f"""
    Subject: Hi, {username}!
    
    Thank you for signing into our website.
    Here is your generated password: {password}.

    Now you can just come back and enter the site.
    """

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, email_password)
        server.sendmail(sender_email, receiver, message)