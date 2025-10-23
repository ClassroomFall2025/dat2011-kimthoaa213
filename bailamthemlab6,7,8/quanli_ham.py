import csv

menu = {
    1 : "Tạo tài khoản mới",
    2 : "Giao dịch (Rút / Gửi tiền)",
    3 : "Kiểm tra số dư",
    4 : "Danh sách tài khoản",# chọn xem danh sach hoặc tìm kiếm tk "Tìm kiếm theo tên"
    5 : "Quản lí tài khoản (Đóng / Chỉnh sửa)", # đóng và chỉnh sửa
    6 : "Xuất báo cáo",
    7 : "Quản lí dữ liệu (Sao lưu / Khôi phục)",
    8 : "Thoát"
   
}

def hien_menu():
    print("..................MENU..................\n")
    for key,value in menu.items():
        print(f"{key} : {value}")
        
def ghiTaiKhoanVaoCSV(file:list):
    with open("taikhoan.csv","a",newline="",encoding="utf-8") as f:
        field_names = ["soTaiKhoan", "ten", "loai", "soDu"]
        ghidulieu_dict = csv.DictWriter(f,fieldnames=field_names)
        ghidulieu_dict.writeheader()
        for tk in file:
            ghidulieu_dict.writerow(tk.to_Dict())
        print("Ghi dữ liệu thành công")    
        
        

import shutil
import datetime
import os

def nhap_so_tai_khoan():
    while True:
        stk = input("Nhập số tài khoản (5 chữ số): ").strip()
        if stk.isdigit() and len(stk) == 5:
            return stk
        print("Lỗi: số tài khoản phải gồm đúng 5 chữ số (0-9).")

def saoLuuDuLieu():
    if not os.path.exists("backup"):
        os.makedirs("backup")

    timestamp = datetime.datetime.now().strftime("%H%M_%d%m%Y")
    ten_file_backup = f"backup/taikhoan_{timestamp}.csv"

    try:
        shutil.copy("taikhoan.csv", ten_file_backup)
        print(f"Sao lưu thành công: {ten_file_backup}")
    except FileNotFoundError:
        print("Không tìm thấy file taikhoan.csv để sao lưu.")
        
def khoiPhucDuLieu():
    backup_folder = "backup"
    if not os.path.exists(backup_folder):
        print("Thư mục backup chưa tồn tại.")
        return
    # listdir là lấy các file trong folder đó và lấy các file csv
    backups = [f for f in os.listdir(backup_folder) if f.endswith(".csv")]
    if not backups:
        print("Không có file sao lưu nào.")
        return

    print("Danh sách các file backup:")
    for i, file in enumerate(backups, start=1):
        print(f"{i}. {file}")

    try:
        chon = int(input("Nhập số thứ tự file muốn khôi phục: "))
        if 1 <= chon <= len(backups):
            file_duoc_chon = backups[chon - 1] # index từ 0 nên phải -1
            shutil.copy(os.path.join(backup_folder, file_duoc_chon), "taikhoan.csv") 
            #join dùng để nổi các đường dẫn lại với nhau, copy file đó và đè vào file taikhoan
            print(f"Đã khôi phục thành công từ file {file_duoc_chon}")
        else:
            print("Lựa chọn không hợp lệ.")
    except ValueError:
        print("Vui lòng nhập số hợp lệ.")

def giaoDich(ql_taikhoan):
    print("\n--- CHỌN LOẠI GIAO DỊCH ---")
    print("1. Gửi tiền")
    print("2. Rút tiền")
    print("3. Thoát")

    while True:
        try:
            chon_gd = int(input("Chọn loại giao dịch (1-3): "))
            if chon_gd == 1:
                ql_taikhoan.guiTien()
                break
            elif chon_gd == 2:
                ql_taikhoan.rut_tien()
                break
            elif chon_gd == 3:
                print("Quay lại menu chính.")
                break
            else:
                print("Vui lòng chọn 1, 2 hoặc 3.")
        except ValueError:
            print("Lỗi: vui lòng nhập số hợp lệ (1-3).")

def hienThiThongTin(ql_taikhoan):
    print("\n--- LỰA CHỌN HIỂN THỊ ---")
    print("1. Danh sách tất cả tài khoản")
    print("2. Tìm kiếm theo tên")
    print("3. Thoát")

    while True:
        try:
            chon = int(input("Chọn (1-3): "))
            if chon == 1:
                ql_taikhoan.xuatDanhSachTaiKhoan()
                break
            elif chon == 2:
                ql_taikhoan.timKiemTheoTen()
                break
            elif chon == 3:
                print("Quay lại menu chính.")
                break
            else:
                print("Vui lòng chọn 1, 2 hoặc 3.")
        except ValueError:
            print("Lỗi: vui lòng nhập số hợp lệ.")


def quanLyTaiKhoan(ql_taikhoan):
    print("\n--- QUẢN LÝ TÀI KHOẢN ---")
    print("1. Xóa tài khoản")
    print("2. Chỉnh sửa tài khoản")
    print("3. Thoát")

    while True:
        try:
            chon = int(input("Chọn (1-3): "))
            if chon == 1:
                ql_taikhoan.xoaTaiKhoan()
                break
            elif chon == 2:
                ql_taikhoan.chinhSua_TaiKhoan()
                break
            elif chon == 3:
                print("Quay lại menu chính.")
                break
            else:
                print("Vui lòng chọn 1, 2 hoặc 3.")
        except ValueError:
            print("Lỗi: vui lòng nhập số hợp lệ.")


def quanLyDuLieu():
    print("\n--- QUẢN LÝ DỮ LIỆU ---")
    print("1. Sao lưu dữ liệu")
    print("2. Khôi phục dữ liệu")
    print("3. Quay lại menu chính")

    while True:
        try:
            chon = int(input("Chọn (1-3): "))
            if chon == 1:
                saoLuuDuLieu()
                break
            elif chon == 2:
                khoiPhucDuLieu()
                break
            elif chon == 3:
                print("Quay lại menu chính.")
                break
            else:
                print("Vui lòng chọn 1, 2 hoặc 3.")
        except ValueError:
            print("Lỗi: vui lòng nhập số hợp lệ.")
