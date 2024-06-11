import pandas as pd  
import numpy as np  
  
# 读取数据  
data_appddos_list = pd.read_csv("ApplicationDDoS/app10.csv", low_memory=False)  
  
# 选择感兴趣的列  
representation_app = data_appddos_list[["Bwd Segment Size Avg", "Bwd Bulk Rate Avg", "URG Flag Count", "CWR Flag Count", "Active Max", "Down/Up Ratio", "Active Min", "Bwd Packet Length Std", "Total Length of Bwd Packet"]]  
  
# 检查列中是否所有值都可以转换为数字  
for column in representation_app.columns:  
    try:  
        # 尝试将列转换为浮点数，不能转换的设置为NaN  
        representation_app[column] = pd.to_numeric(representation_app[column], errors='coerce')  
    except ValueError:  
        print(f"Column '{column}' contains non-numeric values and will be dropped.")  
        # 如果某列包含非数字值，您可以选择删除整列或进行其他处理  
        # representation_app.drop(columns=[column], inplace=True)  # 如果要删除整列，取消注释这行代码  
  
# 删除所有包含NaN值的行（确保只包含可以转换为数字的值）  
representation_app.dropna(inplace=True)  
  
# 转换为NumPy数组  
representation_array_app = representation_app.values  
  
# 计算剩余的行数  
hang = representation_array_app.shape[0]  
print(f"Number of rows after cleaning: {hang}")  
  
# 初始化计数器  
count = 0  
  
# 计算连续行之间的余弦相似度  
for i in range(hang - 1):  
    a = representation_array_app[i]  
    b = representation_array_app[i + 1]  
      
    # 计算点积  
    dot_product = np.dot(a, b)  
      
    # 计算模长  
    a_mod = np.linalg.norm(a)  
    b_mod = np.linalg.norm(b)  
      
    # 计算余弦相似度  
    if b_mod == 0 or a_mod == 0:  
        y = 0  
    else:  
        y = dot_product / (a_mod * b_mod)  
      
    # 检查余弦相似度是否大于或等于阈值  
    if y >= 0.8 or y == 0:  
        count += 1  
  
# 输出结果  
print(f"Number of pairs with cosine similarity >= 0.8: {count}")  
print(f"Proportion of pairs with cosine similarity >= 0.8: {count / (hang - 1)}")