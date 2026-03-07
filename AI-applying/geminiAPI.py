from google import genai

api_key = "AIzaSyADr582lRMSIIb8mikf3fVBK01MfKZwgOg"

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents="Você está limitado a me fornecer informações até qual data?",
)

print(response.text)
