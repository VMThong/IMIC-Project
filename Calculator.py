from tkinter import *
from functools import partial

top = Tk()

def chuyen_danh_sach_thanh_chuoi(ds):
    chuoi_str = ''
    for i in ds:
        chuoi_str += str(i)
    return chuoi_str

ds = ['0']
ds.clear()
chuoi_dau_vao = 0

dau = ['0']
a = 0
c = 0
b = 0

def dau_vao(a):
    if c == 0:
        ds.append(a)
        label_a.config(text=chuyen_danh_sach_thanh_chuoi(ds))
    else:
        ds.append(a)
        label_b.config(text=chuyen_danh_sach_thanh_chuoi(ds))

def xoa_tu_cuoi():
    if ds == []:
        print('Bạn chưa điền số')
        exit()
    if len(ds) > 1 and c == 0 and ds[0] == ds[-1]:
        g = ds[0]
        ds[0] = 'a'
        ds.remove(ds[-1])
        ds[0] = g
        label_a.config(text=chuyen_danh_sach_thanh_chuoi(ds))
    elif len(ds) != 0 and c == 0:
        ds.remove(ds[-1])
        label_a.config(text=chuyen_danh_sach_thanh_chuoi(ds))
    elif len(ds) > 1 and c != 0 and ds[0] == ds[-1]:
        g = ds[0]
        ds[0] = 'a'
        ds.remove(ds[-1])
        ds[0] = g
        label_b.config(text=chuyen_danh_sach_thanh_chuoi(ds))
    elif len(ds) != 0 and c != 0:
        ds.remove(ds[-1])
        label_b.config(text=chuyen_danh_sach_thanh_chuoi(ds))
    else:
        if len(ds) == 0 and c == 0:
            label_a.config(text="")
        elif len(ds) == 0 and c != 0:
            label_b.config(text="")

def tinh_cong():
    dau.clear()
    dau.append('+')
    global a, b, c
    if len(ds) != 0 and ds[0] == '.':
        print('Bạn chưa điền số trước dấu chấm')
        button_reset.invoke()
        exit()
    elif len(ds) != 0:
        chuoi_dau_vao = float(chuyen_danh_sach_thanh_chuoi(ds))
        a = float(chuoi_dau_vao)
        c = 1
        b = 0
        ds.clear()
    else:
        print('Bạn bấm dấu quá nhiều')
        button_reset.invoke()
        exit()

def tinh_tru():
    dau.clear()
    dau.append('-')
    global a,b, c
    if len(ds) != 0 and ds[0] == '.':
        print('Bạn chưa điền số trước dấu chấm')
        button_reset.invoke()
        exit()
    elif len(ds) != 0:
        chuoi_dau_vao = float(chuyen_danh_sach_thanh_chuoi(ds))
        a = float(chuoi_dau_vao)
        c = 1
        b = 0
        ds.clear()
    else:
        print('Bạn bấm dấu quá nhiều')
        button_reset.invoke()
        exit()

def tinh_nhan():
    dau.clear()
    dau.append('*')
    global a,b, c
    if len(ds) != 0 and ds[0] == '.':
        print('Bạn chưa điền số trước dấu chấm')
        button_reset.invoke()
        exit()
    elif len(ds) != 0:
        chuoi_dau_vao = float(chuyen_danh_sach_thanh_chuoi(ds))
        a = float(chuoi_dau_vao)
        c = 1
        b = 0
        ds.clear()
    else:
        print('Bạn bấm dấu quá nhiều')
        button_reset.invoke()
        exit()

def tinh_chia():
    dau.clear()
    dau.append('/')
    global a,b, c
    if len(ds) != 0 and ds[0] == '.':
        print('Bạn chưa điền số trước dấu chấm')
        button_reset.invoke()
        exit()
    elif len(ds) != 0:
        chuoi_dau_vao = float(chuyen_danh_sach_thanh_chuoi(ds))
        a = float(chuoi_dau_vao)
        c = 1
        b = 0
        ds.clear()
    else:
        print('Bạn bấm dấu quá nhiều')
        button_reset.invoke()
        exit()

