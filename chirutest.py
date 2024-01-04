import json
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

def get_prompt(user_query: str, functions: list = []) -> str:
    """
    Generates a conversation prompt based on the user's query and a list of functions.

    Parameters:
    - user_query (str): The user's query.
    - functions (list): A list of functions to include in the prompt.

    Returns:
    - str: The formatted conversation prompt.
    """
    if len(functions) == 0:
        return f"USER: <<question>> {user_query}\nASSISTANT: "
    functions_string = json.dumps(functions)
    return f"USER: <<question>> {user_query} <<function>> {functions_string}\nASSISTANT: "

# Device setup
device : str = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

# Model and tokenizer setup
model_id : str = "gorilla-llm/gorilla-openfunctions-v1"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True)

# Move model to device
model.to(device)

# Pipeline setup
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=1024,
    batch_size=16,
    torch_dtype=torch_dtype,
    device=device,
)

# Example usage
query: str = "Increse Label layout height and width to 100 pixels"

functions = [{
    "name": "change Button Background",
    "api_name": "changeButtonBackground",
    "description": "Transform the visual impact of your button by leveraging this versatile function to adjust its background style. With this powerful tool, customize background properties such as color, gradient, transparency, and more. Whether you're aiming for a vibrant and attention-grabbing design or a subtle and cohesive background, this function provides the flexibility to seamlessly tailor the background style of your buttons, enhancing the overall aesthetics of your user interface.",
    "parameters": {
      "type": "object",
      "properties": {
        "color": {
          "type": "string",
          "description": "Specify the background color for the button."
        },
        "repeat": {
          "type": "string",
          "description": "Define the repetition pattern (e.g., repeat, no-repeat) for the button background."
        },
        "position": {
          "type": "string",
          "description": "Specify the background position (e.g., top, center, bottom) for the button."
        },
        "size": {
          "type": "string",
          "description": "Set the size of the background for the button."
        },
        "attachment": {
          "type": "string",
          "description": "Define the attachment behavior (e.g., scroll, fixed) for the button background."
        }
      },
      "required": ["color", "repeat", "position", "size", "attachment"]
    }
    },
    {
    "name": "change Label Caption Name",
    "api_name": "changeLabelCaptionName",
    "description": "The 'Change Label Caption Name' function is used to modify the caption name provided by the user.",
    "parameters": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "This is for the name provided by the user for the caption name."
        }
      },
      "required": ["name"]
    }
  },
    {
    "name": "change Label Layout",
    "api_name": "changeLabelLayout",
    "description": "This function enables users to modify the layout of the label, providing the flexibility to reposition, resize, or apply other adjustments to the spatial arrangement of the label within the user interface. By utilizing this feature, users can tailor the label's placement and dimensions to suit specific design preferences and enhance the overall visual organization of the interface",
    "parameters": {
      "type": "object",
      "properties": {
        "height": {
          "type": "string",
          "description": "Specify the height for the label layout."
        },
        "width": {
          "type": "string",
          "description": "Specify the width for the label layout."
        }
      },
      "required": ["height", "width"]
    }
  }
]

#print("Len of the Fucntions",len(functions))
# Generate prompt and obtain model output
#result = []
#for i in range(len(functions)):
prompt = get_prompt(query, functions=functions)
result = pipe(prompt)

#result = result["generated_text"]
#response = result.split('ASSISTANT:')[1].strip()
print(result)
