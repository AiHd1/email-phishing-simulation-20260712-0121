# Email Phishing Simulation Tool

## Description
This tool is designed to simulate phishing emails to help organizations test their employees' awareness and response to phishing attempts. It sends out customizable phishing emails to a list of recipients and tracks their interactions with the emails.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/email-phishing-simulation.git
   cd email-phishing-simulation
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage Examples
### Sending Phishing Emails
To send phishing emails to a list of recipients, use the following command:
```bash
python main.py send --recipients recipients.txt --subject "Urgent: Update Your Account Information" --body body.html --link http://example.com/phish
```

### Tracking Interactions
To track interactions with the sent emails, use the following command:
```bash
python main.py track
```

## Options
- `send`: Send phishing emails to recipients.
  - `--recipients`: Path to a file containing the list of email addresses.
  - `--subject`: Subject of the phishing email.
  - `--body`: Path to an HTML file containing the body of the email.
  - `--link`: URL to which the phishing link should point.
- `track`: Track interactions with the sent emails.

## Notes
- Ensure you have the necessary permissions to send emails to the recipients.
- Customize the email body and link to fit your simulation needs.