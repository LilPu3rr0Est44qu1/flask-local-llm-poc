from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        prompt = request.form.get('prompt', '')
        
        # OllamaのローカルAPIを叩く
        try:
            res = requests.post('http://localhost:11434/api/generate', json={
                'model': 'llama3.1', # 使っているモデル名に書き換えてOK
                'prompt': prompt,
                'stream': False
            })
            result = res.json().get('response', '生成に失敗しました')
        except Exception as e:
            result = f"エラー: {str(e)}"
            
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)