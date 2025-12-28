from du_lieu.danh_sach import sap_xep_tang_dan
from du_lieu.tu_dien import lay_gia_tri

ds = [5, 2, 9, 1, 7]
tu_dien = {"a": 10, "b": 20, "c": 30}

print("Danh sách sau khi sắp xếp:", sap_xep_tang_dan(ds))
print("Giá trị của khóa 'b':", lay_gia_tri(tu_dien, "b"))