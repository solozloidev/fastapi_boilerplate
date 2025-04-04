from sqlalchemy import MetaData
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

from config.config import settings


class Base(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(naming_convention=settings.db.naming_convention)

    id: Mapped[int] = mapped_column(primary_key=True)
