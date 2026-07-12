import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
from utils.config import Config

class EmailSender:
    def __init__(self, config: Config):
        self.config = config
        self.server = None

    def connect_to_server(self):
        try:
            self.server = smtplib.SMTP(self.config.smtp_server, self.config.smtp_port)
            self.server.starttls()
            self.server.login(self.config.smtp_user, self.config.smtp_password)
        except Exception as e:
            logging.error(f"Failed to connect to SMTP server: {e}")
            raise

    def disconnect_from_server(self):
        if self.server:
            self.server.quit()

    def send_emails(self, recipients, subject, body, link):
        self.connect_to_server()
        try:
            for recipient in recipients:
                msg = MIMEMultipart()
                msg['From'] = self.config.smtp_user
                msg['To'] = recipient
                msg['Subject'] = subject

                personalized_body = body.replace("{{link}}", link)
                msg.attach(MIMEText(personalized_body, 'html'))

                self.server.sendmail(self.config.smtp_user, recipient, msg.as_string())
                logging.info(f"Email sent to {recipient}")
        except Exception as e:
            logging.error(f"Failed to send email: {e}")
        finally:
            self.disconnect_from_server()