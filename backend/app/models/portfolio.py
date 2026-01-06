from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.database import Base

class Portfolio(Base):
    __tablename__ = "portfolios"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(Text)
    backtest_result_id = Column(Integer, ForeignKey("backtest_results.id"))
    backtest_result = relationship("BacktestResult", backref="portfolios")
    total_value = Column(Float)
    cash = Column(Float)
    positions_value = Column(Float)
    asset_allocation = Column(Text)  # JSON格式存储资产配置
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
