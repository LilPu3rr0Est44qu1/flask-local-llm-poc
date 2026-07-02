# Flask x Local LLM (Ollama) PoC

## 概要
- 過去のローカル環境の紛失に伴い、スキル検証用に短期間で構築した概念実証（PoC）コード。
- ローカルGPU (RTX 4060) で動作する Ollama を Flask から API 経由で呼び出し、テキスト生成を行う。

## 技術スタック
- **Backend:** Python, Flask
- **AI/LLM:** Ollama (llama3.1)
- **Environment:** Windows, RTX 4060 Laptop GPU

## 実行方法
1. Ollama をインストールし、モデルをプルする。
   ```bash
   ollama pull llama3.1
2. 依存パッケージをインストールする。
   ```bash
   pip install flask requests
3. サーバーを起動する。
   ```bash
   python app.py
4. http://localhost:5000にアクセス。

## 備考
- **UIの装飾（CSS）は行っていない。**
- **・バックエンドからローカルLLMのAPIを叩くロジックの検証が目的。**
