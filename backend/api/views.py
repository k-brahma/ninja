from typing import List

from accounts.auth import BearerAuth  # 共通モジュールからインポート
from django.contrib.auth.models import User

from ninja import Router

from .models import Post
from .schemas import PostSchema

router = Router()


@router.get("/posts", response=List[PostSchema])  # PostSchemaを使用
def list_posts(request):
    posts = Post.objects.all()
    # Postオブジェクトをそのまま返すとDjango NinjaがPostSchemaに変換する際にエラーが発生するため、
    # 手動で変換してから返す
    return [
        PostSchema(
            id=post.id,
            title=post.title,
            content=post.content,
            author=post.author.username,  # ユーザー名を文字列として取得
            created_at=post.created_at,
        )
        for post in posts
    ]


@router.get("/myposts", response=List[PostSchema], auth=BearerAuth())  # 認証を追加
def my_posts(request):
    # ユーザーが認証されていることが保証されている
    posts = Post.objects.filter(author=request.auth)
    return [
        PostSchema(
            id=post.id,
            title=post.title,
            content=post.content,
            author=post.author.username,
            created_at=post.created_at,
        )
        for post in posts
    ]


@router.post("/posts", response=PostSchema, auth=BearerAuth())  # 認証を追加
def create_post(request, title: str, content: str):
    post = Post.objects.create(title=title, content=content, author=request.auth)
    return PostSchema(
        id=post.id,
        title=post.title,
        content=post.content,
        author=post.author.username,
        created_at=post.created_at,
    )
