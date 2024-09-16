import requests
import json

def negotiate(message, history=None):
    if history is None:
        history = []
    
    url = "http://localhost:5000/negotiate"
    headers = {"Content-Type": "application/json"}
    data = {
        "message": message,
        "history": history
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

# Example usage
response = negotiate("I am interested in buying the headphones. What is your best price?")
print(json.dumps(response, indent=2))

# Continue the negotiation
while response["status"] == "ongoing":
    user_input = input("Your response: ")
    response = negotiate(user_input, response.get("history", []))
    print(json.dumps(response, indent=2))

print("Negotiation ended.")

'''
To use this script:
1. Save it as `client.py` in your project directory.
2. Install the `requests` library if you haven't already: `pip install requests`
3. Run the script: `python client.py`

This script will allow you to have an interactive negotiation session with the chatbot through your terminal.

c) Using a tool like Postman:
- Set the request type to POST
- Set the URL to `http://localhost:5000/negotiate`
- In the Headers tab, add `Content-Type` with value `application/json`
- In the Body tab, select "raw" and JSON, then enter:
  ```json
  {
    "message": "I am interested in buying the headphones. What is your best price?",
    "history": []
  }
  ```

Remember to include the previous messages in the `history` array for subsequent requests to maintain context in the negotiation.

The API will return a JSON response containing:
- `message`: The AI's response
- `current_offer`: The current price offer
- `rounds`: The number of negotiation rounds completed
- `status`: Either "ongoing" or "ended"

You can continue sending messages back and forth until the negotiation ends (either by reaching the maximum number of rounds or by coming to an agreement).

Would you like me to explain any part of this process in more detail, or do you have any questions about using the API? '''