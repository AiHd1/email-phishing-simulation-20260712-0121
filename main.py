import argparse
import logging
from core.email_sender import EmailSender
from core.interaction_tracker import InteractionTracker
from utils.config import Config
from utils.logger import setup_logger

def parse_arguments():
    parser = argparse.ArgumentParser(description="Email Phishing Simulation Tool")
    subparsers = parser.add_subparsers(dest='command')

    send_parser = subparsers.add_parser('send', help='Send phishing emails')
    send_parser.add_argument('--recipients', required=True, help='Path to a file containing the list of email addresses')
    send_parser.add_argument('--subject', required=True, help='Subject of the phishing email')
    send_parser.add_argument('--body', required=True, help='Path to an HTML file containing the body of the email')
    send_parser.add_argument('--link', required=True, help='URL to which the phishing link should point')

    track_parser = subparsers.add_parser('track', help='Track interactions with the sent emails')

    return parser.parse_args()

def main():
    setup_logger()
    args = parse_arguments()
    config = Config()

    if args.command == 'send':
        try:
            with open(args.recipients, 'r') as file:
                recipients = file.read().splitlines()
        except FileNotFoundError:
            logging.error(f"Recipients file {args.recipients} not found.")
            return
        except Exception as e:
            logging.error(f"Error reading recipients file: {e}")
            return

        try:
            with open(args.body, 'r') as file:
                body = file.read()
        except FileNotFoundError:
            logging.error(f"Email body file {args.body} not found.")
            return
        except Exception as e:
            logging.error(f"Error reading email body file: {e}")
            return

        email_sender = EmailSender(config)
        try:
            email_sender.send_emails(recipients, args.subject, body, args.link)
        except Exception as e:
            logging.error(f"Error sending emails: {e}")

    elif args.command == 'track':
        tracker = InteractionTracker(config)
        try:
            tracker.track_interactions()
        except Exception as e:
            logging.error(f"Error tracking interactions: {e}")

if __name__ == '__main__':
    main()