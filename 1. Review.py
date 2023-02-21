class Tinhtoan:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def Tong(self):
        print('Tổng = ', a+b)
    def Nhan(self):
        print('Tích = ', a * b)
    def Chia(self):
        if b==0:
            print('Không thể chia cho 0!!')
        else:
            print('Thương = ',a/b)
menu = {
    1: 'Cộng 2 số',
    2: 'Nhân 2 số',
    3: 'Chia 2 số',
    4: 'Thoát'
}
def print_meanu(menu):
    for key in menu.keys():
        print(key,':',menu[key])
    return
while True:
    print_meanu(menu)
    opt=int(input('Nhập lựa chọn của bạn: '))
    if opt==4:
        print('Bạn đã thoát!')
        exit()
    a = float(input('Số thứ nhất: '))
    b = float(input('Số thứ hai: '))
    n = Tinhtoan(a,b)
    if opt==1:
        n.Tong()
    elif opt==2:
        n.Nhan()
    elif opt==3:
        n.Chia()
    else:
        print('Nhập không đúng cú pháp')
