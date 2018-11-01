#encoding: utf-8
'''
    author: yiouejv
    email: yiouejv@126.com
    blog: bolg.syzyb.com
'''

import tkinter as tk
from time import sleep
from datetime import datetime

INTERVAL = 60*10  # 设置时间间隔
tips = '忙了这么久，喝点水吧~'


def ok_btn_event(tip):
    '''
        传入tip窗口，把窗口关闭
        写入"有乖乖喝水"到login.txt日志文件中
    '''
    tip.destroy()
    with open('login.txt', 'at', encoding='utf-8') as wf:
        now = datetime.now()
        wf.write(str(now)[:19] + '* 有乖乖喝水哦~' + '\n')


def ignore_btn_envent(tip):
    '''
         传入tip窗口，把窗口关闭
         写入"没理我..."到login.txt日志文件中
    '''
    tip.destroy()
    with open('login.txt', 'at', encoding='utf-8') as wf:
        now = datetime.now()
        wf.write(str(now)[:19] + '* 没理我......' + '\n')




def bubble_tip():
    # 创建一个窗口
    tip = tk.Tk()
    tip.geometry('350x120+1100+600')
    tip.title('传奇喝水小程序...')
    tip.wm_maxsize(350, 120)
    tk.Label(tip, text=tips, font=('黑体', 20)).pack()
    # 创建“好的”按钮
    ok_btn = tk.Button(tip, text='好的', width=5, height=1, background='#66ff66',
                       command=lambda: ok_btn_event(tip))
    ok_btn.place(x=280, y=80)
    # 创建“忽视”按钮
    ignore_btn = tk.Button(tip, text='忽视', width=5, height=1, background='#ff3333	',
                           command=lambda:ignore_btn_envent(tip))
    ignore_btn.place(x=200, y=80)
    tip.mainloop()


def main():
    while True:
        sleep(INTERVAL)
        bubble_tip()


if __name__ == '__main__':
    main()

