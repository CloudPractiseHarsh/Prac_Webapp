from sqlalchemy import Column, VARCHAR, DateTime, Integer, Sequence, ForeignKey
from datetime import datetime
from database import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID

# Define a sequence for the id column
user_id_seq = Sequence('user_id_seq')

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, user_id_seq, primary_key=True, server_default=user_id_seq.next_value(), index=True)
    first_name = Column(VARCHAR, index=True)
    last_name = Column(VARCHAR, index=True)
    email = Column(VARCHAR, index=True)
    password = Column(VARCHAR, index=True)
    account_created = Column(DateTime, nullable=False, default=datetime.utcnow)
    account_updated = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<User(id={self.id}, email='{self.email}')>"
    


class ImageMetadata(Base):
    __tablename__ = "image_metadata"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    file_name = Column(VARCHAR, nullable=False)
    url = Column(VARCHAR, nullable=False)
    upload_date = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"<ImageMetadata(id={self.id}, user_id={self.user_id}, file_name='{self.file_name}')>"
