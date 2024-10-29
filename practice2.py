import numpy as np 
import matplotlib.pyplot as plt
a = np.random.randint(0, 1000, size =100)
#hine thi 10 phan tu dau tien
print(a[:10])
#hien thi 5 phan tu cuoi cung
print(a[-5:])
#kiem tra co bao nhieu phan tu < 100
print(a[a<100])
#tinh tong mang
tong = np.sum(a)
print(tong)
#tinh trung binh
tb = np.mean(a)
print(tb)
#tinh trung vi
tv = np.median(a)
print(tv)
#tim q1, q2, q3
q1 = np.percentile(a, 25)
q2 = np.percentile(a, 50)
q3 = np.percentile(a, 75)
print(q1, q2, q3)
#tinh phan vi
phanvi = np.percentile(a, 20)
print(f"Phan vi: {phanvi}")

#chon ngau nhien 10 phan tu trong mang 5 lan
for i in range(5):
    print(np.random.choice(a,10))

#phan tu xuat hien nhieu nhat trong mang
print(np.bincount(a).argmax())

# ve do thi
x = [1,2,3]
y= [2,4,1]
plt.plot(x,y)
plt.title("Do thi don gian")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
#ve 2 duong thang
x1 = [10, 20, 30]
y1 = [40, 10, 30]

x2 = [10, 20, 30]
y2 = [20, 40, 10]

plt.plot(x1, y1, color='blue', label='line 1')
plt.plot(x2, y2, color='red', label='line 2')

plt.title('Đồ thị hai đường thẳng')
plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.legend()
plt.show()
#su dung marker

x = [1, 4, 5, 6, 7]
y = [2, 6, 3, 6, 3]
plt.plot(x, y, marker='o', color='blue', markerfacecolor='orange', linewidth=1)

plt.title('Sử dụng marker')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
#do thi sin cos
x = np.linspace(0, 2 * np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure(figsize=(10, 5))
plt.plot(x, y_sin, label='sin(x)', color='blue')
plt.plot(x, y_cos, label='cos(x)', color='orange', linestyle='--')

plt.title('Đồ thị hàm sin(x) và cos(x)')


plt.grid(True)
plt.legend()

plt.show()
