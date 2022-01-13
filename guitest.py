# -*- coding:utf-8 -*-
import tkinter as tk
coin = 200
def shop(coin):

    window = tk.Tk()
    window.title("商店")  # window标题
    window.maxsize(300, 200)  # window的大小
    window.minsize(500, 450)  # 通过设置最大最小一样，可以实现window不可缩放大小
    var = tk.StringVar()
    c = tk.StringVar()
    l = tk.Label(window, text='你好！这里是商店', bg='blue', font=('Arial', 13), width=40, height=3)
    e = tk.Label(window, textvariable=var, bg='yellow', fg='green', font=('Arial', 13), width=40, height=3)
    l.place(x='70', y='1')
    e.place(x='70',y='60')
    on_hit = False
    o = tk.Label(window, textvariable=c, bg='yellow', fg='green', font=('Arial', 13), width=20, height=3)
    o.place(x='300', y='370')
    c.set(coin)
    def 点():
        global coin
        if coin <= 0:
            window.destroy()
        else:
            var.set('你买了药')
            coin -= 30
            c.set(coin)
        return coin

    def close():
        window.destroy()
    b = tk.Button(window, font=('Arial', 12), width=9, height=3, text="med", command=点)
    b.place(x='1', y='150')
    v = tk.Button(window, font=('Arial', 12), width=9, height=3, text="close", command=close)
    v.place(x='1',y='380')
    window.mainloop()
    print(coin)
    return coin
shop(coin)