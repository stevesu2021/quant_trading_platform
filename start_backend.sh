#!/bin/bash

# 启动后端服务脚本
echo "启动后端服务..."

# 切换到后端目录
cd /home/steve/workspace/test_qlib/quant_trading_platform/backend || {
    echo "后端目录不存在"
    exit 1
}

# 启动后端服务，使用8000端口
echo "后端服务将在 http://localhost:8000 启动"
conda run -n qlib uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
