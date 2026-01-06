from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class StockBase(BaseModel):
    symbol: str = Field(..., description="股票代码")
    name: str = Field(..., description="股票名称")
    sector: Optional[str] = Field(None, description="行业")
    industry: Optional[str] = Field(None, description="板块")
    market_cap: Optional[float] = Field(None, description="市值")
    price: Optional[float] = Field(None, description="当前价格")
    change: Optional[float] = Field(None, description="涨跌额")
    change_percent: Optional[float] = Field(None, description="涨跌幅")
    volume: Optional[int] = Field(None, description="成交量")
    pe_ratio: Optional[float] = Field(None, description="市盈率")
    pb_ratio: Optional[float] = Field(None, description="市净率")
    listing_date: Optional[date] = Field(None, description="上市日期")

class StockCreate(StockBase):
    pass

class StockUpdate(BaseModel):
    name: Optional[str] = Field(None, description="股票名称")
    sector: Optional[str] = Field(None, description="行业")
    industry: Optional[str] = Field(None, description="板块")
    market_cap: Optional[float] = Field(None, description="市值")
    price: Optional[float] = Field(None, description="当前价格")
    change: Optional[float] = Field(None, description="涨跌额")
    change_percent: Optional[float] = Field(None, description="涨跌幅")
    volume: Optional[int] = Field(None, description="成交量")
    pe_ratio: Optional[float] = Field(None, description="市盈率")
    pb_ratio: Optional[float] = Field(None, description="市净率")

class Stock(StockBase):
    id: int
    last_updated: date
    
    class Config:
        from_attributes = True
