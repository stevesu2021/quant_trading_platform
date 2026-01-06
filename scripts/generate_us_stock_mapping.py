
import yfinance as yf
import pandas as pd
import os

# 获取当前脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))
# 定义输出文件路径
output_file = os.path.join(script_dir, "us_stock_code_name.csv")

# 定义代表性美股股票列表
# 这里使用一些知名的美股股票作为示例
us_stocks = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "TSLA",
    "META", "NVDA", "JPM", "V", "WMT",
    "PG", "KO", "JNJ", "PFE", "MRK",
    "DIS", "NFLX", "INTC", "CSCO", "ORCL",
    "IBM", "AMD", "BA", "CAT", "GE",
    "XOM", "CVX", "COP", "SLB", "OXY"
]

# 获取股票名称数据
data = []
for symbol in us_stocks:
    try:
        stock = yf.Ticker(symbol)
        data.append({
            "code": symbol,
            "name": stock.info.get("longName", symbol)
        })
    except Exception as e:
        print(f"获取{symbol}数据失败: {e}")
        data.append({
            "code": symbol,
            "name": symbol
        })

# 保存到CSV文件
df = pd.DataFrame(data)
df.to_csv(output_file, index=False)
print(f"美股股票编码与名称映射已生成，保存至: {output_file}")
