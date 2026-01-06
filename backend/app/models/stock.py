from sqlalchemy import Column, Integer, String, Float, Date
from app.db.database import Base

class Stock(Base):
    __tablename__ = "stocks"
    
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    sector = Column(String)
    industry = Column(String)
    market_cap = Column(Float)
    price = Column(Float)
    change = Column(Float)
    change_percent = Column(Float)
    volume = Column(Integer)
    pe_ratio = Column(Float)
    pb_ratio = Column(Float)
    listing_date = Column(Date)
    last_updated = Column(Date)
