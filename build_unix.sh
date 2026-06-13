#!/usr/bin/env bash
# macOS / Linux 用ビルドスクリプト
# 生成物: dist/kenpo-support
set -e
cd "$(dirname "$0")"

python3 -m pip install -r requirements.txt -r requirements-build.txt
python3 -m PyInstaller --noconfirm kenpo-support.spec

echo
echo "ビルド完了: dist/KenpoAssist"
echo "配布時は dist/KenpoAssist を渡してください。"
