# ベースイメージ
FROM python:3.9

# 作業ディレクトリを設定
WORKDIR /code

# 依存関係をコピーしてインストール
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードをコピー
COPY . /code/

# 起動スクリプトに実行権限を付与
COPY entrypoint.sh /code/
RUN chmod +x /code/entrypoint.sh

# 起動スクリプトを実行
CMD ["/code/entrypoint.sh"]