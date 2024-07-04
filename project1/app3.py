from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer

app = Flask(__name__)

# Load the model and tokenizer
model_name = "Salesforce/codegen-350M-mono"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Function to generate code
def generate_code(prompt, max_length=150):
    try:
        inputs = tokenizer(prompt, return_tensors="pt")
        outputs = model.generate(inputs["input_ids"], max_length=max_length, num_return_sequences=1)
        generated_code = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return generated_code
    except Exception as e:
        return str(e)

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
