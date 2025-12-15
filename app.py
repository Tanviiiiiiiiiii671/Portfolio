#from fastapi import FastAPI, Body
from ollama_api import OllamaClient #ollama_api is your own Python file (or module)
#that you created earlier to handle communication with the Ollama model.
#app = FastAPI(title="Customer Support Chatbot API")
# Chatbot class (unchanged)
class CustomerSupportChatbot:
    def __init__(self):
        self.client = OllamaClient()
        self.context = [
            {"role": "system", "content": "You are a helpful customer support assistant."}]
        
    def chat(self, user_input):
        self.context.append({"role": "user", "content": user_input})
        bot_reply = self.client.chat(self.context)
        self.context.append({"role": "assistant", "content": bot_reply})
        return bot_reply
    def generate(self, prompt):
        bot_reply = self.client.chat([{"role": "user", "content": prompt}])
        return bot_reply
# Initialize chatbot
bot = CustomerSupportChatbot()
# Chat (endpoint) NOW ACCEPTS PLAIN text
@app.post("/chat")
async def chat_endpoint(
    text: str =Body(..., media_type="text/plain")
):
    bot_reply = bot.chat(text)
    return {"reply" : bot_reply}
#Generate endpoint (also plain text)
#@app.post("/generate")
#async def generate_endpoint(
#text: str = Body(..., media_type="text/plain")
#bot_reply = bot.generate(text)
#return {"reply": bot_reply}
#Optional root endpoint
#@app.get("/")
#def root():
#return {"message": "Customer Support Chatbot API is running!", "input_type": "text/plain"}

