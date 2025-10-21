#Đề Bài: Hệ Thống Quản Lý Ngân Hàng Toàn Diện (Python & CSV) 
from quanli_ham import ghiTaiKhoanVaoCSV, nhap_so_tai_khoan
import datetime as dt
import os.path

class TaiKhoan:
    def __init__(self, soTaiKhoan="", ten="", loai="", soDu=0):
        self.soTaiKhoan = soTaiKhoan
        self.ten = ten
        self.loai = loai
        self.soDu = soDu
    
    def taoTaiKhoan(self,danhsachtk:list):
        while True:
            self.soTaiKhoan = nhap_so_tai_khoan()
            if any(tk.soTaiKhoan == self.soTaiKhoan for tk in danhsachtk):
                print("Tài khoản đã tồn tại.")
            else:
                break
        self.ten = input("Nhập tên: ")
        while True: 
            loai = input("Nhập loại tài khoản T/C: ").upper()
            if loai not in ("T", "C"):
                print("Nhập loại tài khoản của bạn (T/C): ")
            else : 
                match loai:
                    case "T":
                        self.loai = "Tiết kiệm"
                    case "C":
                        self.loai = "Cá nhân"
                break
        while True:
            try:
                self.soDu = int(input("Nhập số dư: "))
                if self.get_loai() == "Tiết kiệm":
                    if self.get_soDu2() < 500000:
                        print("Vui lòng nhập tối thiểu 500,000 VNĐ")
                    else:
                        break
                else:
                    if self.get_soDu2() <1000000:
                        print("Vui lòng nhập số dư tối thiểu 1,000,000 VNĐ")
                    else:
                        break
            except ValueError:
                print("Lỗi: vui lòng nhập số Dư = số")
        return self
        
    def hienThiTaiKhoan(self):
        print(f"|{self.soTaiKhoan:^15} | {self.ten:^15} | {self.loai:^10} | {self.soDu:^17,} VNĐ|")
        
    def __str__(self):
        return f"|{self.soTaiKhoan:^15} | {self.ten:^15} | {self.loai:^10} | {self.soDu:^17,} VNĐ|"
    
    def get_SoTaiKhoan(self):
        return self.soTaiKhoan
            
    def get_soDu(self,stk):
        if stk == self.get_SoTaiKhoan():
            return print(f"Số dư hiện tại: {self.get_soDu2():,} VNĐ")
        
        print("Số tài khoản không tồn tại.")
            
            
    def get_soDu2(self):
        return self.soDu
    
    def get_loai(self):
        return self.loai
            
    def get_ten(self):
        return self.ten
    
    def gui_tien(self,stk):
        if stk == self.get_SoTaiKhoan() :
            so_tien = int(input("Nhập số tiền: "))
            self.soDu += so_tien
            print("Gửi tiên thành công")
            return self.soDu
        else: 
            print("Số tài khoản không tồn tại.")
    
    def rut_tien(self,stk):
        if stk == self.get_SoTaiKhoan() :
            print(f"Số dư hiện tại: {self.soDu:,}VNĐ")
            so_tien = int(input("Nhập số tiền muốn rút: "))
            if self.loai == "Tiết kiệm":
                if self.soDu -500000>= so_tien:
                    self.soDu -= so_tien
                    print("Rút tiền thành công")
                    return self.soDu
                else:
                    print("Số dư không đủ")
            else:
                if self.soDu -1000000>= so_tien:
                    self.soDu -= so_tien
                    print("Rút tiền thành công")
                    return self.soDu
                else:
                    print("Số dư không đủ")
        else:
            print("Số tài khoản không tồn tại.")
            
    def chinhSuaTaiKhoan(self):
        print("Nhập thông tin chỉnh sửa: ")
        try:
            lua_chon = int(input("Nhấn 1 để tiếp tục chỉnh sửa: "))
        except ValueError:
            print("Vui lòng nhập 1 để tiếp tục hoặc các số khác để dừng")
        if lua_chon == 1:
            ten_dasua = input("Nhập lại tên( hoặc nhấn q để bỏ qua): ").lower()
            if ten_dasua != "q":
                self.ten = ten_dasua
            while True:
                loai_dasua = input("Nhập lại loại T/C( hoặc nhấn q để bỏ qua): ")
                if loai_dasua.lower() != "q":
                    if loai_dasua.upper() not in ("T", "C"):
                        print("Nhập loại tài khoản của bạn (T/C): ")
                    else:     
                        self.loai = loai_dasua
                        break
                else:
                    break
            while True:
                try: 
                    soDu_dasua = input("Nhập lại số dư( hoặc nhấn q để bỏ qua): ")
                    if soDu_dasua.lower() != "q":
                        self.soDu = int(soDu_dasua)
                        break
                    else:
                        break
                except ValueError:
                    print("Lỗi: nhập không hợp lệ")
        return self
                    
    def to_Dict(self):
        return {
            "soTaiKhoan": self.soTaiKhoan,
            "ten": self.ten,
            "loai": self.loai,
            "soDu": self.soDu,
        }

