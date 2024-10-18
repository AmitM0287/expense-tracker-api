from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Double, ForeignKey, Sequence
from datetime import datetime

Base = declarative_base()

class AuthUser(Base):
	__tablename__ = 'auth_user'

	id = Column(Integer, Sequence('auth_user_id_seq'), primary_key=True)
	first_name = Column(String(64), nullable=False)
	last_name = Column(String(64), nullable=False)
	username = Column(String(256), nullable=False)
	email = Column(String(256), nullable=False) 
	password = Column(String(128), nullable=False)
	date_joined = Column(DateTime(timezone=True), default=datetime.now())
	created_by = Column(Integer, nullable=False)
	updated_date = Column(DateTime(timezone=True))
	updated_by = Column(Integer)
	is_superuser = Column(Boolean, default=False)
	is_staff = Column(Boolean, default=True)
	is_active = Column(Boolean, default=True)
	last_login = Column(DateTime(timezone=True), default=datetime.now())
