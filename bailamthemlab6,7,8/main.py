from quanli_class import danhSachTaiKhoan
from quanli_ham import *

ql_taikhoan = danhSachTaiKhoan()
hien_menu()
while True:
    while True:
        try:
            lua_chon = int(input("Nhập lựa chọn(1 - 8): "))
            break
        except ValueError:
            print("Lỗi: nhập lựa chọn từ 1 - 8")
    match lua_chon:

        case 1:
            print(menu[lua_chon])
            ql_taikhoan.nhapDanhSachTaiKhoan()
            # ql_taikhoan.xuatDanhSachTaiKhoan()
        case 2:
            giaoDich(ql_taikhoan)

        case 3:
            print(menu[lua_chon])
            ql_taikhoan.kiemTraSoDu()
        case 4:
            print(menu[lua_chon])
            hienThiThongTin(ql_taikhoan)

        case 5:
            print(menu[lua_chon])
            quanLyTaiKhoan(ql_taikhoan)

        case 6:
            print(menu[lua_chon])
            ql_taikhoan.xuatBaoCao()
        case 7:
            quanLyDuLieu()

        case 8:
            print(menu[lua_chon])
            break

        case _:  
            print("Chọn từ 1 - 12")
            
    hien_menu()