from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import expression

from src.core.types.user.gender import GenderType
from src.database import BaseModel
from src.models.types import created_at, updated_at, uuid_pk


class UserModel(BaseModel):
    __tablename__ = "user"

    id: Mapped[uuid_pk]
    email: Mapped[str] = mapped_column(
        String(length=320), unique=True, comment="Email адрес пользователя"
    )
    gender: Mapped[GenderType]
    hashed_password: Mapped[str] = mapped_column(String(1024))
    is_active: Mapped[bool] = mapped_column(server_default=expression.true())
    is_verified: Mapped[bool] = mapped_column(server_default=expression.false())
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
