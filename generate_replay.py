import requests

def generate_reply(email_text, model="llama3:instruct"): 
# This function sends your email content to a local LLM running on your PC via Ollama, and asks it to generate a reply.
    prompt = f"""You are an assistant. Read the following email and generate a professional reply. 
            Email: {email_text} 
            Reply: """ 
# We are creating a prompt to instruct the model on what to do.
    response = requests.post( "http://localhost:11434/api/generate", # This is where Ollama runs locally 
                            json={"model": model, "prompt": prompt, "stream": False} ) 
# This line sends the prompt to Ollama via HTTP.
#    return response.json()['response'].strip() # Return the model’s reply 
    
    
    
    try: 
        data = response.json()
        print("Response JSON:", data['response'])
        return #data.get('Response', 'No response from model').strip()
    except ValueError:
#        print('Invaiid JSON response', respnse.text)
#        return 'Error'
        print('Error')
