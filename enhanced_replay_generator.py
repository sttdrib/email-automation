def load_notes(file_path): 
    with open(file_path, 'r') as f: 
    return f.read() 
# Read a text file and add it to the prompt like this:

notes = load_notes()
def generate_reply_with_context(email_text, notes): 
    prompt = f""" You are an assistant. Use the following notes to help answer the email. 
    Notes: {notes} 
    Email: {email_text} 
    Reply: """ 
    response = requests.post( "http://localhost:11434/api/generate", json={"model": "llama3:instruct", "prompt": prompt, "stream": False} ) 
    return response.json()['response'].strip() 