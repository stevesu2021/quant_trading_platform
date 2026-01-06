import akshare as ak
import pandas as pd
import os

# 获取当前脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))
# 定义输出文件路径
output_file = os.path.join(script_dir, "stock_code_name.csv")

# 获取映射
df = ak.stock_info_a_code_name()

# 为股票代码添加前缀（上海股票以6开头加SH前缀，深圳股票以0或3开头加SZ前缀）
def add_market_prefix(code):
    code_str = str(code)
    if code_str.startswith('6'):
        return f"SH{code_str}"
    elif code_str.startswith(('0', '3')):
        return f"SZ{code_str}"
    else:
        return code_str

df['code'] = df['code'].apply(add_market_prefix)

df.to_csv(output_file, index=False)
print(f"股票编码与名称映射已生成，保存至: {output_file}")

# 演示如何读取和使用映射
mapping = pd.read_csv(output_file).set_index("code")["name"].to_dict()

# 使用示例
if "SH600519" in mapping:
    print(f"示例：mapping['SH600519'] = {mapping['SH600519']}")
else:
    print("示例股票代码SH600519未找到，请检查数据")
    # 打印前10条数据查看格式
    print("\n前10条数据示例：")
    for i, (code, name) in enumerate(list(mapping.items())[:10]):
        print(f"{i+1}. {code}: {name}")
