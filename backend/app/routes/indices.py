from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.db.database import get_db
from app.models.index import Index
from app.schemas.index import IndexCreate, IndexUpdate, Index as IndexSchema

router = APIRouter()

@router.get("", response_model=List[IndexSchema])
def get_indices(
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    symbol: Optional[str] = None
):
    """获取指数列表"""
    query = db.query(Index)
    
    if symbol:
        query = query.filter(Index.symbol == symbol)
    
    indices = query.offset(skip).limit(limit).all()
    return indices

@router.get("/{index_id}", response_model=IndexSchema)
def get_index(index_id: int, db: Session = Depends(get_db)):
    """获取单个指数信息"""
    index = db.query(Index).filter(Index.id == index_id).first()
    if not index:
        raise HTTPException(status_code=404, detail="Index not found")
    return index

@router.post("", response_model=IndexSchema, status_code=201)
def create_index(index: IndexCreate, db: Session = Depends(get_db)):
    """创建指数"""
    # 检查指数代码是否已存在
    existing_index = db.query(Index).filter(Index.symbol == index.symbol).first()
    if existing_index:
        raise HTTPException(status_code=400, detail="Index symbol already exists")
    
    db_index = Index(**index.dict())
    db.add(db_index)
    db.commit()
    db.refresh(db_index)
    return db_index

@router.put("/{index_id}", response_model=IndexSchema)
def update_index(index_id: int, index_update: IndexUpdate, db: Session = Depends(get_db)):
    """更新指数信息"""
    db_index = db.query(Index).filter(Index.id == index_id).first()
    if not db_index:
        raise HTTPException(status_code=404, detail="Index not found")
    
    update_data = index_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_index, field, value)
    
    db.commit()
    db.refresh(db_index)
    return db_index

@router.delete("/{index_id}", status_code=204)
def delete_index(index_id: int, db: Session = Depends(get_db)):
    """删除指数"""
    db_index = db.query(Index).filter(Index.id == index_id).first()
    if not db_index:
        raise HTTPException(status_code=404, detail="Index not found")
    
    db.delete(db_index)
    db.commit()
    return None
