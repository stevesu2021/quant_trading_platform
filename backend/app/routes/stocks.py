from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.db.database import get_db
from app.models.stock import Stock
from app.schemas.stock import StockCreate, StockUpdate, Stock as StockSchema

router = APIRouter()

@router.get("", response_model=List[StockSchema])
def get_stocks(
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    symbol: Optional[str] = None,
    sector: Optional[str] = None
):
    """获取股票列表"""
    query = db.query(Stock)
    
    if symbol:
        query = query.filter(Stock.symbol == symbol)
    if sector:
        query = query.filter(Stock.sector == sector)
    
    stocks = query.offset(skip).limit(limit).all()
    return stocks

@router.get("/{stock_id}", response_model=StockSchema)
def get_stock(stock_id: int, db: Session = Depends(get_db)):
    """获取单个股票信息"""
    stock = db.query(Stock).filter(Stock.id == stock_id).first()
    if not stock:
        raise HTTPException(status_code=404, detail="Stock not found")
    return stock

@router.post("", response_model=StockSchema, status_code=201)
def create_stock(stock: StockCreate, db: Session = Depends(get_db)):
    """创建股票"""
    # 检查股票代码是否已存在
    existing_stock = db.query(Stock).filter(Stock.symbol == stock.symbol).first()
    if existing_stock:
        raise HTTPException(status_code=400, detail="Stock symbol already exists")
    
    db_stock = Stock(**stock.dict())
    db.add(db_stock)
    db.commit()
    db.refresh(db_stock)
    return db_stock

@router.put("/{stock_id}", response_model=StockSchema)
def update_stock(stock_id: int, stock_update: StockUpdate, db: Session = Depends(get_db)):
    """更新股票信息"""
    db_stock = db.query(Stock).filter(Stock.id == stock_id).first()
    if not db_stock:
        raise HTTPException(status_code=404, detail="Stock not found")
    
    update_data = stock_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_stock, field, value)
    
    db.commit()
    db.refresh(db_stock)
    return db_stock

@router.delete("/{stock_id}", status_code=204)
def delete_stock(stock_id: int, db: Session = Depends(get_db)):
    """删除股票"""
    db_stock = db.query(Stock).filter(Stock.id == stock_id).first()
    if not db_stock:
        raise HTTPException(status_code=404, detail="Stock not found")
    
    db.delete(db_stock)
    db.commit()
    return None
