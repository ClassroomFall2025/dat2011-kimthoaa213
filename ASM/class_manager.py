class Nhan_Vien ():
    def __init__(self,ma_nv="",ten_nv="",luong_thang=0):
        self.ma_nv = ma_nv
        self.ten_nv = ten_nv
        self.luong_thang = luong_thang
    
    def nhap_thong_tin(self):
        print("Nhập thông tin :")
        self.ma_nv = input("Nhập mã nv: ")
        self.ten_nv = input("Nhập tên nhân viên: ")
        self.luong_thang = int(input("Nhâp lương tháng :"))
        return self
    
    def tinh_thu_nhap(self):
        return self.luong_thang
    
    def tinh_thue_thu_nhap(self):
        if self.tinh_thu_nhap() < 9000000 :
            return 0
        elif self.tinh_thu_nhap() < 15000000 :
            return (self.tinh_thu_nhap()-9000000) * 0.1
        else:
            return (self.tinh_thu_nhap()-15000000) * 0.12 + 600000
        
    def xuat_thong_tin(self) -> str:
        return f"Mã nhân viên: {self.ma_nv} \nTên nhân viên: {self.ten_nv} \nLương nhân viên: {self.luong_thang}"
    
    def thu_nhap_sau_thue(self):
        return self.tinh_thu_nhap()-self.tinh_thue_thu_nhap()
    
class Nhan_Vien_Tiep_Thi(Nhan_Vien):
    def __init__(self, ma_nv = "", ten_nv = "", luong_thang = 0,doanh_so = 0,ti_le_hoa_hong = 0):
        super().__init__(ma_nv, ten_nv, luong_thang)
        self.doanh_so = doanh_so
        self.ti_le_hoa_hong=ti_le_hoa_hong
    
    def nhap_thong_tin(self):
        super().nhap_thong_tin()
        self.doanh_so=int(input("Nhập doanh số: "))
        self.ti_le_hoa_hong=float(input("Nhập tỉ lệ hoa hồng (%): "))/100
        return self
    
    def tinh_thu_nhap(self) -> float:
        return self.luong_thang + self.doanh_so*self.ti_le_hoa_hong
    def xuat_thong_tin(self) -> str:
        return f"Mã nhân viên: {self.ma_nv} \nTên nhân viên: {self.ten_nv} \nLương nhân viên: {self.luong_thang} \nDoanh số: {self.doanh_so} \nTỉ lệ hoa hông: {self.ti_le_hoa_hong}"
    
class Truong_Phong(Nhan_Vien):
    def __init__(self, ma_nv = "", ten_nv = "", luong_thang = 0,luong_trach_nhiem = 0):
        super().__init__(ma_nv, ten_nv, luong_thang)
        self.luong_trach_nhiem=luong_trach_nhiem
        
    def nhap_thong_tin(self):
        super().nhap_thong_tin()
        self.luong_trach_nhiem = int(input("Nhập lương trách nhiệm: "))
        return self
        
    def tinh_thu_nhap(self):
        return self.luong_thang+self.luong_trach_nhiem
    
    def xuat_thong_tin(self):
        return f"Mã nhân viên: {self.ma_nv} \nTên nhân viên: {self.ten_nv} \nLương nhân viên: {self.luong_thang} \nLương trách nhiệm: {self.luong_trach_nhiem}"

# Tìm nhân viên trong khoảng lương xác định sau đó trả về một list chứa các nhân viên trong khoảng lương đó 
def Findding_Employee (Employee_list, min_sal, max_sal):
    Findding_Employee = []
    for Employee in Employee_list:
        if min_sal <= Employee.tinh_thu_nhap() <= max_sal:
            Findding_Employee.append(Employee)
    return Findding_Employee