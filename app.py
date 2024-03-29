from flask import Flask, render_template, request, jsonify
from transformers import MarianMTModel, MarianTokenizer
from bs4 import BeautifulSoup

app = Flask(__name__)

# Load translation model and tokenizer
model_name = 'Helsinki-NLP/opus-mt-en-hi'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    # Get HTML content from request data
    data = request.get_json()
    html_content = data['htmlContent']

    # Parse HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Translate text within specific tags (e.g., 'p', 'h1', etc.)
    for tag in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'span','nav','li','ul']):
        # Translate text
        english_text = tag.get_text()
        english_tokens = tokenizer.encode(english_text, return_tensors="pt")
        translated_tokens = model.generate(english_tokens)
        translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
        
        # Update tag with translated text
        tag.string.replace_with(translated_text)

    # Reconstruct translated HTML content
    translated_html = str(soup)

    # Return translated HTML content as JSON response
    return jsonify({'translatedHTML': translated_html})

if __name__ == '__main__':
    app.run(debug=True)
