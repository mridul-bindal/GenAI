from dotenv import load_dotenv
import os

load_dotenv()

from langchain.chat_models import init_chat_model

model = init_chat_model("google_genai:gemini-3.5-flash-lite")

# print(model)

response = model.invoke("why is anything to the power 0 1")

print(response.content)