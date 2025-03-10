# ベースイメージ
FROM node:14

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係をコピーしてインストール
COPY package.json ./
RUN npm install

# アプリケーションコードをコピー
COPY . .

# サーバーを起動
# CMD ["npm", "run", "dev", "--", "--host"] 
CMD ["sh", "-c", "npm install && npm run dev -- --host"]