def bang_result():
    if len(ds) == 0:
        print('Bạn chưa điền đủ giá trị để tính')
        button_reset.invoke()
        exit()
    b = float(chuyen_danh_sach_thanh_chuoi(ds))
    if len(ds) != 0 and ds[0] == '.':
        print('Bạn chưa điền số trước dấu chấm')
        button_reset.invoke()
        exit()
    if dau[0] == '+':
        dau.clear()
        label_c.config(text=a + b)
    elif dau[0] == '-':
        dau.clear()
        label_c.config(text=a - b)
    elif dau[0] == '*':
        dau.clear()
        label_c.config(text=a * b)
    elif dau[0] == '/' and b != 0:
        dau.clear()
        label_c.config(text=a / b)
    button_reset.invoke()

def data_reset():
    global a, b, c, dau, chuoi_dau_vao, ds
    ds = ['0']
    ds.clear()
    chuoi_dau_vao = 0
    dau = ['0']
    a = float(chuoi_dau_vao)
    c = 0
    b = 0  # Không xóa được a
    label_a.config(text="")
    label_b.config(text="")

button_so_0 = Button(master=top, text='0', command=partial(dau_vao, 0), bg='cyan', width=5)
button_so_0.grid(row=3, column=0)

button_dau_cham_phay = Button(master=top, text='.', command=partial(dau_vao, '.'), width=5, bg='cyan')
button_dau_cham_phay.grid(row=3, column=1)
button_dau_xoa = Button(master=top, text='Xóa', command=xoa_tu_cuoi, width=5, fg='red')
button_dau_xoa.grid(row=3, column=2)
button_dau_chia = Button(master=top, text='/', command=tinh_chia, width=5, bg='gray')
button_dau_chia.grid(row=3, column=3)

button_so_1 = Button(master=top, text='1', command=partial(dau_vao, 1), bg='cyan', width=5)
button_so_1.grid(row=2, column=0)
button_so_2 = Button(master=top, text='2', command=partial(dau_vao, 2), bg='cyan', width=5)
button_so_2.grid(row=2, column=1)
button_so_3 = Button(master=top, text='3', command=partial(dau_vao, 3), bg='cyan', width=5)
button_so_3.grid(row=2, column=2)
button_dau_cong = Button(master=top, text='+', command=tinh_cong, width=5, bg='gray')
button_dau_cong.grid(row=2, column=3)

button_so_4 = Button(master=top, text='4', command=partial(dau_vao, 4), bg='cyan', width=5)
button_so_4.grid(row=1, column=0)
button_so_5 = Button(master=top, text='5', command=partial(dau_vao, 5), bg='cyan', width=5)
button_so_5.grid(row=1, column=1)
button_so_6 = Button(master=top, text='6', command=partial(dau_vao, 6), bg='cyan', width=5)
button_so_6.grid(row=1, column=2)
button_dau_tru = Button(master=top, text='-', command=tinh_tru, width=5, bg='gray')
button_dau_tru.grid(row=1, column=3)

button_so_7 = Button(master=top, text='7', command=partial(dau_vao, 7), bg='cyan', width=5)
button_so_7.grid(row=0, column=0)
button_so_8 = Button(master=top, text='8', command=partial(dau_vao, 8), bg='cyan', width=5)
button_so_8.grid(row=0, column=1)
button_so_9 = Button(master=top, text='9', command=partial(dau_vao, 9), bg='cyan', width=5)
button_so_9.grid(row=0, column=2)
button_dau_nhan = Button(master=top, text='*', command=tinh_nhan, width=5, bg='gray')
button_dau_nhan.grid(row=0, column=3)

label_nhan_dap_so = Label(master=top, text="Kết quả", width=5)
label_nhan_dap_so.grid(row=5, column=0)
button_dau_bang = Button(master=top, text='=', command=bang_result, width=5,bg='gray')
button_dau_bang.grid(row=5, column=1)
label_c = Label(master=top, text="", bg='pink', width=5, fg='red')
label_c.grid(row=5, column=2)
button_reset = Button(master=top, text='Reset', command=data_reset, width=5,bg='red')
button_reset.grid(row=5, column=3)

label_nhan_a = Label(master=top, text="a=", width=5)
label_nhan_a.grid(row=4, column=0)
label_a = Label(master=top, text="", bg='yellow', width=5)
label_a.grid(row=4, column=1)
label_nhan_b = Label(master=top, text="b=", width=5)
label_nhan_b.grid(row=4, column=2)
label_b = Label(master=top, text="", bg='yellow', width=5)
label_b.grid(row=4, column=3)

top.mainloop()
