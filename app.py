from flask import Flask, render_template, request
import requests

app = Flask(__name__)

NEWS_API_KEY = 'b7853b306e014614946d67381a53893e'  # 你的 NewsAPI API Key

@app.route('/')
def home():
    return render_template('index.html')  # 渲染首頁 HTML 頁面

@app.route('/api/everything', methods=['GET'])
def search_everything():
    query = request.args.get('query') or 'news'
    category = request.args.get('category')

    # 如果有選擇分類，將分類加入到關鍵字中進行搜索
    if category:
        query += f' {category}'

    params = {
        'apiKey': NEWS_API_KEY,
        'q': query,
        'language': 'zh'  # 可以根據需要更改語言
    }

    response = requests.get('https://newsapi.org/v2/everything', params=params)
    data = response.json()
    return {'articles': data.get('articles', [])}


@app.route('/api/top-headlines', methods=['GET'])
def search_us_news():
    query = request.args.get('query') or 'news'
    category = request.args.get('category') or None
    country = request.args.get('country') or 'us'  # 默認國家為 'us'

    params = {
        'apiKey': NEWS_API_KEY,
        'q': query,
        'country': country  # 使用傳入的國家，或默認為 'us'
    }

    if category:
        params['category'] = category

    response = requests.get('https://newsapi.org/v2/top-headlines', params=params)
    data = response.json()
    return {'articles': data.get('articles', [])}

if __name__ == '__main__':
    app.run(debug=True)
