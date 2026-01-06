from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class IndexBase(BaseModel):
    symbol: str = Field(..., description="指数代码")
    name: str = Field(..., description="指数名称")
    description: Optional[str] = Field(None, description="指数描述")
    base_value: Optional[float] = Field(None, description="基点")
    current_value: Optional[float] = Field(None, description="当前值")
    change: Optional[float] = Field(None, description="涨跌额")
    change_percent: Optional[float] = Field(None, description="涨跌幅")
    market_cap: Optional[float] = Field(None, description="市值")
    constituent_count: Optional[int] = Field(None, description="成分股数量")
    launch_date: Optional[date] = Field(None, description="发布日期")

class IndexCreate(IndexBase):
    pass

class IndexUpdate(BaseModel):
    name: Optional[str] = Field(None, description="指数名称")
    description: Optional[str] = Field(None, description="指数描述")
    current_value: Optional[float] = Field(None, description="当前值")
    change: Optional[float] = Field(None, description="涨跌额")
    change_percent: Optional[float] = Field(None, description="涨跌幅")
    market_cap: Optional[float] = Field(None, description="市值")
    constituent_count: Optional[int] = Field(None, description="成分股数量")

class Index(IndexBase):
    id: int
    last_updated: date
    
    class Config:
        from_attributes = True
