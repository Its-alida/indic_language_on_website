**Indic Language Support for Websites**

**Introduction:**
This project aims to provide Indic language support for websites by enabling dynamic translation of content from English to Indic languages, initially focusing on Hindi.

**Features:**
- Dynamic translation of website content from English to Hindi.
- Seamless integration into existing web pages.
- User-friendly interface for triggering translation.

**Constraints:**
- Translation accuracy is low

**Requirements:**
- Python 3.x
- Flask
- Hugging Face `transformers` library
- BeautifulSoup (for HTML parsing)

**Setup Instructions:**
1. Clone the repository to your local machine:

```bash
git clone  https://github.com/Its-alida/indic_language_on_website.git
```

2. Install dependencies using pip:

```bash
pip install -r requirements.txt
```

3. Start the Flask server:

```bash
python app.py
```

4. Access the application in your web browser at `http://localhost:5000`.

**Usage:**
- Navigate to the webpage you want to translate.
- Click the "Translate" button to initiate translation.
- The webpage content will be dynamically translated from English to Hindi.
