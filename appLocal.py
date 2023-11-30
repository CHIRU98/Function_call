import json
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

def get_prompt(user_query: str, functions: list = []) -> str:
    if len(functions) == 0:
        return f"USER: <<question>> {user_query}\nASSISTANT: "
    functions_string = json.dumps(functions)
    return f"USER: <<question>> {user_query} <<function>> {functions_string}\nASSISTANT: "

device : str = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

model_id : str = "gorilla-llm/gorilla-openfunctions-v0"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True)

model.to(device)

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=128,
    batch_size=16,
    torch_dtype=torch_dtype,
    device=device,
)

query: str = "change button color to the Blue"
buttonType = [
    {
        "name": "change_Button_Type",
        "api_name": "changeButtonType",
        "description": " It will get the type of the button from the user provided query and it will not return the color,it returns only the type.For Ex-Primary,Secondary,Danger,etc",
        "parameters":  [
                        {
                            "name": "type", 
                            "description": "It's type of the Button.For ex-Primary,Secondary,Danger,etc"
                        }
                        ]
    }
]

buttonColor = [
    {
        "name": "change_Button_Color",
        "api_name": "changeButtonColor",
        "description": "It will get the color of the button from the user provided query and it will change the color of the Button.For Ex colors are-Green,red,Green,etc",
        "parameters":  [
                        {
                            "name": "Color", 
                            "description": "It's type of the Button and change the Color of the Button.For Ex-Green,Blue."
                        }
                        ]
    }
]
func = [buttonType,buttonColor]
prompt = get_prompt(query, functions=func)
output = pipe(prompt)
print(output)
