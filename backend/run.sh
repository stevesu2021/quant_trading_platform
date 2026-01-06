#!/bin/bash

# 激活conda环境
source activate qlib

# 进入后端目录
cd /home/steve/workspace/quant_platform_qlib/backend

# 安装依赖（如果需要）
pip install -r requirements.txt

# 启动FastAPI服务
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
