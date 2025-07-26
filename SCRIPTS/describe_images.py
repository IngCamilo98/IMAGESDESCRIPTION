from google import genai
GEMINI_API_KEY="AIzaSyD332uVXCMg6fslTo1Qj5X5QOTVZhyl870"
# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(GEMINI_API_KEY)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)