from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.database import Base

class BacktestResult(Base):
    __tablename__ = "backtest_results"
    
    id = Column(Integer, primary_key=True, index=True)
    strategy_id = Column(Integer, ForeignKey("strategies.id"), nullable=False)
    strategy = relationship("Strategy", backref="backtest_results")
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    total_return = Column(Float)
    annual_return = Column(Float)
    sharpe_ratio = Column(Float)
    max_drawdown = Column(Float)
    volatility = Column(Float)
    win_rate = Column(Float)
    avg_win = Column(Float)
    avg_loss = Column(Float)
    trade_count = Column(Integer)
    status = Column(String, default="completed")  # running, completed, failed
    logs = Column(Text)  # 回测日志
    created_at = Column(DateTime(timezone=True), server_default=func.now())
