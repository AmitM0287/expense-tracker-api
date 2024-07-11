from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Double, ForeignKey, Sequence
from datetime import datetime

Base = declarative_base()


class AuthUser(Base):
    __tablename__ = 'auth_user'

    id = Column(Integer, Sequence('auth_user_id_seq'), primary_key=True)
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    email = Column(String(256), nullable=False) 
    username = Column(String(256), nullable=False)
    password = Column(String(128), nullable=False)
    date_joined = Column(DateTime(timezone=True), default=datetime.now())
    created_by = Column(Integer, nullable=False)
    updated_date = Column(DateTime(timezone=True))
    updated_by = Column(Integer)
    is_superuser = Column(Boolean, default=False)
    is_staff = Column(Boolean, default=True)
    is_active = Column(Boolean, default=True)
    last_login = Column(DateTime(timezone=True), default=datetime.now())


class InvestmentType(Base):
    __tablename__ = 'investment_type'

    id = Column(Integer, Sequence('investment_type_id_seq'), primary_key=True)
    type_name = Column(String(64), nullable=False)      # MF / FD / NPS / Savings
    fund_name = Column(String(128), nullable=False)     # Axis Small Cap / ICICI
    fund_category = Column(String(64), nullable=False)  # Small Cap / Index / ETF / Bank
    fund_type = Column(String(64), nullable=False)      # Equity / Debt / Emergency
    app_name = Column(String(64), nullable=False)       # Groww / NPS
    created_date = Column(DateTime(timezone=True), default=datetime.now())
    created_by = Column(Integer, nullable=False)
    updated_date = Column(DateTime(timezone=True))
    updated_by = Column(Integer)
    is_active = Column(Boolean, default=True)
    is_trash = Column(Boolean, default=False)


class Investment(Base):
    __tablename__ = 'investment'

    id = Column(Integer, Sequence('investment_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('auth_user.id'))
    investment_type_id = Column(Integer, ForeignKey('investment_type.id'))
    day = Column(Integer, nullable=False)
    month = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    investment_amount = Column(Integer, default=0)
    total_invested = Column(Integer, default=0)
    total_percent_returns = Column(Double(precision=2), default=0)
    expense_ratio = Column(Double(precision=2), default=0)
    created_date = Column(DateTime(timezone=True), default=datetime.now())
    created_by = Column(Integer, nullable=False)
    updated_date = Column(DateTime(timezone=True))
    updated_by = Column(Integer)
    is_active = Column(Boolean, default=True)
    is_trash = Column(Boolean, default=False)


class CreditExpense(Base):
    __tablename__ = 'credit_expense'

    id = Column(Integer, Sequence('credit_expense_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('auth_user.id'))
    day = Column(Integer, nullable=False)
    month = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    amount = Column(Integer, default=0)
    category = Column(String(64), nullable=False)   # Medicine / Salary 
    source = Column(String(128), nullable=False)    # Salary / Referal / Flipkart
    is_credited = Column(Boolean, default=False)
    created_date = Column(DateTime(timezone=True), default=datetime.now())
    created_by = Column(Integer, nullable=False)
    updated_date = Column(DateTime(timezone=True))
    updated_by = Column(Integer)
    is_active = Column(Boolean, default=True)
    is_trash = Column(Boolean, default=False)

