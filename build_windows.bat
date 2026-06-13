@echo off
REM Windows 用ビルドスクリプト
REM 生成物: dist\KenpoAssist.exe
REM ※ Windows向けexeはWindows上でビルドする必要があります（クロスビルド不可）。
cd /d "%~dp0"

python -m pip install -r requirements.txt -r requirements-build.txt
if errorlevel 1 goto :error

python -m PyInstaller --noconfirm kenpo-support.spec
if errorlevel 1 goto :error

echo.
echo ビルド完了: dist\KenpoAssist.exe
echo 配布時は dist\KenpoAssist.exe を渡してください。
goto :eof

:error
echo.
echo ビルドに失敗しました。Python と pip が利用可能か確認してください。
exit /b 1
