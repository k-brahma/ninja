import logging
import secrets

from django.contrib.auth import authenticate, get_user_model
from django.shortcuts import render
from ninja.security import HttpBearer

from ninja import Router

from .auth import BearerAuth, tokens  # 共通モジュールをインポート
from .schemas import LoginSchema, TokenSchema, UserOut

# ロガーのセットアップ
logger = logging.getLogger(__name__)

auth_router = Router()

# Create your views here.

# 簡易的なトークン認証
# tokens = {}  # 本番環境では、データベースまたはRedisなどを使用してください -> auth.pyに移動

# class BearerAuth(HttpBearer):
#     def authenticate(self, request, token):
#         if token in tokens:
#             return tokens[token]
#         return None -> auth.pyに移動


@auth_router.post("/login", response=TokenSchema)
def login(request, data: LoginSchema):
    logger.info(f"ログイン試行 - メール: {data.email}")
    user = authenticate(email=data.email, password=data.password)
    if user is None:
        logger.warning(f"ログイン失敗 - メール: {data.email}")
        return 401, {"detail": "Invalid email or password"}

    token = secrets.token_hex(16)
    logger.info(f"トークン生成 - ユーザー: {user.username}, トークン: {token}")
    tokens[token] = user
    logger.info(f"現在のトークン数: {len(tokens)}, キー: {list(tokens.keys())}")

    return {"access_token": token, "token_type": "bearer"}


@auth_router.get("/me", response=UserOut, auth=BearerAuth())
def me(request):
    return {"id": request.auth.id, "email": request.auth.email, "username": request.auth.username}


@auth_router.post("/register", response=UserOut)
def register(request, data: LoginSchema):
    User = get_user_model()

    if User.objects.filter(email=data.email).exists():
        return 400, {"detail": "Email already registered"}

    user = User.objects.create_user(
        email=data.email,
        username=data.email.split("@")[0],  # メールアドレスからユーザー名を自動生成
        password=data.password,
    )

    return {"id": user.id, "email": user.email, "username": user.username}
