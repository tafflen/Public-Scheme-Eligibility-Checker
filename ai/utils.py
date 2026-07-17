from ollama import OllamaClient

client = OllamaClient(model_path="DeepSeek-Coder/Qwen/LLama")

def get_ai_response(prompt):
    return client.generate_text(prompt)
