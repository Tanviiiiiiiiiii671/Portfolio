from ollama_api import OllamaClient

class CustomerSupportChatbot:
    def __init__(self):
        #Instance of the ollamaclient used internally 
        self.client = OllamaClient()#chatbot can send messages to LLM and receive reply.
        self.context = [#stores the entire chat history two forms 1.who is speking 2.what is being said 
            {"role": "system", "content": "You are a helpful customer support assistant."}
        ]

    def handle_conversation(self):# Function where chatbot talks with user again and again.It controls the main chat loop
        print("Welcome to the Customer Support Chatbot!")
        print("Type 'exit' to quit.\n")

        while True:
            user_input = input("You:  ")
            if user_input.lower() == "exit":
                print("Chat ended.")
                break
            self.context.append({"role": "user", "content": user_input})# Send entire conversation (context) to LLM Receive reply text from model
            bot_reply = self.client.chat(self.context)#sends the entire conversation (context)to llm receive reply text from the model
            print("Bot:", bot_reply)#Show AI response to screen

            self.context.append({"role": "assistant", "content": bot_reply})#Bot remembers its own previous answers .Future replies
