from flask_cors import CORS
import torch
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
import json
from flask import Flask, request, jsonify

app = Flask(__name__)
CORS(app)


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
    collection_name="functioncall",
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
    collection_name="functioncall",
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

@app.route('/generate_prompt',methods=['GET','POST'])
#@app.route('/generate_prompt',methods=['POST'])
def generate_prompt():
    if request.method == 'GET':
        query = request.args.get('query')
        #data = request.get_json()
        #query = data.get('query')
        print("query",query)
        ###
        hits = qdrant.search(
        collection_name="functioncall",
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
        #print("functions:",functions)

        ##
        prompt = generate_functions_prompt(query,functions=functions)
        result = generate(prompt)
        
        print("result",result)

        import re

        def extract_all_parameters(data_string):
            # Extracting function parameters using regex
            match = re.match(r'(\w+)\(([^)]*)\)', data_string)
            
            print("match",match)

            if match:
                parameters = match.group(2)

                print("parameters",parameters)

                # Splitting parameters into a dictionary
                parameters_dict = dict(re.findall(r'(\w+)=("[^"]*"|[^,)]*)', parameters))

                json_data = {key: value.strip('"') for key, value in parameters_dict.items()}
                # json_data = {key: value for key, value in parameters_dict.items()}
        
                return json_data
            else:
                return data_string

        transformed_data = extract_all_parameters(result)
        print("transformed_data",transformed_data)
        return jsonify(transformed_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)


