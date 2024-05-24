from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, func, MetaData

Base = declarative_base()
metadata = Base.metadata

class UserModel(Base):
  __tablename__ = "users"
  
  id = Column(Integer, primary_key=True)
  name = Column(String(60))
  email = Column(String(30), unique=True)
  password = Column(String(60))
  created_at = Column(DateTime, default=func.now())
  updated_at = Column(DateTime, server_default=func.now(), onupdate=func.current_timestamp())
  
  def __repr__(self):
    return f"id: {self.id}, name: {self.name}"