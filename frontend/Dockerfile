# ベースイメージ
FROM node:14

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係をコピーしてインストール
COPY package.json package-lock.json ./
RUN npm install

# アプリケーションコードをコピー
COPY . .

# サーバーを起動
CMD ["npm", "run", "dev"] 