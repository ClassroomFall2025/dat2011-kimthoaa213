class SinhVien:
    def __init__(self,ho_va_ten="",nganh="",diem=""):
        self.ho_va_ten = ho_va_ten
        self.nganh = nganh
        self.diem = diem
    
    def nhap_thongtin(self):
        self.ho_va_ten = input("Nhập họ và tên: ")
        self.nganh = input("Nhập ngành đang học: ")
        self.diem = float(input("Nhập điểm trung bình: "))
        return self
         
    def get_diem(self):
        return self.diem
    
    def get_hocluc(self):
        if 0> self.get_diem() <=5:
            self.hoc_luc = "Yếu"
        elif self.get_diem() <=7:
            self.hoc_luc = "Khá"
        elif self.get_diem() <=8:
            self.hoc_luc = "Gioi"
        elif self.get_diem() <=10:
            self.hoc_luc = "Xuất sắc"
        return self.hoc_luc
    
    def xuat_thong_tin(self) -> str:
        print("----------------------")
        print(f"Họ tên: {self.ho_va_ten}\nNgành: {self.nganh}\nĐiểm: {self.diem}\nHọc lực: {self.get_hocluc()}")
        
menu_lab6= {
    1: "Nhập danh sach sinh viên",
    2: "Xuất thông tin danh sách sinh viên",
    3: "Xuất danh sach sinh viên có học lực giỏi",
    4: "Sắp xếp danh sách nhân vien theo điểm",
    5: "Kết thúc"
}
def menu():
    print("=================Menu================")
    for key, value in menu_lab6.items():
        print(f"{key} : {value}")
        
ds_sinhvien = []

def nhapds_sinhvien():
    n = int(input("Nhập số sinh viên muốn nhập vào: "))
    for i in range(n):
        print(f"Nhập sinh viên thứ {i+1}: ")
        ds_sinhvien.append(SinhVien().nhap_thongtin())
            
def xuatds_sinhvien():
    print("======Danh sách sinh viên=======")
    for sinhvien in ds_sinhvien:
        sinhvien.xuat_thong_tin()
        
def ds_svgioi():
    sv_gioi = []
    for sv in ds_sinhvien:
        if sv.get_hocluc() == "Gioi":
            sv_gioi.append(sv)
    print("=====Danh sach sinh vien GIOI=====")
    if len(sv_gioi) == 0:
        print("Không có sinh viên nào loại GIỎI")
    else:
        for sv in sv_gioi:
            sv.xuat_thong_tin()
            
#Sắp xếp giảm dần
def sapxepsv_diem():
    ds_sapxep = []
    for sv in ds_sinhvien:
        ds_sapxep = sorted(ds_sinhvien, key = lambda sv: sv.get_diem(), reverse=True)
    print("==========Danh Sách Đã Sắp Xếp========")
    for sv in ds_sapxep:
        sv.xuat_thong_tin()
    