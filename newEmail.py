# Import smtplib for the actual sending function
import smtplib
import emailConfig

# Import the email modules we'll need
from email.mime.text import MIMEText



def send(subject, message, toList):
    """
    :type subject: str
    :type message: str
    :type toList: list[str]
    """

    # Create a text/plain message
    msg = MIMEText(message)
    config = emailConfig.emailConfig()
    msg['Subject'] = subject
    msg['From'] = config.from_email
    msg['To'] = ', '.join(toList)

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    server = smtplib.SMTP(config.server, config.port)
    server.starttls()
    server.login(config.login_name, config.login_password)
    failDict = server.sendmail(config.from_email, toList, msg.as_string())
    server.quit()
    print(failDict)
