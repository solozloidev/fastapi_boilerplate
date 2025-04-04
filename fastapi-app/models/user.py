from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User(Base):
    __tablename__ = "users"
    username: Mapped[int] = mapped_column(unique=True)
