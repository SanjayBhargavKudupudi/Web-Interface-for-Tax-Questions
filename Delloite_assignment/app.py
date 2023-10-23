from flask import Flask, render_template, request, jsonify
import openai

# Initialize OpenAI API
openai.api_key = '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'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_question():
    question = request.form.get('question')
    
    if not question:
        return jsonify({"error": "Please provide a question"}), 400

    # Interacting with OpenAI Model
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Tax-related question: {question}\nAnswer:",
        max_tokens=150
    )
    
    return jsonify({"answer": response.choices[0].text.strip()})

if __name__ == '__main__':
    app.run(debug=True)
