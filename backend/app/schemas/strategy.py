from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class StrategyBase(BaseModel):
    name: str = Field(..., description="策略名称")
    description: Optional[str] = Field(None, description="策略描述")
    type: str = Field(..., description="策略类型")
    config_path: Optional[str] = Field(None, description="配置文件路径")
    status: Optional[str] = Field("active", description="策略状态")

class StrategyCreate(StrategyBase):
    pass

class StrategyUpdate(BaseModel):
    name: Optional[str] = Field(None, description="策略名称")
    description: Optional[str] = Field(None, description="策略描述")
    type: Optional[str] = Field(None, description="策略类型")
    config_path: Optional[str] = Field(None, description="配置文件路径")
    status: Optional[str] = Field(None, description="策略状态")

class Strategy(StrategyBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]
    
    class Config:
        from_attributes = True
