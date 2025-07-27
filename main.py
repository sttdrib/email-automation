def run_email_assistant(): 
    emails = get_unread_emails() 
    # Step 1: Fetch unread emails 
    for email_data in emails: 
        # Step 2: Loop through each one 
        print(f"Replying to: {email_data['from']} - {email_data['subject']}") 
        reply = generate_reply(email_data['body']) 
        # Step 3: Generate reply using LLM 
        send_email(email_data['from'], email_data['subject'], reply) 
        # Step 4: Send reply 
        print("Sent reply:\n", reply) 