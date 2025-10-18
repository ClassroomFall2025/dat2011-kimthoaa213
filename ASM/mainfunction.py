from class_manager import * 

ds_nhanvien ={
        "Hành chính" :[],
        "Tiếp thị" :[],
        "Trưởng phòng": [] 
    }

def kiem_tra_trung_ma(ma_nv, ds_nhanvien):
    #for list in dict (loai_nhan_vien là 1 list trong dict ds_nhanvien)
    for loai_nhan_vien in ds_nhanvien.values():
        #for item in list -> mỗi phần tử trong list (nhan_vien_trong_loai )là 1 object được nhập từ class 
        for nhan_vien_trong_loai in loai_nhan_vien:
            #kiểm tra trùng lặp mã nhân viên
            if nhan_vien_trong_loai.ma_nv == ma_nv:
                return True
    return False

def nhap_ds_nv():
    print("Chọn Loại Nhân Viên Muốn Nhập")

    while True:
        print("\nChọn loại nhân viên:")
        print("1. Hành chính")
        print("2. Tiếp thị") 
        print("3. Trưởng phòng")
        print("0. Thoát")
        
        try:
            the_loai= int(input("Nhập Thể Loại Nhân Viên:"))
        except ValueError:
            print("Vui lòng nhập lại lựa chọn 1, 2, 3 để nhập danh sách nhân viên hoặc 0 để thoát")
            continue
        if the_loai == 1:
            nhap_nhan_vien = NhanVien().nhap_thong_tin()
            if kiem_tra_trung_ma(nhap_nhan_vien.ma_nv, ds_nhanvien):
                print("Mã nhân viên đã tồn tại")
            else:
                ds_nhanvien["Hành chính"].append(nhap_nhan_vien)
        elif the_loai == 2:
            nhap_nhan_vien_tiep_thi = NhanVienTiepThi().nhap_thong_tin()
            if kiem_tra_trung_ma(nhap_nhan_vien_tiep_thi.ma_nv, ds_nhanvien):
                print("Mã nhân viên đã tồn tại")
            else:
                ds_nhanvien["Tiếp thị"].append(nhap_nhan_vien_tiep_thi)
        elif the_loai == 3:
            nhap_truong_phong = TruongPhong().nhap_thong_tin()
            if kiem_tra_trung_ma(nhap_truong_phong.ma_nv, ds_nhanvien):
                print("Mã nhân viên đã tồn tại")
            else:
                ds_nhanvien["Trưởng Phòng"].append(nhap_truong_phong)
        elif the_loai ==0 :
            break
        else:
            print("vui lòng nhập lại lựa chọn 1, 2, 3 để nhập danh sách nhân viên hoặc 0 để thoát")
    return ds_nhanvien
    
# nhap_ds_nv()




def luu_file():
    pass


def doc_tu_file():
    pass

def xuat_ds():
    pass


def tim_nv_theo_luong (ds_nhanvien:list, min_sal, max_sal):
    pass

def tim_nv_theo_ma():
    pass

def tim_kiem_nhan_vien():
    list_tim_kiem = []
    print("*"*15+" TÌM KIẾM NHÂN VIÊN "+"*"*15)
    print("|    1. Tìm kiếm nhân viên theo mã               |")
    print("|    2. Tìm kiếm nhân viên theo khoảng lương     |")
    print("*"*50)
    print("Chọn phương thức tìm kiếm")
    while True:
        try:
            tim_kiem = int(input("Bạn hãy chon 1 hoặc 2: "))
            if tim_kiem in [1,2]:
                break
        except ValueError:
            print("Lựa chọn không hợp lệ ! Vui lòng nhập lại lựa chọn.")
    if tim_kiem == 1:
        list_tim_kiem #=tim_nv_theo_ma()
    else :
        list_tim_kiem #=tim_nv_theo_luong()
    return list_tim_kiem
    
                    


def xoa_nv_theo_ma():
    pass

def sap_xep_nv_theo_thu_nhap():
    pass

def sap_xep_nv_theo_ho_ten():
    pass

def sap_xep_nv_():
    print("*"*15+" SẮP XẾP NHÂN VIÊN "+"*"*16)
    print("|    1. Sắp xếp nhân viên theo tên               |")
    print("|    2. Sắp xếp nhân viên theo thu nhập          |")
    print("*"*50)
    print("Chọn phương thức tìm kiếm")
    while True:
        try:
            sap_xep = int(input("Bạn hãy chon 1 hoặc 2: "))
            if sap_xep in [1,2]:
                break
        except ValueError:
            print("Lựa chọn không hợp lệ ! Vui lòng nhập lại lựa chọn.")
    if sap_xep == 1:
        list_tim_kiem=sap_xep_nv_theo_ho_ten()
    elif sap_xep == 2:
        list_tim_kiem=sap_xep_nv_theo_thu_nhap()
    else:
        print("Thoát sắp xếp")
    return 

def cap_nhat_tt_theo_ma():
    pass

def xuat_5_nv_thu_nhap_cao_nhat():
    pass
