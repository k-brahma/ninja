from datetime import datetime

from pydantic import BaseModel


class PostSchema(BaseModel):
    id: int
    title: str
    content: str
    author: str  # Userモデルからユーザー名を取得
    created_at: datetime  # datetimeとして扱う

    model_config = {"from_attributes": True, "arbitrary_types_allowed": True}
