
---

### ✅ `cryptobuddy.py`

```python
# CryptoBuddy Chatbot

crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8
    }
}

def get_user_input():
    return input("\nYou: ").lower()

def respond_to_query(query):
    if "sustainable" in query:
        recommended = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"CryptoBuddy: Invest in {recommended}! 🌱 It’s eco-friendly and has long-term potential!"
    
    elif "trending" in query or "profit" in query or "growth" in query:
        for name, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["market_cap"] == "high":
                return f"CryptoBuddy: {name} is currently rising with a strong market cap. 🚀 Consider it for high profitability!"
        return "CryptoBuddy: Hmm... no perfect match found right now!"

    elif "energy" in query:
        low_energy = [name for name, data in crypto_db.items() if data["energy_use"] == "low"]
        return f"CryptoBuddy: Try {' or '.join(low_energy)} — they consume less energy. 🌍"

    elif "help" in query or "what can you do" in query:
        return ("CryptoBuddy: I can help you choose a crypto based on trends or sustainability.\n"
                "Ask things like:\n"
                "- Which crypto is trending?\n"
                "- What’s the most sustainable coin?\n"
                "- I want long-term growth suggestions.")

    else:
        return "CryptoBuddy: I’m not sure how to help with that. Try asking about sustainability, trends, or profitability."

def chat():
    print("👋 Hello! I’m CryptoBuddy, your AI-powered financial sidekick!")
    print("Ask me about crypto trends, energy use, or long-term investment advice. Type 'exit' to quit.")

    while True:
        user_query = get_user_input()
        if "exit" in user_query:
            print("CryptoBuddy: Goodbye! 🌟 Remember to invest wisely.")
            break
        response = respond_to_query(user_query)
        print(response)

if __name__ == "__main__":
    chat()
