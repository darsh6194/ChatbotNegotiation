import os
from flask import Flask, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
from textblob import TextBlob
import re

# Load environment variables
load_dotenv()

# Set up Gemini API
genai.configure(api_key=os.getenv("Your API Key"))
model = genai.GenerativeModel('gemini-pro')

app = Flask(__name__)

# Product information
product = {
    "name": "Premium Wireless Headphones",
    "base_price": 200,
    "min_price": 150,
    "max_price": 250
}

negotiation_state = {
    "current_offer": product["base_price"],
    "rounds": 0,
    "max_rounds": 5,
    "sentiment_score": 0
}

def get_ai_response(user_message, negotiation_history):
    prompt = f"""
    You are an AI assistant acting as a supplier in a negotiation for {product['name']}.
    The base price is ${product['base_price']}, and you can offer between ${product['min_price']} and ${product['max_price']}.
    Current offer: ${negotiation_state['current_offer']}
    Negotiation rounds: {negotiation_state['rounds']}/{negotiation_state['max_rounds']}
    Customer sentiment score: {negotiation_state['sentiment_score']}

    Negotiation history:
    {negotiation_history}

    Customer: {user_message}

    Respond as the supplier, considering the negotiation state and history. Be polite and professional.
    If you decide to make a new offer, clearly state the new price in your response.
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return "I'm sorry, but I encountered an unexpected error. Please try again later."

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

def extract_price(text):
    price_match = re.search(r'\$?(\d+(?:\.\d{2})?)', text)
    if price_match:
        return float(price_match.group(1))
    return None

def update_offer(ai_response, user_sentiment):
    extracted_price = extract_price(ai_response)
    if extracted_price:
        negotiation_state['current_offer'] = max(min(extracted_price, product['max_price']), product['min_price'])
    
    # Adjust offer based on sentiment
    sentiment_adjustment = user_sentiment * 10  # Adjust by up to $10 based on sentiment
    negotiation_state['current_offer'] = max(min(negotiation_state['current_offer'] - sentiment_adjustment, product['max_price']), product['min_price'])

@app.route('/negotiate', methods=['POST'])
def negotiate():
    data = request.json
    user_message = data.get('message')
    negotiation_history = data.get('history', [])

    if negotiation_state['rounds'] >= negotiation_state['max_rounds']:
        return jsonify({"message": "Negotiation has ended. Maximum rounds reached.", "status": "ended"})

    user_sentiment = analyze_sentiment(user_message)
    negotiation_state['sentiment_score'] = (negotiation_state['sentiment_score'] * negotiation_state['rounds'] + user_sentiment) / (negotiation_state['rounds'] + 1)

    ai_response = get_ai_response(user_message, negotiation_history)
    
    if "unexpected error" in ai_response.lower():
        return jsonify({
            "message": ai_response,
            "current_offer": negotiation_state['current_offer'],
            "rounds": negotiation_state['rounds'],
            "status": "error"
        })

    update_offer(ai_response, user_sentiment)
    negotiation_state['rounds'] += 1

    return jsonify({
        "message": ai_response,
        "current_offer": negotiation_state['current_offer'],
        "rounds": negotiation_state['rounds'],
        "status": "ongoing"
    })

if __name__ == '__main__':
    app.run(debug=True)
