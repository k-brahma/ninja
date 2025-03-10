from typing import List

from django.contrib.auth.models import User

from ninja import Router

from .models import Post, PostSchema  # PostSchemaをインポート
from .schemas import PostSchema  # PostSchemaをインポート

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


@router.get("/myposts", response=List[PostSchema])  # PostSchemaを使用
def my_posts(request):
    posts = Post.objects.filter(author=request.user)
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


@router.post("/posts", response=PostSchema)  # 作成したPostを返す場合は、responseを指定
def create_post(request, title: str, content: str):
    post = Post.objects.create(title=title, content=content, author=request.user)
    return PostSchema(
        id=post.id,
        title=post.title,
        content=post.content,
        author=post.author.username,
        created_at=post.created_at,
    )
