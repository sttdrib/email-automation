def send_email(to_address, subject, body): 
# Function to send an email reply.
msg = EmailMessage() msg['From'] = EMAIL 
# Your email 
msg['To'] = to_address 
# Who you're replying to 
msg['Subject'] = "RE: " + subject 
# Add "RE:" to the original subject 
msg.set_content(body) # Set the generated reply text 
# Now connect securely to Gmail and send:
context = ssl.create_default_context() # Set up a secure connection with smtplib.SMTP_SSL(SMTP_SERVER, 465, context=context) as server: server.login(EMAIL, PASSWORD) # Login server.send_message(msg) # Send the email 