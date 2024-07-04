from flask import Flask, request, render_template
from openai import OpenAI

app = Flask(__name__)

# Initialize the OpenAI client
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']
    
    # Create completion
    completion = client.chat.completions.create(
        model="meta/llama3-70b-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        top_p=1,
        max_tokens=1024,
        stream=True
    )
    
    response = ""
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            response += chunk.choices[0].delta.content

    return render_template('index.html', prompt=prompt, response=response)

if __name__ == '__main__':
    app.run(debug=True)
