import requests
import json
class OllamaClient:
    def __init__(self, base_url="http://localhost:11434"):
        self.base = base_url#store the base url insode the object.....................
    def chat(self, messages, temperature=0.3 , max_tokens=200):
        url = f"{self.base}/api/chat"#"f"It allows you to insert variables directly inside a string.
        payload = {#payload=varibale ,dictonary
            "model": "llama3.2",
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens }
        response = requests.post(url, json=payload)#url means the address of the API where you are sending your request.
        #response.raise_for_status() #Checks if something went wrong (like wrong URL or server error). If yes, it will stop the program and show an error.
        full_response = " "
        for line in response.text.splitlines():#response is the object returned by the API call
            try:#if in this block any error occurs it will jump on the except b,ock without harming the code 
               data = json.loads(line)#Python function that converts a JSON string into a Python dictionary
               if "message" in data:# data is the dictonary and the message is the key we are checking inside the dictonary.
                  full_response += data["message"]["content"]# Take    the text from the AI’s response and add it to the final answer we are building.
            except:#take the text from the response and add it to the final answer we are are building to it.
               # If a line is not JSON or has no message, ignore it (don’t crash the program)
                pass#ignores the error and continue running
        return full_response   #Send the final chatbot answer back to the place where this function was called.
    #.strip()    #stripe Removes extra spaces or new lines
    

    