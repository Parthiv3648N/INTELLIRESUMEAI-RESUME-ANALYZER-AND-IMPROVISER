import google.generativeai as genai

# 🔑 Paste your NEW Gemini API key here
api_key = "AIzaSyCd-hHYokprdhaxAYKroiPkQVvYTkbU5BA"

print("Loaded API Key:", api_key)

# Configure Gemini
genai.configure(api_key=api_key)

# Use fast free model
model = genai.GenerativeModel("models/gemini-flash-latest")

try:
    response = model.generate_content("Say hello in one line")

    print("\n✅ Gemini working!\n")
    print(response.text)

except Exception as e:
    print("\n❌ Error:", e)