**Indic Language Support for Websites**

***src="https://www.youtube.com/embed/flITEsE9R2g?si=Fiw6b6yH9QyoyXR_"***


**Introduction:**
This project aims to provide Indic language support for websites by enabling dynamic translation of content from English to Indic languages, initially focusing on Hindi.

**Features:**
- Free of cost
- Dynamic translation of website content from English to Hindi.
- Seamless integration into existing web pages.
- User-friendly interface for triggering translation.

**Constraints:**
- Translation accuracy
- Response time 

**Requirements:**
- Python 3.x
- Flask
- Hugging Face `transformers` library
- BeautifulSoup (for HTML parsing)
- Transformers
- Sentencepiece
- Pytorch

**Setup Instructions:**
1. Clone the repository to your local machine:

```bash
git clone  https://github.com/Its-alida/indic_language_on_website.git
```

2. Install dependencies using pip:

```bash
pip install -r requirements.txt
```
Or install the modules independently using ```pip install <module_name>```

3. Start the Flask server:

```bash
python app.py
```

To be able to dynamically translate , you need to access your webpage not by running ```index.html``` directly but only through flask server . First start flask server by ```python app.py```
and once you go to the link it shows , you can access the site.

4. Access the application in your web browser at `http://localhost:5000`.

**Usage:**
- Navigate to the webpage on the given address above ```localhost:5000``` , or when your flask servers starts , it gives you the link to follow to access the site.
- Click the "Translate" button to initiate translation.
- The webpage content will be dynamically translated from English to Hindi.
