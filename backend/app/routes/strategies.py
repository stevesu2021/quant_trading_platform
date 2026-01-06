from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.db.database import get_db
from app.models.strategy import Strategy
from app.schemas.strategy import StrategyCreate, StrategyUpdate, Strategy as StrategySchema
from app.services.qlib_service import QLibService

router = APIRouter()

@router.get("", response_model=List[StrategySchema])
def get_strategies(
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    name: Optional[str] = None,
    type: Optional[str] = None,
    status: Optional[str] = None
):
    """获取策略列表"""
    query = db.query(Strategy)
    
    if name:
        query = query.filter(Strategy.name == name)
    if type:
        query = query.filter(Strategy.type == type)
    if status:
        query = query.filter(Strategy.status == status)
    
    strategies = query.offset(skip).limit(limit).all()
    return strategies

@router.get("/{strategy_id}", response_model=StrategySchema)
def get_strategy(strategy_id: int, db: Session = Depends(get_db)):
    """获取单个策略信息"""
    strategy = db.query(Strategy).filter(Strategy.id == strategy_id).first()
    if not strategy:
        raise HTTPException(status_code=404, detail="Strategy not found")
    return strategy

@router.post("", response_model=StrategySchema, status_code=201)
def create_strategy(strategy: StrategyCreate, db: Session = Depends(get_db)):
    """创建策略"""
    # 检查策略名称是否已存在
    existing_strategy = db.query(Strategy).filter(Strategy.name == strategy.name).first()
    if existing_strategy:
        raise HTTPException(status_code=400, detail="Strategy name already exists")
    
    db_strategy = Strategy(**strategy.dict())
    db.add(db_strategy)
    db.commit()
    db.refresh(db_strategy)
    return db_strategy

@router.put("/{strategy_id}", response_model=StrategySchema)
def update_strategy(strategy_id: int, strategy_update: StrategyUpdate, db: Session = Depends(get_db)):
    """更新策略信息"""
    db_strategy = db.query(Strategy).filter(Strategy.id == strategy_id).first()
    if not db_strategy:
        raise HTTPException(status_code=404, detail="Strategy not found")
    
    update_data = strategy_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_strategy, field, value)
    
    db.commit()
    db.refresh(db_strategy)
    return db_strategy

@router.delete("/{strategy_id}", status_code=204)
def delete_strategy(strategy_id: int, db: Session = Depends(get_db)):
    """删除策略"""
    db_strategy = db.query(Strategy).filter(Strategy.id == strategy_id).first()
    if not db_strategy:
        raise HTTPException(status_code=404, detail="Strategy not found")
    
    db.delete(db_strategy)
    db.commit()
    return None

@router.post("/run/{strategy_id}")
def run_strategy(strategy_id: int, db: Session = Depends(get_db)):
    """运行策略"""
    strategy = db.query(Strategy).filter(Strategy.id == strategy_id).first()
    if not strategy:
        raise HTTPException(status_code=404, detail="Strategy not found")
    
    try:
        qlib_service = QLibService()
        result = qlib_service.run_strategy(strategy.config_path)
        return {"message": "Strategy run successfully", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to run strategy: {str(e)}")
