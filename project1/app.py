from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['question']
    
    completion = client.chat.completions.create(
        model="google/codegemma-1.1-7b",
        messages=[{"role": "user", "content": user_input}],
        temperature=0.2,
        top_p=0.7,
        max_tokens=1024,
        stream=True
    )
    
    answer = ""
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            answer += chunk.choices[0].delta.content

    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)