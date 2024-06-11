import pandas as pd  
import numpy as np  
  
# 读取数据  
data_appddos_list = pd.read_csv("app_orderly.csv", low_memory=False)  
  
# 选择感兴趣的列  
representation_app = data_appddos_list[["Bwd Segment Size Avg", "Bwd Bulk Rate Avg", "URG Flag Count", "CWR Flag Count", "Active Max", "Down/Up Ratio", "Active Min", "Bwd Packet Length Std", "Total Length of Bwd Packet"]]  
  
# 检查列中是否所有值都可以转换为数字  
for column in representation_app.columns:  
    try:  
        # 尝试将列转换为浮点数，不能转换的设置为NaN  
        representation_app[column] = pd.to_numeric(representation_app[column], errors='coerce')  
    except ValueError:  
        print(f"Column '{column}' contains non-numeric values and will be dropped.")  
        # 如果某列包含非数字值，你可以选择删除整列或进行其他处理  
        representation_app.drop(columns=[column], inplace=True)  # 如果要删除整列，取消注释这行代码  
  
# 删除所有包含NaN值的行（确保只包含可以转换为数字的值）  
representation_app.dropna(inplace=True)  
  
# 转换为NumPy数组（如果需要，但通常保留DataFrame更灵活）  
representation_array_app = representation_app.values  
  
# 计算剩余的行数  
hang = representation_app.shape[0]  
print(f"Number of rows after cleaning: {hang}")  
  
# 如果需要将排序后的DataFrame保存到一个新的CSV文件中  
# 注意：这里我们使用原始的DataFrame，而不是NumPy数组  
representation_app.to_csv('app_init.csv', index=False)  # 'app_init.csv'是新文件的名称