# Djaango Ninja + React Vite

このプロジェクトは、ReactとDjangoを使用したフルスタックアプリケーションです。  
特に、バックエンドにはDjango Ninjaを使用しており、高速で直感的なAPIを目指しています。  
Django Ninjaを使用することで、型安全で高速なAPIを簡単に構築できます。


## 構成

- **フロントエンド**: React, Vite
- **バックエンド**: Django, Django Ninja
- **データベース**: PostgreSQL
- **コンテナ化**: Docker, Docker Compose

## セットアップ

### 必要条件

- Docker
- Docker Compose

### クイックスタート

1. リポジトリをクローンします。
   ```bash
   git clone <リポジトリのURL>
   cd <プロジェクトディレクトリ>
   ```

2. Dockerコンテナをビルドして起動します。
   ```bash
   docker-compose up --build
   ```

3. ブラウザで`http://localhost:3000`にアクセスして、アプリケーションを確認します。

## 使用方法

- フロントエンドの開発サーバーは`http://localhost:3000`で動作します。
- バックエンドのAPIは`http://localhost:8000`で動作します。

## 開発

Docker を使わない フロントエンド/バックエンドの開発は以下の容量で進めてください。

### フロントエンド

フロントエンドの開発を行うには、以下のコマンドを使用します。

```bash
cd frontend
npm install
npm run dev
```

### バックエンド

バックエンドはDjango Ninjaを使用しており、以下のコマンドで開発サーバーを起動できます。

```bash
cd backend
pip install -r requirements.txt
python manage.py runserver
```

## 貢献

貢献を歓迎します。プルリクエストを送信する前に、問題を報告してください。

## ライセンス

このプロジェクトはMITライセンスの下でライセンスされています。 