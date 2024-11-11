# 通过GUI编辑要发送的json关键帧数据，可以调整机器人的body，footpoint的位置，然后通过websocket发送到服务器
# Websocket连接的地址为：ws://192.168.8.151:10710/getjson

import os
import tkinter as tk
from tkinter import filedialog, simpledialog
from tkinter import messagebox
import json
import threading
import websocket
import time


# 通过UI编辑要发送的json关键帧数据，可以调整机器人的body，footpoint的位置，然后通过websocket发送到服务器
# 以10ms的频率发送到机器人

class DefaultValue:
    def __init__(self):
        self.pitch = 0
        self.roll = 0
        self.tran_x = 0
        self.tran_y = 0
        self.tran_z = 141.0
        self.yaw = 0.0
        self.pitch_head = 0.0
        self.yaw_head = 0.0
        self.front_left_leg_x = 75
        self.front_left_leg_y = 55
        self.front_left_leg_z = 0
        self.front_right_leg_x = 75
        self.front_right_leg_y = -55
        self.front_right_leg_z = 0
        self.back_left_leg_x = -75
        self.back_left_leg_y = 55
        self.back_left_leg_z = 0
        self.back_right_leg_x = -75
        self.back_right_leg_y = -55
        self.back_right_leg_z = 0
        self.acc = 'Fastest'
        self.speed = 'Fastest'
        self.time = 10


