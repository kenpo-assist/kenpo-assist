# ケンポアシスト ランディングページ（販売HP）

`index.html` 単体で完結する静的ページです。外部ライブラリ・画像に依存しません。
そのままWebサーバーにアップロードするか、ローカルでブラウザで開けば表示できます。

## 公開前に差し替える3か所（プレースホルダ）

1. **価格** — `index.html` 内の `<!-- TODO: 価格を確定後に... -->` の直後
   `<div class="price-amt"><small>¥</small>XX,XXX</div>` を実際の金額に。
2. **問い合わせフォームの送信先** — `<form ... action="https://formspree.io/f/YOUR_FORM_ID">`
   - 例: [Formspree](https://formspree.io/) や [Getform](https://getform.io/) で無料のフォームエンドポイントを取得し、`action` に貼る。
   - JSON応答（`Accept: application/json`）に対応済み。エンドポイント未設定のままだと送信時に注意メッセージが出ます。
3. **フッターの著作権表記** — 必要に応じて社名等に調整。

## ローカルでの確認

```bash
cd landing
python3 -m http.server 8080
# ブラウザで http://localhost:8080/ を開く
```

## 公開（ホスティング）の例

- 静的ホスティング（Netlify / Cloudflare Pages / GitHub Pages / S3 など）に `index.html` を置くだけ。
- 独自ドメインを割り当てれば「専用HP」として運用できます。

## 備考

- デザインはアプリ本体と同系統のブルー（#1a5fa8）に統一しています。
- 記載内容は製品の実態（3AI選択・ローカル保存・買い切り席単位・個人利用前提）に合わせています。
  仕様変更時は本文も更新してください。
