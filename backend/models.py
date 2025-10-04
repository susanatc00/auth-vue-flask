 
from sqlalchemy import Column, Integer, String, DateTime, func, UniqueConstraint
from database import Base
from passlib.hash import bcrypt

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), nullable=False, unique=True, index=True)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (UniqueConstraint('email', name='uq_users_email'),)

    # Helpers
    @staticmethod
    def hash_password(password: str) -> str:
        return bcrypt.hash(password)

    def verify_password(self, password: str) -> bool:
        return bcrypt.verify(password, self.password_hash)
