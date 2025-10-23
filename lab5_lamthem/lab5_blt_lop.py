import math as m
import datetime as dt


ten_phep_tinh = {
    1: "Phép tính cơ bản",
    2: "Lũy thừa",
    3: "Căn bậc hai",
    4: "Hàm lượng giác",
    5: "Logarit",
    6: "Giải phương trình bậc nhất",
    7: "Giải phương trình bậc hai",
    8: "Lịch sử",
    9: "Thời gian hiện tại",
    10:"Thoát chương trình"
}

def menu():
    print("===============MENU=================")
    for key, value in ten_phep_tinh.items():
        print(f"{key}: {value}")
        
        
class MayTinh:
    
    def __init__(self):
        pass
        
    def phep_tinh_co_ban(self):
        while True:
            try:
                so1 = float(input("Nhập số thứ nhất: "))
                so2 = float(input("Nhập số thứ hai: "))
                toan_tu = input("Nhập phép toán (+, -, *, /): ")
                break
            except:
                print("Lỗi: Vui lòng nhập phép toán (+, -, *, /)")
        
        if toan_tu == "+":
            self.ket_qua = so1 + so2
            print(f"Tổng = {self.ket_qua}")
        elif toan_tu == "-":
            self.ket_qua = so1 - so2
            print(f"Hiệu = {self.ket_qua}")
        elif toan_tu == "*":
            self.ket_qua = so1 * so2
            print(f"Tích = {self.ket_qua}")
        elif toan_tu == "/":
            if so2 != 0:
                self.ket_qua = so1 / so2
                print(f"Thương = {self.ket_qua}")
            else:
                print("Lỗi: không chia được cho 0")
        else:
            print("Phép toán không hợp lệ") 
        return self.ket_qua
    
    def luy_thua(self):
        x = float(input("Nhập cơ số: "))
        y = float(input("Nhập số mũ: "))
        self.ket_qua = m.pow(x, y)
        print(f"{x}^{y} = {self.ket_qua}")
        return self.ket_qua
    
    def can_bac_hai(self):
        x = float(input("Nhập số: "))
        if x >= 0:
            self.ket_qua = m.sqrt(x)
            print(f"√{x} = {self.ket_qua}")
        else:
            print("Lỗi: không căn bậc 2 số âm")
        return self.ket_qua  
    
    def luong_giac(self):
        so_1 = float(input("Nhập số: "))
        toan_tu = input("Nhập phép toán (sin, cos, tan): ").lower().strip()
        
            #Hàm lượng giác
        if toan_tu == "sin":
            self.ket_qua = m.sin(m.radians(so_1))
            print(f"Sin {so_1} = {self.ket_qua:.3f}")
            
        elif toan_tu == "cos":
            self.ket_qua = m.cos(m.radians(so_1))
            print(f"Cos {so_1} = {self.ket_qua:.3f}")
            
        elif toan_tu == "tan": 
            self.ket_qua = m.tan(m.radians(so_1))
            print(f"Tan {so_1} = {self.ket_qua:.3f}")
    #Phép toán không hợp lệ
        else:
            print("Lỗi: Phép toán không hợp lệ")
        return round(self.ket_qua,3)
    
    def logarit(self):
        so_1 = float(input("Nhập số thứ nhất: "))
        so_2 = float(input("Nhập số thứ hai: "))
        if so_1!=0 and so_2>0 and so_2!=1:
            self.ket_qua = m.log(so_1, so_2)
            print(f"Logarit {so_1} cơ số {so_2} = {self.ket_qua:.3f}")
            
        else:
            print("Lỗi: Điều kiện logarit không thỏa")
        return self.ket_qua
    
    def phuong_trinh_bac_nhat(self):
        a = int(input("Nhập a: "))
        b = int(input("Nhập b: "))
        
        if a == 0:
            if b== 0 :
                print("Vô số nghiệm")
                self.ket_qua = "Vô số nghiệm"
            else:
                print("Vô nghiệm") 
                self.ket_qua = "Vô nghiệm"
        else:
            x =-b/a
            print(f"Phương trình {a}x + {b} = 0 có nghiệm là: {x}")
            self.ket_qua = x
        return self.ket_qua
    
    def phuong_trinh_bac_hai(self):
        a = int(input("Nhập a: "))
        b = int(input("Nhập b: "))
        c = int(input("Nhập c: "))
        #xét a
        if a == 0 : #bx+c = 0
            if b == 0:
                if c == 0 :
                    print("Vô số nghiệm")
                    self.ket_qua = "Vô số nghiệm"
                    return print("Vô số nghiệm")
                else:
                    print("Vô nghiệm")
                    self.ket_qua = "Vô nghiệm"
                    return print("Vô nghiệm")
            else:
                x =-c/b
                print(f"Phương trình {b}x + {c} = 0 có nghiệm là: {x}")
                self.ket_qua = x
        else:
            delta = b * b - 4 * a * c
            if delta < 0:
                self.ket_qua = "Vô nghiệm"
                return print("Phương trình vô nghiệm")
            elif delta == 0:
                x = -b/(2*a)
                print(f"Phương trình có nghiệm kép: {x}")
                self.ket_qua = x
                return print(f"Phương trình có nghiệm kép: {x}")
            else:
                x1 = (-b+m.sqrt(delta))/(2*a)
                x2 = (-b-m.sqrt(delta))/(2*a)
                print(f"Phương trình có 2 nghiệm phân biệt:\n x1:{x1:.3f}\n x2:{x2:.3f}")
                self.ket_qua = (x1, x2)
                return print(f"Phương trình có 2 nghiệm phân biệt:\n x1:{x1:.3f}\n x2:{x2:.3f}")
        return self.ket_qua
    
    def hien_thi_thoi_gian(self):
        now = dt.datetime.now()
        return print(now.strftime("Bây giờ là %H giờ %M phút %S giây, ngày %d tháng %m năm %Y"))

    def in_lich_su(self,lich_su):
        if not lich_su:
            print("Chưa có phép tính nào được thực hiện.")
            return
        else:
            print("============================================")
            print("Lịch sử các phép tính đã thực hiện:")
            for item in lich_su:
                print("----------------------------")
                for key, value in item.items():
                    print(f"{key}: {value}")
                    
