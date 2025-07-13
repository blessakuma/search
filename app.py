from flask import Flask, render_template, request
from duckduckgo_search import DDGS
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

def get_page_excerpt(url, max_chars=300):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        resp = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(resp.text, 'html.parser')

        # Ищем текст в <p> или fallback
        paragraphs = soup.find_all('p')
        text = ''
        for p in paragraphs:
            text += p.get_text(strip=True) + ' '
            if len(text) >= max_chars:
                break
        return text.strip()[:max_chars] + '...'
    except Exception as e:
        return "❌ Не удалось получить описание."

def search_web(query, max_results=5):
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            excerpt = get_page_excerpt(r['href'])
            results.append({
                'title': r['title'],
                'link': r['href'],
                'excerpt': excerpt
            })
    return results

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    query = ''
    if request.method == 'POST':
        query = request.form.get('query')
        if query:
            results = search_web(query)
    return render_template('index.html', query=query, results=results)

if __name__ == '__main__':
    app.run(debug=True)
