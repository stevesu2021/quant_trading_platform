from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.db.database import get_db
from app.models.backtest_result import BacktestResult
from app.schemas.backtest_result import BacktestResultCreate, BacktestResultUpdate, BacktestResult as BacktestResultSchema

router = APIRouter()

@router.get("", response_model=List[BacktestResultSchema])
def get_backtest_results(
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    strategy_id: Optional[int] = None,
    status: Optional[str] = None
):
    """获取回测结果列表"""
    query = db.query(BacktestResult)
    
    if strategy_id:
        query = query.filter(BacktestResult.strategy_id == strategy_id)
    if status:
        query = query.filter(BacktestResult.status == status)
    
    results = query.offset(skip).limit(limit).all()
    return results

@router.get("/{result_id}", response_model=BacktestResultSchema)
def get_backtest_result(result_id: int, db: Session = Depends(get_db)):
    """获取单个回测结果"""
    result = db.query(BacktestResult).filter(BacktestResult.id == result_id).first()
    if not result:
        raise HTTPException(status_code=404, detail="Backtest result not found")
    return result

@router.post("", response_model=BacktestResultSchema, status_code=201)
def create_backtest_result(result: BacktestResultCreate, db: Session = Depends(get_db)):
    """创建回测结果"""
    db_result = BacktestResult(**result.dict())
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result

@router.put("/{result_id}", response_model=BacktestResultSchema)
def update_backtest_result(result_id: int, result_update: BacktestResultUpdate, db: Session = Depends(get_db)):
    """更新回测结果"""
    db_result = db.query(BacktestResult).filter(BacktestResult.id == result_id).first()
    if not db_result:
        raise HTTPException(status_code=404, detail="Backtest result not found")
    
    update_data = result_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_result, field, value)
    
    db.commit()
    db.refresh(db_result)
    return db_result

@router.delete("/{result_id}", status_code=204)
def delete_backtest_result(result_id: int, db: Session = Depends(get_db)):
    """删除回测结果"""
    db_result = db.query(BacktestResult).filter(BacktestResult.id == result_id).first()
    if not db_result:
        raise HTTPException(status_code=404, detail="Backtest result not found")
    
    db.delete(db_result)
    db.commit()
    return None
