import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")

def rewrite_query(question):
    response = model.generate_content(
        f"Rewrite into standalone question:\n{question}"
    )
    return response.text