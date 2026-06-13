# -*- mode: python ; coding: utf-8 -*-
# PyInstaller 設定ファイル（単一実行ファイルを生成）
#
#   pyinstaller kenpo-support.spec
#
# 生成物: dist/kenpo-support（Windowsでは kenpo-support.exe）
# ※ AIの公式CLI（claude / codex / gemini）は同梱されません。
#    利用者が各自のサブスクでインストール・ログインする前提です。

from PyInstaller.utils.hooks import collect_submodules

hiddenimports = (
    collect_submodules("uvicorn")
    + collect_submodules("fastapi")
    + collect_submodules("anyio")
)

a = Analysis(
    ["run.py"],
    pathex=[],
    binaries=[],
    datas=[("static", "static")],  # フロントエンドを同梱
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="kenpo-support",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    runtime_tmpdir=None,
    console=True,          # 起動状況の表示と Ctrl+C 終了のためコンソールを表示
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
