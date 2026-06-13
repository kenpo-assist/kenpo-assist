#!/usr/bin/env python3
"""健保問い合わせサポートシステム ランチャ

ローカルでサーバーを起動し、既定ブラウザで画面を自動的に開きます。
非エンジニアの利用者がダブルクリック相当で起動できることを想定しています。

    python run.py

環境変数 PORT で待受ポートを変更できます（既定: 8765）。
"""
import os
import threading
import webbrowser

import uvicorn

HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", "8765"))


def _open_browser():
    webbrowser.open(f"http://{HOST}:{PORT}/")


if __name__ == "__main__":
    # サーバー起動直後にブラウザを開く（起動待ちのため少し遅延）
    threading.Timer(1.5, _open_browser).start()
    print(f"健保問い合わせサポートシステムを起動します → http://{HOST}:{PORT}/")
    print("終了するには Ctrl+C を押してください。")
    uvicorn.run("main:app", host=HOST, port=PORT, log_level="info")
