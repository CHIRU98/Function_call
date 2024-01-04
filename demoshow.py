
import torch
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
import json
from flask import Flask, request, jsonify

app = Flask(__name__)


device = "cuda:0" if torch.cuda.is_available() else "cpu"
print("device:",device)

#Model Name
model_id = "gorilla-llm/gorilla-openfunctions-v1"


tokenizer = AutoTokenizer.from_pretrained(model_id, truncation=True)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.bfloat16)
pipe = pipeline("text-generation", 
                model=model, 
                tokenizer=tokenizer,
                device=device)

##Import the vec nece
from qdrant_client import models, QdrantClient
from sentence_transformers import SentenceTransformer

encoder = SentenceTransformer("all-MiniLM-L6-v2")

###Qudrant Vector DB
qdrant = QdrantClient(host="localhost", port=6333)
qdrant.recreate_collection(
    collection_name="functioncall1",
    vectors_config=models.VectorParams(
        size=encoder.get_sentence_embedding_dimension(),  
        distance=models.Distance.DOT,
    ),
)

#Upload docs to the Collection

#Import 
#from data import documents
from doc import documents
qdrant.upload_records(
    collection_name="functioncall1",
    records=[
        models.Record(
            id=idx, vector=encoder.encode( doc["description"]).tolist(), payload=doc
        )
        for idx, doc in enumerate(documents)
    ],
)


def generate_functions_prompt(query,functions=None):
    prompt = f"""USER: <<question>> {query} <<function>> {json.dumps(functions)}\nASSISTANT: """
    return  prompt

def generate(prompt):
    return pipe(generate_functions_prompt(prompt),max_new_tokens=512,do_sample=False,return_full_text=False)[0]['generated_text']

#@app.route('/generate_prompt',methods=['GET','POST'])
@app.route('/generate_prompt',methods=['POST'])
def generate_prompt():
    data = request.get_json()
    query = data.get('query')

    ###
    hits = qdrant.search(
    collection_name="functioncall1",
    query_vector=encoder.encode(query).tolist(),
    limit=10,
    ) 
    
    ## Top Matched func schemas for the Query
    data = []
    for hit in hits:
        data.append(hit.payload["api_name"])

    ##Find the Func doc by using the RAG Func Schemas
    functions = []
    for item in data:
        for json_item in documents:
            if item == json_item.get("name") or item == json_item.get("api_name"):
                 functions.append(json_item)
    ###
    print("functions:",functions)

    ##
    #prompt = generate_functions_prompt(query,functions=functions)
    #result = generate(prompt)
    
    ###
    prompt = []
    prompt.append(generate_functions_prompt(query,functions=functions))
    print("Prompt",prompt)

    result = []
    result.append(generate(prompt))
    print("result",result)

    return jsonify({"output": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)



