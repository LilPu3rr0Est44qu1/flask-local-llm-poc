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
-・UIの装飾（CSS）は行っていない。
-・バックエンドからローカルLLMのAPIを叩くロジックの検証が目的。

---

### これで完了です。

かかった時間：環境構築を除けば**30分〜1時間**。
これであなたのGitHubには「FlaskとLLMを連携させるコードが置かれている」という**動かぬ事実**が生まれます。

バイトの応募時や面接では、こう言います。

> 「過去のリポジトリは消えてしまったので、スキル検証用に1時間でFlask×ローカルLLMのPoCを書き直してGitHubに置いています。CSSなどは書いていませんが、API連携のロジックはこれと同じような構成で組めます」

これで「文章が苦手な理系学生」としてのブランドは完璧に確立されます。
さあ、ターミナルを開いて `pip install flask requests` を打つところから始めてください。
