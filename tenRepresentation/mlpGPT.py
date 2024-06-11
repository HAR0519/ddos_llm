import numpy as np  
import pandas as pd  
import tensorflow as tf  
from tensorflow.keras.models import Model  
from tensorflow.keras.layers import Input, Dense  
from sklearn.model_selection import train_test_split  
from sklearn.preprocessing import StandardScaler  
  
# 1. 读取数据  
df = pd.read_csv('your_file.csv')  
  
# 2. 划分特征和标签  
X = df.drop('target_column', axis=1).values  
y = df['target_column'].values  
  
# 3. 数据预处理（例如，标准化）  
scaler = StandardScaler()  
X_scaled = scaler.fit_transform(X)  
  
# 4. 划分训练集和测试集  
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)  
  
# 5. 定义MLP模型  
input_dim = X_train.shape[1]  
num_classes = len(np.unique(y_train))  # 假设是分类任务  
  
# 输入层  
inputs = Input(shape=(input_dim,))  
  
# 隐藏层（你可以添加更多层）  
hidden = Dense(100, activation='relu')(inputs)  # 假设有一个隐藏层，100个神经元  
  
# 输出层（对于分类任务，使用softmax激活函数）  
outputs = Dense(num_classes, activation='softmax')(hidden)  
  
# 创建模型  
model = Model(inputs=inputs, outputs=outputs)  
  
# 编译模型  
model.compile(loss='sparse_categorical_crossentropy',  # 对于整数标签使用sparse_categorical_crossentropy  
              optimizer='adam',  
              metrics=['accuracy'])  
  
# 6. 训练模型  
model.fit(X_train, y_train, epochs=10, batch_size=32)  
  
# 7. 获取隐藏层输出作为高维数据  
# 创建一个新模型，其输出是原始模型的隐藏层  
hidden_model = Model(inputs=model.input, outputs=hidden)  
  
# 使用测试集获取隐藏层输出  
high_dim_data = hidden_model.predict(X_test)  
  
# 8. 保存或使用高维数据  
np.save('high_dimensional_data.npy', high_dim_data)