import logging

from ninja.security import HttpBearer

# ロガーのセットアップ
logger = logging.getLogger(__name__)

# 共有トークンストレージ（本番環境ではデータベースやRedisなどを使用すべき）
tokens = {}


class BearerAuth(HttpBearer):
    def authenticate(self, request, token):
        logger.info(f"認証リクエスト - トークン: {token}")
        logger.info(f"現在のトークン一覧: {list(tokens.keys())}")

        if token in tokens:
            user = tokens[token]
            logger.info(f"認証成功 - ユーザー: {user.username}, ID: {user.id}")
            return user
        else:
            logger.warning(f"認証失敗 - トークンが見つかりません: {token}")
            return None

    def __call__(self, request):
        logger.info(f"認証呼び出し - パス: {request.path}")
        logger.info(f"認証ヘッダー: {request.headers.get('Authorization', 'なし')}")
        return super().__call__(request)
