#Bài tập 3: Phân tích dữ liệu dạng bảng
import pandas as pd
import numpy as np
df = pd.read_csv('advertising.csv')
data = df.to_numpy()
#Câu hỏi 15: Lấy giá trị lớn nhất và chỉ mục tương ứng của nó trên cột Sales:
print(f"Max:{np.max(data[:,3])} - Index:{np.argmax(data[:,3])}")

#Câu hỏi 16: Giá trị trung bình của cột TV là:
print(f"{np.mean(data[:,0])}")

#Câu hỏi 17: Số lượng bản ghi có giá trị tại cột Sales lớn hơn hoặc bằng 20 là:
print(f"{len(data[np.nonzero(data[:,3]>=20)])}")

#Câu hỏi 18: Tính giá trị trung bình của cột Radio thoả mãn điều kiện giá trị tương ứng trên cột Sales lớn hơn hoặc bằng 15:
print(f"{np.mean(data[np.nonzero(data[:,3]>=15),1])}")

#Câu hỏi 19: Tính tổng các hàng của cột Sales với điều kiện giá trị Newspaper lớn hơn giá trị trung bình của cột Newspaper:
print(f"{np.sum(data[np.nonzero(data[:,2]>np.mean(data[:,2])),3])}")

"""
Câu hỏi 20: Gọi giá trị trung bình của cột Sales là A. Tạo ra mảng mới scores chứa các
giá trị Good, Average và Bad sao cho: nếu giá trị hiện tại > A => giá trị trong mảng mới
là Good, < A thì sẽ là Bad và = A sẽ là Average. Sau đó in ra kết quả scores[7:10]
"""
A = np.mean(data[:,3])
scores = np.where(data[:,3]>A,'Good','Bad')
scores = np.where(data[:,3]==A,'Average',scores)
print(scores[7:10])

"""
Câu hỏi 21: Gọi giá trị trên cột Sales gần nhất với giá trị trung bình cũng chính cột
Sales là A. Tạo ra mảng mới scores chứa các giá trị Good, Average và Bad sao cho: nếu
giá trị hiện tại > A => giá trị trong mảng mới là Good, < A thì sẽ là Bad và = A sẽ là
Average. Sau đó in ra kết quả scores[7:10]
"""
index = np.argmin(np.abs(data[:,3]-np.mean(data[:,3])))
A = data[index,3]
scores = np.where(data[:,3]>A,'Good','Bad')
scores = np.where(data[:,3]==A,'Average',scores)
print(scores[7:10])