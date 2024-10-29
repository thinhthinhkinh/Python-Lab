# #Huong dan cach nhap du lieu
# a = input("Nhap vao mot so nguyen a: ")
# print(a)
# print("So a vua nhap la:",a)
# print("So a vua nhap la: "+a) #Noi chuoi
# print(f"So a vua nhap la: {a}")
# print("So a vua nhap la: {}".format(a))

# """
# Day la cach comment thu 2
# Toi ten la Pham vo truong thinh
# """
# #Variable trong Python
# x = 9
# y = 8
# name = "Thinh"
# print(name)
# print(y)
# print(x)
# #Cac kieu du lieu trong python
# songuyen = 5
# sothuc = 8.8
# chuoi = "Thinhhihi"
# sophuc = 8 + 9j
# luanli = True
# print(songuyen, sothuc, chuoi, sophuc, luanli)
# #Cach xem kieu du lieu trong python
# print("\n#Cach xem kieu du lieu trong python")
# print(type(songuyen))
# print(type(sothuc))
# print(type(chuoi))
# print(type(sophuc))
# print(type(luanli))
# print()
# #Ep kieu du lieu trong python
# print("\n#Ep kieu du lieu trong python")

# a = 1256
# b = 4
# print(a%b)
# #
# age =20
# sinhvien= False
# res = age <= 20 and not sinhvien
# print(res)
# x = 5
# y=3
# res1 = x ^ y
# print(res1)
# print()

print("#Câu 1: Nhập vào số nguyên dương a, nếu a là số chẵn thì in ra đây là số chẵn, ngược lại in ra đây là số lẻ")
a = int(input("Nhap mot so nguyen a(a>0): "))
if(a%2==0):
    print(a," la so chan")
else:
    print(a, "la so le")
print("Câu 2: Nhập vào 3 số thực dương a, b, c. Kiểm tra xem a, b, c có cấu thành độ dài của 1 tam giác được không")
b = float(input("Nhap so thuc b: "))
c = float(input("Nhap so thuc c: "))
a1 = float(input("Nhap so thuc a1: "))
if ((a1+b > c) or (b+c>a1) or (a1 +c)):
    print("a1,b,c co the tao thanh do dai cua tam giac")
else:
    print("a1,b,c khong the tao thang do dai cua tam giac")