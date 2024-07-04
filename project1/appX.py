from flask import Flask, request, jsonify, render_template
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

app = Flask(__name__)

# Load the model and tokenizer
model_name = "Salesforce/codegen-350M-mono"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Function to generate code
def generate_code(prompt, max_length=150):
    try:
        inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
        input_ids = inputs["input_ids"]
        attention_mask = inputs["attention_mask"]
        
        outputs = model.generate(
            input_ids=input_ids, 
            attention_mask=attention_mask, 
            max_length=max_length, 
            pad_token_id=tokenizer.eos_token_id,
            num_return_sequences=1
        )
        
        generated_code = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return generated_code
    except Exception as e:
        return str(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.get_json()
        description = data.get('description', '')
        code = generate_code(description)
        return jsonify({"code": code})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
