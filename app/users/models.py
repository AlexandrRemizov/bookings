from sqlalchemy import Integer, Column, String

from app.database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)

    def __str__(self):
        return f"Пользователь {self.email}"
