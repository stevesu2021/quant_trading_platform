from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import stocks, indices, strategies, backtest_results
from app.db.database import engine, Base

# 创建数据库表
Base.metadata.create_all(bind=engine)

# 初始化FastAPI应用
app = FastAPI(
    title="Quant Platform API",
    description="量化策略平台API",
    version="1.0.0"
)

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 在生产环境中应设置具体的前端URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(stocks.router, prefix="/api/stocks", tags=["stocks"])
app.include_router(indices.router, prefix="/api/indices", tags=["indices"])
app.include_router(strategies.router, prefix="/api/strategies", tags=["strategies"])
app.include_router(backtest_results.router, prefix="/api/backtest-results", tags=["backtest_results"])

@app.get("/")
def read_root():
    return {"message": "Quant Platform API is running"}
