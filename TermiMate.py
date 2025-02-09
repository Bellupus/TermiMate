import openai
import os

def chat():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    conversation = [{"role": "system", "content": "You are a helpful assistant."}]
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        
        conversation.append({"role": "user", "content": user_input})
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or another model if selected
            messages=conversation
        )
        
        assistant_reply = response['choices'][0]['message']['content']
        print(f"Assistant: {assistant_reply}")
        
        conversation.append({"role": "assistant", "content": assistant_reply})

if __name__ == "__main__":
    chat()
