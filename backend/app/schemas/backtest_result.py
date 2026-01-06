from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class BacktestResultBase(BaseModel):
    strategy_id: int = Field(..., description="策略ID")
    start_date: Optional[datetime] = Field(None, description="回测开始日期")
    end_date: Optional[datetime] = Field(None, description="回测结束日期")
    total_return: Optional[float] = Field(None, description="总收益率")
    annual_return: Optional[float] = Field(None, description="年化收益率")
    sharpe_ratio: Optional[float] = Field(None, description="夏普比率")
    max_drawdown: Optional[float] = Field(None, description="最大回撤")
    volatility: Optional[float] = Field(None, description="波动率")
    win_rate: Optional[float] = Field(None, description="胜率")
    avg_win: Optional[float] = Field(None, description="平均盈利")
    avg_loss: Optional[float] = Field(None, description="平均亏损")
    trade_count: Optional[int] = Field(None, description="交易次数")
    status: Optional[str] = Field("completed", description="回测状态")
    logs: Optional[str] = Field(None, description="回测日志")

class BacktestResultCreate(BacktestResultBase):
    pass

class BacktestResultUpdate(BaseModel):
    start_date: Optional[datetime] = Field(None, description="回测开始日期")
    end_date: Optional[datetime] = Field(None, description="回测结束日期")
    total_return: Optional[float] = Field(None, description="总收益率")
    annual_return: Optional[float] = Field(None, description="年化收益率")
    sharpe_ratio: Optional[float] = Field(None, description="夏普比率")
    max_drawdown: Optional[float] = Field(None, description="最大回撤")
    volatility: Optional[float] = Field(None, description="波动率")
    win_rate: Optional[float] = Field(None, description="胜率")
    avg_win: Optional[float] = Field(None, description="平均盈利")
    avg_loss: Optional[float] = Field(None, description="平均亏损")
    trade_count: Optional[int] = Field(None, description="交易次数")
    status: Optional[str] = Field(None, description="回测状态")
    logs: Optional[str] = Field(None, description="回测日志")

class BacktestResult(BacktestResultBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True
