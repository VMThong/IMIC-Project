from lap_trinh_huong_doi_tuong import employee

ds_nv=[]
yes_no='y'
while True:
    if yes_no=='y':
        e=employee()
        e.set_info()
        ds_nv.append(e)
        yes_no=input(
"""Nhấn y nếu muốn nhập tiếp thông tin người khác!
Nhập ký tự bất kỳ ngoại trừ "y" để dừng!!
Bạn chọn: """)
    else:
        break

for i in ds_nv:
    i.prin_info()

sua_thong_tin= input('Ấn y để sửa thông tin ')

if sua_thong_tin=='y':
    id_cua_ban=input('Nhập ID ')
    for i in ds_nv:
        if i.employee_id==id_cua_ban:
            a=input("""Bạn muốn sửa gì?
            Bấm "1": sửa tên
            Bấm "2": sửa email
            Bấm "3": sửa tuổi
            """)
            if a=='1':
                i.employee_name= input('Mời bạn nhập name ')
                print('Tên đã được sửa')
            elif a=='2':
                i.employee_email= input('Mời bạn nhập email ')
                print('Mail đã được sửa')
            elif a=='3':
                i.age= input('Mời bạn nhập tuổi ')
                print('Tuổi đã được sửa')
            break
    else:
        print('Không có nhân viên này')
    for i in ds_nv:
        i.prin_info()

