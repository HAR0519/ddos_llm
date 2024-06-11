import pandas as pd  
  
# 读取CSV文件  
df = pd.read_csv('ApplicationDDoS/app10.csv')  # 替换'your_file.csv'为你的CSV文件名  
  
# 确保CSV文件中的列名与你要排序的列名相匹配  
# 如果列名不匹配，你可能需要手动修改它们  
  
# 按照指定的列进行排序  
df_sorted = df.sort_values(by=['Protocol', 'Src IP', 'Dst IP', 'Src Port', 'Dst Port'])  
  
# 显示排序后的DataFrame  
#print(df_sorted)  
  
# 如果需要将排序后的DataFrame保存到一个新的CSV文件中  
df_sorted.to_csv('app_orderly.csv', index=False)  # 'sorted_file.csv'是新文件的名称