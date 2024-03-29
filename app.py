from flask import Flask, render_template, request, jsonify
from transformers import MarianMTModel, MarianTokenizer
from bs4 import BeautifulSoup

app = Flask(__name__)

model_name = 'Helsinki-NLP/opus-mt-en-hi'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():

    data = request.get_json()
    html_content = data['htmlContent']

    soup = BeautifulSoup(html_content, 'html.parser')

    for tag in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'span','li']):

        english_text = tag.get_text()
        english_tokens = tokenizer.encode(english_text, return_tensors="pt")
        translated_tokens = model.generate(english_tokens)
        translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
        tag.string.replace_with(translated_text)

    translated_html = str(soup)

    return jsonify({'translatedHTML': translated_html})

if __name__ == '__main__':
    app.run(debug=True)
