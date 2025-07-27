import imaplib
import email

# Configuration
EMAIL = 'your_email@gmail.com'           # Replace with your Gmail address
PASSWORD = 'your_app_password'           # App password, not your Gmail password
IMAP_SERVER = 'imap.gmail.com'
IMAP_PORT = 993

def fetch_unread_emails():
    # Connect to the server
    mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
    mail.login(EMAIL, PASSWORD)

    # Select the inbox (read-only mode)
    mail.select('inbox')

    # Search for unread emails
    result, data = mail.search(None, '(UNSEEN)')

    if result != 'OK':
        print("Failed to retrieve emails.")
        return []

    mail_ids = data[0].split()
    emails = []

    # Loop through unread emails
    for num in mail_ids:
        result, data = mail.fetch(num, '(RFC822)')  # Full email content

        if result != 'OK':
            print(f"Failed to fetch email ID {num}")
            continue

        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)

        subject = msg['subject']
        from_ = msg['from']

        # Extract plain text body
        if msg.is_multipart():
            body = ''
            for part in msg.walk():
                if part.get_content_type() == 'text/plain':
                    body += part.get_payload(decode=True).decode(errors='ignore')
        else:
            body = msg.get_payload(decode=True).decode(errors='ignore')

        emails.append({
            'from': from_,
            'subject': subject,
            'body': body.strip()
        })

    # Logout and return emails
    mail.logout()
    return emails

# Run and print
if name == 'main':
    unread_emails = fetch_unread_emails()
    for i, email_data in enumerate(unread_emails, 1):
        print(f"\n--- Email {i} ---")
        print(f"From: {email_data['from']}")
        print(f"Subject: {email_data['subject']}")
        print(f"Body:\n{email_data['body']}")