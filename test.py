functions = [{
    "name": "get_organic_results",
    "api_name": "getOrganicResults",
    "description": "Fetch the news url based on a search query",
    "parameters": {
      "type": "object",
      "properties": {
        "query": {
          "type": "string",
          "description": "search query."
        }
      },
      "required": ["query"]
    }
  },
  {
    "name": "get_chat_response",
    "api_name": "getResponse",
    "description": "Procide the chat responce to the query",
    "parameters": {
      "type": "object",
      "properties": {
        "user_input": {
          "type": "string",
          "description": "user's query"
        }
      },
      "required": ["query"]
    }
  },
  {
    "name": "dalle_api_generate_image",
    "api_name": "generateImage",
    "description": "Generate an image based on a description using DALL-E",
    "parameters": {
      "type": "object",
      "properties": {
        "description": {
          "type": "string",
          "description": "Description for the image to generate"
        }
      },
      "required": ["description"]
    }
  },
  {
    "name": "get_weather",
    "api_name": "getWeather",
    "description": "Provide the chat response for the user queries.",
    "parameters": {
      "type": "object",
      "properties": {
        "user_input": {
          "type": "string",
          "description": "User's query"
        }
      },
      "required": ["user_input"]
    }
  }
]

import torch
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
import json

device = "cuda:0" if torch.cuda.is_available() else "cpu"
print("device:",device)

model_id = "gorilla-llm/gorilla-openfunctions-v1"

tokenizer = AutoTokenizer.from_pretrained(model_id, truncation=True)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.bfloat16)
pipe = pipeline("text-generation", 
                model=model, 
                tokenizer=tokenizer,
                device=device)


def generate_functions_prompt(query,functions=None):
    prompt = f"""USER: <<question>> {query} <<function>> {json.dumps(functions)}\nASSISTANT: """
    return  prompt

def generate(prompt):
    return pipe(generate_functions_prompt(prompt),max_new_tokens=512,do_sample=False,return_full_text=False)[0]['generated_text']

prompt = generate_functions_prompt("Find the best pizza place in New York and the weather",functions=functions)
print(generate(prompt))
