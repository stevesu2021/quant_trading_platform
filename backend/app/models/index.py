from sqlalchemy import Column, Integer, String, Float, Date
from app.db.database import Base

class Index(Base):
    __tablename__ = "indices"
    
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String)
    base_value = Column(Float)
    current_value = Column(Float)
    change = Column(Float)
    change_percent = Column(Float)
    market_cap = Column(Float)
    constituent_count = Column(Integer)
    launch_date = Column(Date)
    last_updated = Column(Date)