# 创建UI
class KeyFrameUI:
    def __init__(self, master):
        self.ws = websocket.WebSocket()
        # 弹出对话框获取用户输入的IP地址
        ip_address = simpledialog.askstring("Input", "Enter the IP address:",
                                            parent=master)
        if ip_address:
            self.ws.connect(f'ws://{ip_address}:10710/getjson')  # 使用用户输入的IP地址
        else:
            print("No IP address entered. Cannot connect to websocket.")
        self.ws.send('{"cmd":"Mode_Switch","target":"Edit_Mode"}')
        self.master = master
        self.master.title('KeyFrameUI')
        self.master.geometry('1024x1280')
        self.master.resizable(1, 1)
        self.master.protocol('WM_DELETE_WINDOW', self.on_closing)

        self.pitch = 0
        self.roll = 0
        self.tran_x = 0
        self.tran_y = 0
        self.tran_z = 141
        self.yaw = 0.0
        self.pitch_head = 0.0
        self.yaw_head = 0.0

        self.front_left_leg_x = 75
        self.front_left_leg_y = 55
        self.front_left_leg_z = 0
        self.front_right_leg_x = 75
        self.front_right_leg_y = -55
        self.front_right_leg_z = 0
        self.back_left_leg_x = -75
        self.back_left_leg_y = 55
        self.back_left_leg_z = 0
        self.back_right_leg_x = -75
        self.back_right_leg_y = -55
        self.back_right_leg_z = 0

        self.acc = 'Slowest'
        self.speed = 'Slowest'
        self.time = 10
        self.mode = 'Edit_Mode'
        self.key_file_name = 'keyframe.txt'  # 默认打开读写的关键帧文件名称
        self.last_time = 0  # 关键帧文件上次修改时间
        self.current_key_frame_index = 0

        self.create_widgets()
        self.create_thread()

    # 创建控件
    def create_widgets(self):
        # 创建控件
        self.body_frame = tk.Frame(self.master)
        self.body_frame.pack()
        self.body_label = tk.Label(self.body_frame, text='Body')
        self.body_label.grid(row=0, column=0, columnspan=2)
        self.pitch_label = tk.Label(self.body_frame, text='pitch')
        self.pitch_label.grid(row=1, column=0)
        self.pitch_scale = tk.Scale(self.body_frame, from_=-1, to=1, resolution=0.01, length=500, orient=tk.HORIZONTAL,
                                    command=self.set_pitch)
        self.pitch_scale.grid(row=1, column=1)
        self.roll_label = tk.Label(self.body_frame, text='roll')
        self.roll_label.grid(row=2, column=0)
        self.roll_scale = tk.Scale(self.body_frame, from_=-1, to=1, resolution=0.01, length=500, orient=tk.HORIZONTAL,
                                   command=self.set_roll)
        self.roll_scale.grid(row=2, column=1)
        self.tran_x_label = tk.Label(self.body_frame, text='tran_x')
        self.tran_x_label.grid(row=3, column=0)
        self.tran_x_scale = tk.Scale(self.body_frame, from_=-50, to=50, resolution=0.01, length=500,
                                     orient=tk.HORIZONTAL, command=self.set_tran_x)
        self.tran_x_scale.grid(row=3, column=1)
        self.tran_y_label = tk.Label(self.body_frame, text='tran_y')
        self.tran_y_label.grid(row=4, column=0)
        self.tran_y_scale = tk.Scale(self.body_frame, from_=-50, to=50, resolution=0.01, length=500,
                                     orient=tk.HORIZONTAL, command=self.set_tran_y)
        self.tran_y_scale.grid(row=4, column=1)
        self.tran_z_label = tk.Label(self.body_frame, text='tran_z')
        self.tran_z_label.grid(row=5, column=0)
        # 设置tran_z的初始值141
        self.tran_z_scale = tk.Scale(self.body_frame, from_=0, to=170, resolution=0.5, orient=tk.HORIZONTAL,
                                     command=self.set_tran_z, length=500, variable=tk.IntVar(value=self.tran_z))
        self.tran_z_scale.grid(row=5, column=1)
        self.yaw_label = tk.Label(self.body_frame, text='yaw')
        self.yaw_label.grid(row=6, column=0)
        self.yaw_scale = tk.Scale(self.body_frame, from_=-1, to=1, resolution=0.01, length=500, orient=tk.HORIZONTAL,
                                  command=self.set_yaw)
        self.yaw_scale.grid(row=6, column=1)

        self.footpoint_frame = tk.Frame(self.master)
        self.footpoint_frame.pack()
        self.footpoint_label = tk.Label(self.footpoint_frame, text='FootPoint')
        self.footpoint_label.grid(row=0, column=0, columnspan=2)
        self.front_left_leg_x_label = tk.Label(self.footpoint_frame, text='front_left_leg_x')
        self.front_left_leg_x_label.grid(row=1, column=0)
        self.front_left_leg_x_scale = tk.Scale(self.footpoint_frame, from_=-25, to=175, resolution=1, length=300,
                                               orient=tk.HORIZONTAL, command=self.set_front_left_leg_x,
                                               variable=tk.IntVar(value=self.front_left_leg_x))
        self.front_left_leg_x_scale.grid(row=1, column=1)
        self.front_left_leg_y_label = tk.Label(self.footpoint_frame, text='front_left_leg_y')
        self.front_left_leg_y_label.grid(row=2, column=0)
        self.front_left_leg_y_scale = tk.Scale(self.footpoint_frame, from_=-45, to=155, resolution=1, length=300,
                                               orient=tk.HORIZONTAL, command=self.set_front_left_leg_y,
                                               variable=tk.IntVar(value=self.front_left_leg_y))
        self.front_left_leg_y_scale.grid(row=2, column=1)
        self.front_left_leg_z_label = tk.Label(self.footpoint_frame, text='front_left_leg_z')
        self.front_left_leg_z_label.grid(row=3, column=0)
        self.front_left_leg_z_scale = tk.Scale(self.footpoint_frame, from_=-100, to=100, resolution=1, length=300,
                                               orient=tk.HORIZONTAL, command=self.set_front_left_leg_z,
                                               variable=tk.IntVar(value=self.front_left_leg_z))
        self.front_left_leg_z_scale.grid(row=3, column=1)
        self.front_right_leg_x_label = tk.Label(self.footpoint_frame, text='front_right_leg_x')
        self.front_right_leg_x_label.grid(row=4, column=0)
        self.front_right_leg_x_scale = tk.Scale(self.footpoint_frame, from_=-25, to=175, resolution=1, length=300,
                                                orient=tk.HORIZONTAL, command=self.set_front_right_leg_x,
                                                variable=tk.IntVar(value=self.front_right_leg_x))
        self.front_right_leg_x_scale.grid(row=4, column=1)
        self.front_right_leg_y_label = tk.Label(self.footpoint_frame, text='front_right_leg_y')
        self.front_right_leg_y_label.grid(row=5, column=0)
        self.front_right_leg_y_scale = tk.Scale(self.footpoint_frame, from_=-155, to=45, resolution=1, length=300,
                                                orient=tk.HORIZONTAL, command=self.set_front_right_leg_y,
                                                variable=tk.IntVar(value=self.front_right_leg_y))
        self.front_right_leg_y_scale.grid(row=5, column=1)
        self.front_right_leg_z_label = tk.Label(self.footpoint_frame, text='front_right_leg_z')
        self.front_right_leg_z_label.grid(row=6, column=0)
        self.front_right_leg_z_scale = tk.Scale(self.footpoint_frame, from_=-100, to=100, resolution=1, length=300,
                                                orient=tk.HORIZONTAL, command=self.set_front_right_leg_z,
                                                variable=tk.IntVar(value=self.front_right_leg_z))
        self.front_right_leg_z_scale.grid(row=6, column=1)
        self.back_left_leg_x_label = tk.Label(self.footpoint_frame, text='back_left_leg_x')
        self.back_left_leg_x_label.grid(row=7, column=0)
        self.back_left_leg_x_scale = tk.Scale(self.footpoint_frame, from_=-175, to=25, resolution=1, length=300,
                                              orient=tk.HORIZONTAL, command=self.set_back_left_leg_x,
                                              variable=tk.IntVar(value=self.back_left_leg_x))
        self.back_left_leg_x_scale.grid(row=7, column=1)
        self.back_left_leg_y_label = tk.Label(self.footpoint_frame, text='back_left_leg_y')
        self.back_left_leg_y_label.grid(row=8, column=0)
        self.back_left_leg_y_scale = tk.Scale(self.footpoint_frame, from_=-45, to=155, resolution=1, length=300,
                                              orient=tk.HORIZONTAL, command=self.set_back_left_leg_y,
                                              variable=tk.IntVar(value=self.back_left_leg_y))
        self.back_left_leg_y_scale.grid(row=8, column=1)
        self.back_left_leg_z_label = tk.Label(self.footpoint_frame, text='back_left_leg_z')
        self.back_left_leg_z_label.grid(row=9, column=0)
        self.back_left_leg_z_scale = tk.Scale(self.footpoint_frame, from_=-100, to=100, resolution=1, length=300,
                                              orient=tk.HORIZONTAL, command=self.set_back_left_leg_z,
                                              variable=tk.IntVar(value=self.back_left_leg_z))
        self.back_left_leg_z_scale.grid(row=9, column=1)
        self.back_right_leg_x_label = tk.Label(self.footpoint_frame, text='back_right_leg_x')
        self.back_right_leg_x_label.grid(row=10, column=0)
        self.back_right_leg_x_scale = tk.Scale(self.footpoint_frame, from_=-175, to=25, resolution=1, length=300,
                                               orient=tk.HORIZONTAL, command=self.set_back_right_leg_x,
                                               variable=tk.IntVar(value=self.back_right_leg_x))
        self.back_right_leg_x_scale.grid(row=10, column=1)
        self.back_right_leg_y_label = tk.Label(self.footpoint_frame, text='back_right_leg_y')
        self.back_right_leg_y_label.grid(row=11, column=0)
        self.back_right_leg_y_scale = tk.Scale(self.footpoint_frame, from_=-155, to=45, resolution=1, length=300,
                                               orient=tk.HORIZONTAL, command=self.set_back_right_leg_y,
                                               variable=tk.IntVar(value=self.back_right_leg_y))
        self.back_right_leg_y_scale.grid(row=11, column=1)
        self.back_right_leg_z_label = tk.Label(self.footpoint_frame, text='back_right_leg_z')
        self.back_right_leg_z_label.grid(row=12, column=0)
        self.back_right_leg_z_scale = tk.Scale(self.footpoint_frame, from_=-100, to=100, resolution=1, length=300,
                                               orient=tk.HORIZONTAL, command=self.set_back_right_leg_z,
                                               variable=tk.IntVar(value=self.back_right_leg_z))
        self.back_right_leg_z_scale.grid(row=12, column=1)

        self.head_frame = tk.Frame(self.master)
        self.head_frame.pack()
        self.head_label = tk.Label(self.head_frame, text='Head')
        self.head_label.grid(row=0, column=0, columnspan=2)
        self.pitch_head_label = tk.Label(self.head_frame, text='pitch')
        self.pitch_head_label.grid(row=1, column=0)
        self.pitch_head_scale = tk.Scale(self.head_frame, from_=-1, to=1, resolution=0.01, length=500,
                                         orient=tk.HORIZONTAL, command=self.set_pitch_head)
        self.pitch_head_scale.grid(row=1, column=1)
        self.yaw_head_label = tk.Label(self.head_frame, text='yaw')
        self.yaw_head_label.grid(row=2, column=0)
        self.yaw_head_scale = tk.Scale(self.head_frame, from_=-1, to=1, resolution=0.01, length=500,
                                       orient=tk.HORIZONTAL, command=self.set_yaw_head)
        self.yaw_head_scale.grid(row=2, column=1)

        # 时间滑条
        self.time_frame = tk.Frame(self.master)
        self.time_frame.pack()
        self.time_label = tk.Label(self.time_frame, text='Time')
        self.time_label.grid(row=0, column=0, columnspan=2)
        self.time_scale = tk.Scale(self.time_frame, from_=10, to=5000, resolution=1, length=500, orient=tk.HORIZONTAL,
                                   command=self.set_time, variable=tk.IntVar(value=self.time))
        self.time_scale.grid(row=1, column=0, columnspan=2)

        # 速度和加速度下拉菜单
        self.speed_frame = tk.Frame(self.master)
        self.speed_frame.pack()
        self.speed_label = tk.Label(self.speed_frame, text='Speed')
        self.speed_label.grid(row=0, column=0)
        self.acc_label = tk.Label(self.speed_frame, text='Acc')
        self.acc_label.grid(row=0, column=1)
        self.speed_var = tk.StringVar()
        self.acc_var = tk.StringVar()
        self.speed_var.set('Fastest')
        self.acc_var.set('Fastest')
        self.speed_menu = tk.OptionMenu(self.speed_frame, self.speed_var, 'Slowest', 'Slow', 'Fast', 'Fastest',
                                        command=self.set_speed)
        self.speed_menu.grid(row=1, column=0)
        self.acc_menu = tk.OptionMenu(self.speed_frame, self.acc_var, 'Slowest', 'Slow', 'Fast', 'Fastest',
                                      command=self.set_acc)
        self.acc_menu.grid(row=1, column=1)

        # 创建按钮
        # 复位按钮
        self.reset_button = tk.Button(self.master, text='Reset', command=self.reset)
        self.reset_button.pack()

        # 限幅按钮
        self.limit_button = tk.Button(self.master, text='Limit', command=self.limit)
        self.limit_button.pack()

        # 解除限幅按钮
        self.unlimit_button = tk.Button(self.master, text='Unlimit', command=self.unlimit)
        self.unlimit_button.pack()

        # 保存按钮
        self.save_button = tk.Button(self.master, text='Save', command=self.save)
        self.save_button.pack()

        # 保存修改关键帧按钮
        self.save_button = tk.Button(self.master, text='Change_KeyFrame', command=self.save_key_frame)
        self.save_button.pack()

        # 播放模式切换按钮(一行两个按键)，有编辑模式和播放模式，编辑模式下发送当前界面的关键帧，播放模式下播放keyframe.txt中的关键帧
        self.mode_frame = tk.Frame(self.master)
        self.mode_frame.pack()
        self.mode_label = tk.Label(self.mode_frame, text='Mode')
        self.mode_label.grid(row=0, column=0, columnspan=2)
        self.edit_button = tk.Button(self.mode_frame, text='Edit_Mode', command=self.edit_mode)
        self.edit_button.grid(row=1, column=0)
        self.play_button = tk.Button(self.mode_frame, text='Play_Mode', command=self.play_mode)
        self.play_button.grid(row=1, column=1)
        self.play_button = tk.Button(self.mode_frame, text='Idle_Mode', command=self.idle_mode)
        self.play_button.grid(row=1, column=2)

        # 创建一个侧边窗口 创建一个列表(tk.Listbox)用于按顺序显示文件中关键帧的计数，点击列表的某一项，可以将该项的关键帧信息显示在主窗口上
        # 该窗口上有打开文件按钮可以选择要打开的关键帧文件,默认情况下自动打开keyframe.txt，如果文件不存在则创建一个空的文件
        self.side_window = tk.Toplevel()
        self.side_window.title('KeyFrameList')
        self.side_window.geometry('300x600')
        self.side_window.resizable(1, 1)
        self.side_window.protocol('WM_DELETE_WINDOW', self.on_closing)
        # 创建列表
        self.key_frame_list = tk.Listbox(self.side_window, selectmode=tk.SINGLE)
        self.key_frame_list.pack(fill=tk.BOTH, expand=True)
        self.open_button = tk.Button(self.side_window, text='Open', command=self.open_file)
        self.open_button.pack()
        self.key_frame_list.bind('<Double-Button-1>', self.show_key_frame)
        # 默认打开keyframe.txt文件
        if not os.path.exists('keyframe.txt'):
            with open('keyframe.txt', 'w', encoding='utf-8') as f:
                f.write('')
                f.flush()
        with open('keyframe.txt', 'r', encoding='utf-8') as f:
            for line in f:
                self.key_frame_list.insert(tk.END, line)

    # 创建线程
    def create_thread(self):
        self.t = threading.Thread(target=self.send_thread)
        self.t.start()

    # 发送json数据
    def send(self):
        data = {
            "cmd": "Play_Keyframe",
            "acc": self.acc,
            "speed": self.speed,
            "time": 10,  # GUI演示用时间固定为10ms
            "Body": {
                "pitch": self.pitch,
                "roll": self.roll,
                "tran_x": self.tran_x,
                "tran_y": self.tran_y,
                "tran_z": self.tran_z,
                "yaw": self.yaw
            },
            "FootPoint": {
                "FrontLeftLeg": {
                    "x": self.front_left_leg_x,
                    "y": self.front_left_leg_y,
                    "z": self.front_left_leg_z
                },
                "FrontRightLeg": {
                    "x": self.front_right_leg_x,
                    "y": self.front_right_leg_y,
                    "z": self.front_right_leg_z
                },
                "BackLeftLeg": {
                    "x": self.back_left_leg_x,
                    "y": self.back_left_leg_y,
                    "z": self.back_left_leg_z
                },
                "BackRightLeg": {
                    "x": self.back_right_leg_x,
                    "y": self.back_right_leg_y,
                    "z": self.back_right_leg_z
                }
            },
            "Head": {
                "pitch": self.pitch_head,
                "yaw": self.yaw_head
            }
        }
        data = json.dumps(data)
        self.ws.send(data)
        print(data)

    # 序列化为json，保存到本地txt文件keyframe.txt
    def save(self):
        data = {
            "cmd": "Play_Keyframe",
            "acc": self.acc,
            "speed": self.speed,
            "time": self.time,
            "Body": {
                "pitch": self.pitch,
                "roll": self.roll,
                "tran_x": self.tran_x,
                "tran_y": self.tran_y,
                "tran_z": self.tran_z,
                "yaw": self.yaw
            },
            "FootPoint": {
                "FrontLeftLeg": {
                    "x": self.front_left_leg_x,
                    "y": self.front_left_leg_y,
                    "z": self.front_left_leg_z
                },
                "FrontRightLeg": {
                    "x": self.front_right_leg_x,
                    "y": self.front_right_leg_y,
                    "z": self.front_right_leg_z
                },
                "BackLeftLeg": {
                    "x": self.back_left_leg_x,
                    "y": self.back_left_leg_y,
                    "z": self.back_left_leg_z
                },
                "BackRightLeg": {
                    "x": self.back_right_leg_x,
                    "y": self.back_right_leg_y,
                    "z": self.back_right_leg_z
                }
            },
            "Head": {
                "pitch": self.pitch_head,
                "yaw": self.yaw_head
            }
        }
        data = json.dumps(data)
        with open('keyframe.txt', 'a', encoding='utf-8') as f:
            f.write(data + '\n')
            f.flush()
        print(data)

    # 复位
    def reset(self):
        self.pitch = DefaultValue().pitch
        self.roll = DefaultValue().roll
        self.tran_x = DefaultValue().tran_x
        self.tran_y = DefaultValue().tran_y
        self.tran_z = DefaultValue().tran_z
        self.yaw = DefaultValue().yaw
        self.pitch_head = DefaultValue().pitch_head
        self.yaw_head = DefaultValue().yaw_head
        self.front_left_leg_x = DefaultValue().front_left_leg_x
        self.front_left_leg_y = DefaultValue().front_left_leg_y
        self.front_left_leg_z = DefaultValue().front_left_leg_z
        self.front_right_leg_x = DefaultValue().front_right_leg_x
        self.front_right_leg_y = DefaultValue().front_right_leg_y
        self.front_right_leg_z = DefaultValue().front_right_leg_z
        self.back_left_leg_x = DefaultValue().back_left_leg_x
        self.back_left_leg_y = DefaultValue().back_left_leg_y
        self.back_left_leg_z = DefaultValue().back_left_leg_z
        self.back_right_leg_x = DefaultValue().back_right_leg_x
        self.back_right_leg_y = DefaultValue().back_right_leg_y
        self.back_right_leg_z = DefaultValue().back_right_leg_z
        self.pitch_scale.set(self.pitch)
        self.roll_scale.set(self.roll)
        self.tran_x_scale.set(self.tran_x)
        self.tran_y_scale.set(self.tran_y)
        self.tran_z_scale.set(self.tran_z)
        self.yaw_scale.set(self.yaw)
        self.pitch_head_scale.set(self.pitch_head)
        self.yaw_head_scale.set(self.yaw_head)
        self.front_left_leg_x_scale.set(self.front_left_leg_x)
        self.front_left_leg_y_scale.set(self.front_left_leg_y)
        self.front_left_leg_z_scale.set(self.front_left_leg_z)
        self.front_right_leg_x_scale.set(self.front_right_leg_x)
        self.front_right_leg_y_scale.set(self.front_right_leg_y)
        self.front_right_leg_z_scale.set(self.front_right_leg_z)
        self.back_left_leg_x_scale.set(self.back_left_leg_x)
        self.back_left_leg_y_scale.set(self.back_left_leg_y)
        self.back_left_leg_z_scale.set(self.back_left_leg_z)
        self.back_right_leg_x_scale.set(self.back_right_leg_x)
        self.back_right_leg_y_scale.set(self.back_right_leg_y)
        self.back_right_leg_z_scale.set(self.back_right_leg_z)
        self.ws.send('{"cmd":"Reset_Robot_Position"}')

    def limit(self):
        self.ws.send('{"cmd":"Set_Parameter","type":"AIA_FrontLeft","parameter":"Output_Torque", "value":"Limit"}')
        self.ws.send('{"cmd":"Set_Parameter","type":"AIA_FrontRight","parameter":"Output_Torque", "value":"Limit"}')
        self.ws.send('{"cmd":"Set_Parameter","type":"AIA_BackLeft","parameter":"Output_Torque", "value":"Limit"}')
        self.ws.send('{"cmd":"Set_Parameter","type":"AIA_BackRight","parameter":"Output_Torque", "value":"Limit"}')
        self.ws.send('{"cmd":"Set_Parameter","type":"AIA_Head","parameter":"Output_Torque", "value":"Limit"}')

    def unlimit(self):
        self.ws.send('{"cmd":"Set_Parameter","type":"AIA_FrontLeft","parameter":"Output_Torque", "value":"UnLimit"}')
        self.ws.send('{"cmd":"Set_Parameter","type":"AIA_FrontRight","parameter":"Output_Torque", "value":"UnLimit"}')
        self.ws.send('{"cmd":"Set_Parameter","type":"AIA_BackLeft","parameter":"Output_Torque", "value":"UnLimit"}')
        self.ws.send('{"cmd":"Set_Parameter","type":"AIA_BackRight","parameter":"Output_Torque", "value":"UnLimit"}')
        self.ws.send('{"cmd":"Set_Parameter","type":"AIA_Head","parameter":"Output_Torque", "value":"UnLimit"}')

    # 发送json数据线程
    def send_thread(self):
        while True:
            # 当关键帧文件内容发生变化时，刷新关键帧列表
            if os.path.getmtime(self.key_file_name) != self.last_time:
                self.last_time = os.path.getmtime(self.key_file_name)
                self.key_frame_list.delete(0, tk.END)
                with open(self.key_file_name, 'r', encoding='utf-8') as f:
                    for line in f:
                        self.key_frame_list.insert(tk.END, line)
            # 如果当前模式是编辑模式，则发送json数据
            if self.mode == 'Edit_Mode':
                self.send()
                time.sleep(0.1)
            # 如果当前模式是播放模式，则发送keyframe.txt中的json数据,发送结束切换到空闲模式
            elif self.mode == 'Play_Mode':
                with open('keyframe.txt', 'r', encoding='utf-8') as f:
                    for line in f:
                        self.ws.send(line)
                        print(line)
                        time.sleep(0.05)
                self.mode = 'Idle_Mode'

    # 设置pitch
    def set_pitch(self, value):
        self.pitch = float(value)

    # 设置roll
    def set_roll(self, value):
        self.roll = float(value)

    # 设置tran_x
    def set_tran_x(self, value):
        self.tran_x = float(value)

    # 设置tran_y
    def set_tran_y(self, value):
        self.tran_y = float(value)

    # 设置tran_z
    def set_tran_z(self, value):
        self.tran_z = float(value)

    # 设置yaw
    def set_yaw(self, value):
        self.yaw = float(value)

    # 设置front_left_leg_x
    def set_front_left_leg_x(self, value):
        self.front_left_leg_x = int(value)

    # 设置front_left_leg_y
    def set_front_left_leg_y(self, value):
        self.front_left_leg_y = int(value)

    # 设置front_left_leg_z
    def set_front_left_leg_z(self, value):
        self.front_left_leg_z = int(value)

    # 设置front_right_leg_x
    def set_front_right_leg_x(self, value):
        self.front_right_leg_x = int(value)

    # 设置front_right_leg_y
    def set_front_right_leg_y(self, value):
        self.front_right_leg_y = int(value)

    # 设置front_right_leg_z
    def set_front_right_leg_z(self, value):
        self.front_right_leg_z = int(value)

    # 设置back_left_leg_x
    def set_back_left_leg_x(self, value):
        self.back_left_leg_x = int(value)

    # 设置back_left_leg_y
    def set_back_left_leg_y(self, value):
        self.back_left_leg_y = int(value)

    # 设置back_left_leg_z
    def set_back_left_leg_z(self, value):
        self.back_left_leg_z = int(value)

    # 设置back_right_leg_x
    def set_back_right_leg_x(self, value):
        self.back_right_leg_x = int(value)

    # 设置back_right_leg_y
    def set_back_right_leg_y(self, value):
        self.back_right_leg_y = int(value)

    # 设置back_right_leg_z
    def set_back_right_leg_z(self, value):
        self.back_right_leg_z = int(value)

    # 设置pitch_head
    def set_pitch_head(self, value):
        self.pitch_head = float(value)

    # 设置yaw_head
    def set_yaw_head(self, value):
        self.yaw_head = float(value)

    # 设置time
    def set_time(self, value):
        self.time = int(value)

    # 设置速度
    def set_speed(self, value):
        self.speed = value

    # 设置加速度
    def set_acc(self, value):
        self.acc = value

    # 打开文件
    def open_file(self):
        self.key_file_name = filedialog.askopenfilename()
        self.key_frame_list.delete(0, tk.END)
        with open(self.key_file_name, 'r', encoding='utf-8') as f:
            for line in f:
                self.key_frame_list.insert(tk.END, line)

    # 重新读取关键帧文件
    def reread_key_frame(self, event):
        self.key_frame_list.delete(0, tk.END)
        with open(self.key_file_name, 'r', encoding='utf-8') as f:
            for line in f:
                self.key_frame_list.insert(tk.END, line)

    # 显示关键帧
    def show_key_frame(self, event):
        # 记录当前选中的关键帧的索引
        self.current_key_frame_index = self.key_frame_list.curselection()
        self.current_key_frame_index = self.current_key_frame_index[0]
        # 读取当前选中的关键帧
        data = self.key_frame_list.get(self.current_key_frame_index)
        data = json.loads(data)
        self.pitch = data['Body']['pitch']
        self.roll = data['Body']['roll']
        self.tran_x = data['Body']['tran_x']
        self.tran_y = data['Body']['tran_y']
        self.tran_z = data['Body']['tran_z']
        self.yaw = data['Body']['yaw']
        self.pitch_head = data['Head']['pitch']
        self.yaw_head = data['Head']['yaw']
        self.front_left_leg_x = data['FootPoint']['FrontLeftLeg']['x']
        self.front_left_leg_y = data['FootPoint']['FrontLeftLeg']['y']
        self.front_left_leg_z = data['FootPoint']['FrontLeftLeg']['z']
        self.front_right_leg_x = data['FootPoint']['FrontRightLeg']['x']
        self.front_right_leg_y = data['FootPoint']['FrontRightLeg']['y']
        self.front_right_leg_z = data['FootPoint']['FrontRightLeg']['z']
        self.back_left_leg_x = data['FootPoint']['BackLeftLeg']['x']
        self.back_left_leg_y = data['FootPoint']['BackLeftLeg']['y']
        self.back_left_leg_z = data['FootPoint']['BackLeftLeg']['z']
        self.back_right_leg_x = data['FootPoint']['BackRightLeg']['x']
        self.back_right_leg_y = data['FootPoint']['BackRightLeg']['y']
        self.back_right_leg_z = data['FootPoint']['BackRightLeg']['z']
        self.time = data['time']
        self.acc = data['acc']
        self.speed = data['speed']
        self.pitch_scale.set(self.pitch)
        self.roll_scale.set(self.roll)
        self.tran_x_scale.set(self.tran_x)
        self.tran_y_scale.set(self.tran_y)
        self.tran_z_scale.set(self.tran_z)
        self.yaw_scale.set(self.yaw)
        self.pitch_head_scale.set(self.pitch_head)
        self.yaw_head_scale.set(self.yaw_head)
        self.front_left_leg_x_scale.set(self.front_left_leg_x)
        self.front_left_leg_y_scale.set(self.front_left_leg_y)
        self.front_left_leg_z_scale.set(self.front_left_leg_z)
        self.front_right_leg_x_scale.set(self.front_right_leg_x)
        self.front_right_leg_y_scale.set(self.front_right_leg_y)
        self.front_right_leg_z_scale.set(self.front_right_leg_z)
        self.back_left_leg_x_scale.set(self.back_left_leg_x)
        self.back_left_leg_y_scale.set(self.back_left_leg_y)
        self.back_left_leg_z_scale.set(self.back_left_leg_z)
        self.back_right_leg_x_scale.set(self.back_right_leg_x)
        self.back_right_leg_y_scale.set(self.back_right_leg_y)
        self.back_right_leg_z_scale.set(self.back_right_leg_z)
        self.time_scale.set(self.time)
        self.speed_var.set(self.speed)
        self.acc_var.set(self.acc)

    # 编辑模式
    def edit_mode(self):
        self.mode = 'Edit_Mode'

    # 播放模式
    def play_mode(self):
        self.mode = 'Play_Mode'

    # 空闲模式
    def idle_mode(self):
        self.mode = 'Idle_Mode'

    # 关闭窗口
    def on_closing(self):
        if messagebox.askokcancel('Quit', 'Do you want to quit?'):
            self.ws.close()
            self.master.destroy()

    # 保存修改的关键帧
    # 读取current_key_frame_index对应的关键帧，然后将当前界面的关键帧数据替换掉原来的关键帧数据
    def save_key_frame(self):
        data = {
            "cmd": "Play_Keyframe",
            "acc": self.acc,
            "speed": self.speed,
            "time": self.time,
            "Body": {
                "pitch": self.pitch,
                "roll": self.roll,
                "tran_x": self.tran_x,
                "tran_y": self.tran_y,
                "tran_z": self.tran_z,
                "yaw": self.yaw
            },
            "FootPoint": {
                "FrontLeftLeg": {
                    "x": self.front_left_leg_x,
                    "y": self.front_left_leg_y,
                    "z": self.front_left_leg_z
                },
                "FrontRightLeg": {
                    "x": self.front_right_leg_x,
                    "y": self.front_right_leg_y,
                    "z": self.front_right_leg_z
                },
                "BackLeftLeg": {
                    "x": self.back_left_leg_x,
                    "y": self.back_left_leg_y,
                    "z": self.back_left_leg_z
                },
                "BackRightLeg": {
                    "x": self.back_right_leg_x,
                    "y": self.back_right_leg_y,
                    "z": self.back_right_leg_z
                }
            },
            "Head": {
                "pitch": self.pitch_head,
                "yaw": self.yaw_head
            }
        }
        data = json.dumps(data)
        with open('keyframe.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            lines[self.current_key_frame_index] = data + '\n'
        with open('keyframe.txt', 'w', encoding='utf-8') as f:
            f.writelines(lines)
        self.key_frame_list.delete(0, tk.END)
        with open('keyframe.txt', 'r', encoding='utf-8') as f:
            for line in f:
                self.key_frame_list.insert(tk.END, line)


# 主函数
if __name__ == '__main__':
    root = tk.Tk()
    app = KeyFrameUI(root)
    root.mainloop()

# end of file
