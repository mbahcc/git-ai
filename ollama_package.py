import ollama
from main import get_user_query
# Initialize the ollama API client
client = ollama.Ollama()

model = "mistral"
prompt = {get_user_query()}

# Send the query to the model

response = client.generate(model=model, prompt=prompt)

# Store the response for the LLM to match with the dictionary

llm_response = response.response
