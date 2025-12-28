import sys
import os

# lấy đường dẫn tới thư mục cha
thu_muc_goc = os.path.dirname(os.path.dirname(__file__))

# thêm thu_vien_chung vào sys.path
sys.path.append(os.path.join(thu_muc_goc, "thu_vien_chung"))

import xu_ly_so

so = 17

if xu_ly_so.kiem_tra_so_nguyen_to(so):
    print(so, "là số nguyên tố")
else:
    print(so, "không phải là số nguyên tố")
 