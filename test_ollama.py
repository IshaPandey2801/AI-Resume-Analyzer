from langchain_ollama import OllamaLLM

# Load local Gemma model
llm = OllamaLLM(model="gemma:2b")

# Send prompt
response = llm.invoke("Explain AI in simple words")

# Print response
print(response)