from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class PortfolioBase(BaseModel):
    name: str = Field(..., description="组合名称")
    description: Optional[str] = Field(None, description="组合描述")
    backtest_result_id: Optional[int] = Field(None, description="回测结果ID")
    total_value: Optional[float] = Field(None, description="总价值")
    cash: Optional[float] = Field(None, description="现金")
    positions_value: Optional[float] = Field(None, description="持仓价值")
    asset_allocation: Optional[str] = Field(None, description="资产配置")

class PortfolioCreate(PortfolioBase):
    pass

class PortfolioUpdate(BaseModel):
    name: Optional[str] = Field(None, description="组合名称")
    description: Optional[str] = Field(None, description="组合描述")
    backtest_result_id: Optional[int] = Field(None, description="回测结果ID")
    total_value: Optional[float] = Field(None, description="总价值")
    cash: Optional[float] = Field(None, description="现金")
    positions_value: Optional[float] = Field(None, description="持仓价值")
    asset_allocation: Optional[str] = Field(None, description="资产配置")

class Portfolio(PortfolioBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]
    
    class Config:
        from_attributes = True
