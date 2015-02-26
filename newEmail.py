import smtplib
from email.mime.multipart import MIMEMultipart
import Config
from email.mime.text import MIMEText


def send(subject, plain_text_message, html_message, to_list):
    """
    example of how to use newEmail to send emails
    toList = ["samuelr@yorkshiretrading.com", "superlistingteam@gmail.com"]
    newEmail.send("Test Message", "another new message\nyesyesyes", "<p>Html Message</p>", toList)

    :type subject: str
    :type message: str
    :type to_list: list[str]
    """
    if not to_list:
        to_list = 'superlistingteam@gmail.com'
    # Create a text/plain message
    msg = MIMEMultipart('alternative')
    config = Config.emailConfig()
    msg['Subject'] = subject
    msg['From'] = config.from_email
    msg['To'] = ', '.join(to_list)

    if plain_text_message == '':
        plain_text_message = 'This email has been sent as an HTML email; please view it in a ' \
                             'capable email client.'

    part1 = MIMEText(plain_text_message, 'plain')
    part2 = MIMEText(html_message, 'html')

    msg.attach(part1)
    msg.attach(part2)

    server = smtplib.SMTP(config.server, config.port)
    server.starttls()
    server.login(config.login_name, config.login_password)
    failDict = server.sendmail(config.from_email, to_list, msg.as_string())
    server.quit()
    if len(failDict) > 0:
        print(failDict)
