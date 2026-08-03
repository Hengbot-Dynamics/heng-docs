# 创建一个UI用于录制播放动作
# 通过websocket连接服务器，收发json数据

import os
import websocket
import json
import time
import threading
from tkinter import *

# 创建一个UI类存储需要使用的变量
class RecordUI:
    def __init__(self):
        # 默认地址
        self.default_port = '10710'
        self.default_path = '/getjson'
        self.ip_address = '0.0.0.0'
        self.ws_url = f'ws://{self.ip_address}:{self.default_port}{self.default_path}'
        # 默认文件名
        self.filename = 'record.txt'
        # 默认模式
        self.mode = 'Idle'  # 'Idle', 'Record', 'Play', 'PauseRecord', 'PausePlay'
        # 任务线程
        self.t = None

        # 创建一个窗口
        self.window = Tk()
        self.window.title('Record')
        self.window.geometry('300x200')
        # 创建两个个按钮，并列显示
        self.record_button = Button(self.window, text='Record', command=self.record)
        self.record_button.pack(side=LEFT)
        self.play_button = Button(self.window, text='Play', command=self.play)
        self.play_button.pack(side=RIGHT)
        # 创建一个输入框(宽度与窗口相同)，用于输入地址。创建一个按钮，用于更新地址后重新连接。
        self.ip_entry = Entry(self.window)
        self.ip_entry.pack(fill=X)
        self.ip_entry.insert(0, self.ip_address)
        self.update_button = Button(self.window, text='ReConnect', command=self.update)
        self.update_button.pack()

        # 创建一个按钮用于暂停
        self.pause_button = Button(self.window, text='Pause', command=self.pause)
        self.pause_button.pack()

        # 创建一个标签用于显示模式
        self.mode_label = Label(self.window, text=self.mode)
        self.mode_label.pack()


        # 创建一个websocket连接
        self.ws = websocket.WebSocketApp(self.ws_url, on_open=self.on_open, on_message=self.on_message)
        # 创建一个线程用于连接服务器
        self.t = threading.Thread(target=self.ws.run_forever)
        self.t.start()
        # 进入消息循环
        self.window.mainloop()

    # 连接websocket服务器
    def on_open(self, ws):
        # 发送指令
        ws.send('{"cmd":"Reset_Robot_Position"}')

    # 接收json数据
    def on_message(self, ws, message):
        # 保存到本地txt文件
        with open(self.filename, 'a', encoding='utf-8') as f:
            # 确认message是json格式，且feedback字段为Recording
            data = json.loads(message)
            if 'feedback' in data and data['feedback'] == 'Recording':
                f.write(message + '\n')
                f.flush()
        print(message)

    # 暂停
    # 根据模式不同显示的文字不同
    def pause(self):
        if self.mode == 'Record':
            self.ws.send('{"cmd":"Pause_Record"}')
            self.mode = 'PauseRecord'
            self.mode_label.config(text=self.mode)
            self.pause_button.config(text='Resume')
        elif self.mode == 'Play':
            self.ws.send('{"cmd":"Pause_Play"}')
            self.mode = 'PausePlay'
            self.mode_label.config(text=self.mode)
            self.pause_button.config(text='Resume')
        elif self.mode == 'PauseRecord':
            self.ws.send('{"cmd":"Resume_Record"}')
            self.mode = 'Record'
            self.mode_label.config(text=self.mode)
            self.pause_button.config(text='Pause')
        elif self.mode == 'PausePlay':
            self.ws.send('{"cmd":"Resume_Play"}')
            self.mode = 'Play'
            self.mode_label.config(text=self.mode)
            self.pause_button.config(text='Pause')

    # 录制
    def record(self):
        if self.mode == 'Idle':
            # 如果存在record.txt文件，则删除
            if os.path.exists(self.filename):
                os.remove(self.filename)
            self.ws.send('{"cmd":"Set_Parameter","type":"AIA_FrontLeft","parameter":"Output_Torque", "value":"Limit"}')
            self.ws.send('{"cmd":"Set_Parameter","type":"AIA_FrontRight","parameter":"Output_Torque", "value":"Limit"}')
            self.ws.send('{"cmd":"Set_Parameter","type":"AIA_BackLeft","parameter":"Output_Torque", "value":"Limit"}')
            self.ws.send('{"cmd":"Set_Parameter","type":"AIA_BackRight","parameter":"Output_Torque", "value":"Limit"}')
            self.ws.send('{"cmd":"Set_Parameter","type":"AIA_Head","parameter":"Output_Torque", "value":"Limit"}')
            self.ws.send('{"cmd":"Start_Record"}')
            self.mode = 'Record'
            self.mode_label.config(text=self.mode)
            self.record_button.config(text='Stop')
        elif self.mode == 'Record' or self.mode == 'PauseRecord':
            self.ws.send('{"cmd":"Stop_Record"}')
            self.mode = 'Idle'
            self.mode_label.config(text=self.mode)
            self.record_button.config(text='Record')

    # 播放
    def play(self):
        if self.mode == 'Idle':
            self.ws.send('{"cmd":"Set_Parameter","type":"AIA_FrontLeft","parameter":"Output_Torque", "value":"UnLimit"}')
            self.ws.send('{"cmd":"Set_Parameter","type":"AIA_FrontRight","parameter":"Output_Torque", '
                         '"value":"UnLimit"}')
            self.ws.send('{"cmd":"Set_Parameter","type":"AIA_BackLeft","parameter":"Output_Torque", "value":"UnLimit"}')
            self.ws.send('{"cmd":"Set_Parameter","type":"AIA_BackRight","parameter":"Output_Torque", "value":"UnLimit"}')
            self.ws.send('{"cmd":"Set_Parameter","type":"AIA_Head","parameter":"Output_Torque", "value":"UnLimit"}')
            self.ws.send('{"cmd":"Start_Play"}')
            self.mode = 'Play'
            self.mode_label.config(text=self.mode)
            self.play_button.config(text='Stop')
            # 创建一个线程，读取json数据，转换为播放的json数据，发送到websocket服务器
            self.t = threading.Thread(target=self.play_json)
            self.t.start()

        elif self.mode == 'Play' or self.mode == 'PausePlay':
            self.ws.send('{"cmd":"Stop_Play"}')
            self.mode = 'Idle'

            self.mode_label.config(text=self.mode)
            self.play_button.config(text='Play')


    # 读取json数据，转换为播放的json数据，发送到websocket服务器
    def play_json(self):
        with open(self.filename, 'r', encoding='utf-8') as f:
            for line in f:
                if self.mode == 'PausePlay':
                    while self.mode == 'PausePlay':
                        time.sleep(0.1)
                elif self.mode == 'Idle':
                    break
                data = json.loads(line)
                data.pop('feedback')
                data['cmd'] = 'Playing'
                data = json.dumps(data)
                self.ws.send(data)
                print(data)
                time.sleep(0.01)
        self.ws.send('{"cmd":"Stop_Play"}')
        self.mode = 'Idle'
        self.play_button.config(text='Play')
        self.mode_label.config(text=self.mode)

        # 更新地址
    def update(self):
        self.ip_address = self.ip_entry.get()
        self.ws_url = f'ws://{self.ip_address}:{self.default_port}{self.default_path}'
        self.ws = websocket.WebSocketApp(self.ws_url, on_open=self.on_open, on_message=self.on_message)
        self.t = threading.Thread(target=self.ws.run_forever)
        self.t.start()

# 主函数
if __name__ == '__main__':
    # 创建一个UI
    record_ui = RecordUI()
    print('end')



