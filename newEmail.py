# Import smtplib for the actual sending function
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import Config

# Import the email modules we'll need
from email.mime.text import MIMEText

def send(subject, plain_text_message, html_message, toList):
    """
    example of how to use newEmail to send emails
    toList = ["samuelr@yorkshiretrading.com", "superlistingteam@gmail.com"]
    newEmail.send("Test Message", "another new message\nyesyesyes", "<p>Html Message</p>", toList)

    :type subject: str
    :type message: str
    :type toList: list[str]
    """
    if not toList:
        toList = u'superlistingteam@gmail.com'
    # Create a text/plain message
    msg = MIMEMultipart('alternative')
    config = Config.emailConfig()
    msg['Subject'] = subject
    msg['From'] = config.from_email
    msg['To'] = ', '.join(toList)

    if plain_text_message == '':
        plain_text_message = 'This email has been sent as an HTML email; please view it in a capable email client.'

    part1 = MIMEText(plain_text_message, 'plain')
    part2 = MIMEText(html_message, 'html')

    msg.attach(part1)
    msg.attach(part2)

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    server = smtplib.SMTP(config.server, config.port)
    server.starttls()
    server.login(config.login_name, config.login_password)
    failDict = server.sendmail(config.from_email, toList, msg.as_string())
    server.quit()
    if len(failDict) > 0:
        print(failDict)