class danhSachTaiKhoan():
    def __init__(self):
        self.danhsachtk = []
        
    def nhapDanhSachTaiKhoan(self):
        while True: 
            print("Nhập thông tin tài khoản")
            print("1. Nhập thông tin\n2.Thoát ")
            try:
                luachon = int(input("Nhập lựa chọn: "))
                if luachon ==1:
                    taikhoan =TaiKhoan().taoTaiKhoan(self.danhsachtk)
                    self.danhsachtk.append(taikhoan) 
                    ghiTaiKhoanVaoCSV(self.danhsachtk)
                    return self.danhsachtk
                elif luachon == 2:
                    print("Đã thoát trình nhập")
                    break
                else: print("Vui lòng nhập 1 hoặc 2")
            except ValueError:
                print("Lỗi: vui lòng nhập 1 hoặc 2")
                
    def checkTrungStk(self,stk):
        return any(tk.get_SoTaiKhoan() == stk for tk in self.danhsachtk)
                
    def get_Danhsachtaikhoan(self):
        return self.danhsachtk
    
    def xuatDanhSachTaiKhoan(self):
        print("="*10 + "DANH SACH TÀI KHOẢN" + "="*10)
        print("="*72)
        print(f"|{'Số Tài Khoản':^15} | {'Tên':^15} | {'Loại':^10} | {'Số Dư':^21}|")
        print("-"*72)
        if not self.danhsachtk:
            print("(Danh sách rỗng)")
        else:
            for tk in self.danhsachtk:
                tk.hienThiTaiKhoan()
        print("="*72)
                
    def guiTien(self):
        stk = input("Nhập số tài khoản muốn gửi tiền: ")
        for tk in self.get_Danhsachtaikhoan():
            tk.gui_tien(stk)
    
    def rut_tien(self):
        stk = input("Nhập số tài khoản muốn rút tiền: ")
        for tk in self.danhsachtk:
            tk.rut_tien(stk)
        
        
    def xoaTaiKhoan(self):
        stk = input("Nhập số tài khoản muốn Xóa: ")
        for tk in self.get_Danhsachtaikhoan():
            if stk == tk.get_SoTaiKhoan():
                self.danhsachtk.remove(tk)
                print(f"Đã xóa số tài khoản : {stk}")
                return self.danhsachtk
            else:
                print("Số tài khoản không tồn tại.")
                
    def chinhSua_TaiKhoan(self):
        stk = input("Nhập số tài khoản muốn chỉnh sửa: ")
        for tk in self.get_Danhsachtaikhoan():
            if stk == tk.get_SoTaiKhoan():
                return tk.chinhSuaTaiKhoan()
            else: 
                print("Số tài khoản không tồn tại.")
                
    def kiemTraSoDu(self):
        stk = input("Nhập số tài khoản : ")
        for tk in self.get_Danhsachtaikhoan():
            tk.get_soDu(stk) 
                
                
    def timKiemTheoTen(self):
  
        ten_timkiem = input("Nhập tên STK muốn tìm: ").lower()
        
        print("Danh sách tài khoản tìm kiếm:")
        print("="*72)
        print(f"|{'Số Tài Khoản':^15} | {'Tên':^15} | {'Loại':^10} | {'Số Dư':^21}|")
        print("-"*72)
        if self.danhsachtk != []:
            for tk in self.get_Danhsachtaikhoan():
                if ten_timkiem in tk.get_ten().lower():
                    tk.hienThiTaiKhoan()
            print("="*72)
        else:
            print("Danh sách trống")
     
        
    def xuatBaoCao(self):
        count_tk = len(self.danhsachtk)
        sum_soDu = 0
        for tk in self.danhsachtk:
            tien = tk.get_soDu2()        
            sum_soDu += tien
        sl_chiphi = 0
        sl_tietkiem = 0  
        for tk in self.danhsachtk:
            if tk.get_loai() == "Cá nhân":
                sl_chiphi +=1
            else:
                sl_tietkiem +=1
        tg_capnhat = dt.datetime.now()
        with open("baocao.txt", "a", encoding= "utf-8") as f:
            if os.path.exists("baocao.txt"):
                f.write(f"\n|{count_tk:^15} | {sum_soDu:^12} | {sl_chiphi:^20} | {sl_tietkiem:^22} | {tg_capnhat.strftime("%H:%M:%S, %d/%m/%Y"):^17}|\n")
                f.write("-"*103)
            else :   
                f.write("="*103)
                f.write(f"\n|{"Tổng tài khoản":^15} | {"Tổng số dư:":^12} | {"Số lượng TK Chi phí":^20} | {"Số lượng TK Tiết kiệm":^22} | {"Thời gian cập nhật":^20}|\n")
                f.write("-"*103)
                f.write(f"\n|{count_tk:^15} | {sum_soDu:^12} | {sl_chiphi:^20} | {sl_tietkiem:^22} | {tg_capnhat.strftime("%H:%M:%S, %d/%m/%Y"):^17}|\n")
                f.write("-"*103)
                    
    def docTaiKhoanTuCSV(file,danhsachtk_moi):
        import csv
        with open(file, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                tk = TaiKhoan(
                    soTaiKhoan=row["soTaiKhoan"],
                    ten=row["ten"],
                    loai=row["loai"],
                    soDu=int(row["soDu"])
                )
                danhsachtk_moi.append(tk)
                return danhsachtk_moi
