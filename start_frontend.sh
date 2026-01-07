#!/bin/bash

# 启动前端服务脚本
echo "启动前端服务..."

# 切换到前端目录
cd /home/steve/workspace/quant_trading_platform/frontend || {
    echo "前端目录不存在"
    exit 1
}

# 安装依赖
echo "检查并安装依赖..."
npm install

# 启动前端服务，使用3000端口
echo "前端服务将在 http://localhost:3000 启动"
npm start
