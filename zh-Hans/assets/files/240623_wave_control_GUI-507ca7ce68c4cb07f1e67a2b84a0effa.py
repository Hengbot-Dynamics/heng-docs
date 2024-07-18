import json
import time
import tkinter as tk

import matplotlib.pyplot as plt
import numpy as np
import websocket
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class WsClient:
    def __init__(self):
        self.ws1 = websocket.WebSocket()
        self.ws1.connect('ws://192.168.8.223:10710/getjson')  # 机器人端的websocket地址
        self.ws1.send('{"cmd":"Mode_Switch","target":"Edit_Mode"}')  # 切换到编辑模式

        self.pitch = 0
        self.roll = 0
        self.tran_x = -20
        self.tran_y = 0
        self.tran_z = 140
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
        self.last_time = 0

    def send(self):
        # 如果上次发送的时间与当前时间间隔小于10ms，则不发送
        if time.time() - self.last_time < 0.01:
            return
        self.last_time = time.time()
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
        # self.ws.send(data)
        self.ws1.send(data)
        print(data)


# 初始化全局变量
time_data = []
y_data_1 = []
y_data_2 = []
y_data_3 = []

init_time = time.time()
# 控制全局bpm 默认下每分钟60个节拍
bpm = 60
# 控制波形类型
wave_mode = 1  # 1: 正弦波, 2: 方波, 3: S型曲线
# 正半周期占整个周期的比例，0 < ratio <= 1
positive_ratio = 0.10  # 例如，0.75表示正半周期占整个周期的75%

# 振荡器1
amplitude_1 = 0.5
frequency_1 = 1
phase_1 = 0
# 振荡器2
amplitude_2 = 0.5
frequency_2 = 1
phase_2 = 0
# 振荡器3
amplitude_3 = 0.5
frequency_3 = 1
phase_3 = 0

sampling_rate = 100  # 每秒更新的帧数
WsClient = WsClient()


def parabolic_cycle(t, a, b, c):
    """
    周期性抛物线函数。

    参数:
    t -- 时间轴 a -- 抛物线开口大小 b -- y轴截距 c -- 对称轴位置，周期为2c
    返回:
    周期性抛物线函数的值
    """
    period = 2 * c
    normalized_t = t % period  # 确保t在0到period之间
    return a * (normalized_t - c) ** 2 + b


def update(frame):
    global time_data, y_data_1, y_data_2, y_data_3

    # timestep_1 = (frame / sampling_rate) * 2 * np.pi  # 计算当前时间点的x值
    # timestep = (frame / sampling_rate) * 2 * np.pi  # 计算当前时间点的x值

    timestep_1 = time.time() - init_time  # 计算当前时间点的x值
    timestep = time.time() - init_time  # 计算当前时间点的x值
    print(f"当前时间戳（秒）: {timestep}")
    # 根据GUI动态调整运行震荡周期
    time_ratio = bpm / 60
    # 计算周期和正半周期的持续时间
    period = 1 / (frequency_1 * time_ratio)
    positive_duration = period * positive_ratio
    if timestep_1 > period:
        timestep_1 = timestep_1 % period  # 运行时间对运行周期取余
    if timestep_1 < positive_duration:
        if wave_mode == 1:  # 计算方波对应的y值
            y_1 = amplitude_1
        if wave_mode == 2:  # 计算正弦波对应的y值
            y_1 = amplitude_1 * np.sin(2 * np.pi * frequency_1 * time_ratio * timestep_1 + phase_1)
        if wave_mode == 3:  # 计算三角波对应的y值
            y_1 = 0.5 * timestep_1 * amplitude_1
    else:
        y_1 = 0
    print(f"timestep_1: {timestep_1:.3f}, y_1: {y_1:.3f}")
    print(f"timestep: {timestep:.3f}, y_1: {y_1:.3f}")

    y_2 = amplitude_2 * np.sin(2 * np.pi * frequency_2 * time_ratio * timestep + phase_2)  # 计算对应的y值
    y_3 = amplitude_3 * np.sin(2 * np.pi * frequency_3 * time_ratio * timestep + phase_3)  # 计算对应的y值
    time_data.append(timestep)
    y_data_1.append(y_1)
    y_data_2.append(y_2)
    y_data_3.append(y_3)

    # 更新线图数据
    line_1.set_data(time_data, y_data_1)
    # 动态更新x轴显示范围，使其随着时间向右移动
    axs[0].set_xlim(time_data[-1] - 2 * np.pi, time_data[-1])

    # 更新线图数据
    line_2.set_data(time_data, y_data_2)
    # 动态更新x轴显示范围，使其随着时间向右移动
    axs[1].set_xlim(time_data[-1] - 2 * np.pi, time_data[-1])

    # 更新线图数据
    line_3.set_data(time_data, y_data_3)
    # 动态更新x轴显示范围，使其随着时间向右移动
    axs[2].set_xlim(time_data[-1] - 2 * np.pi, time_data[-1])

    # 限制数据点的数量
    if len(time_data) > 1000:  # 根据需要调整保留的数据点数量
        time_data = time_data[-1000:]
        y_data_1 = y_data_1[-1000:]
        y_data_2 = y_data_2[-1000:]
        y_data_3 = y_data_3[-1000:]

    # 发送数据到websocket服务器
    # pitch的范围是-1~1，需要进行映射
    WsClient.yaw = y_2 / 5
    WsClient.pitch = y_3 / 5
    # WsClient.yaw = y_3 / 5

    WsClient.yaw_head = - y_2 / 3
    WsClient.pitch_head = y_1 / 3

    # WsClient.tran_x = -y_3 * 20 - 20
    # WsClient.tran_y = -y_3 * 20
    WsClient.tran_z = y_1 * 20 + 140

    # WsClient.front_left_leg_z = y_1 * 60
    # WsClient.front_left_leg_x = y_1 * 40 + 90
    # WsClient.front_right_leg_z = -y_1 * 40

    # WsClient.front_left_leg_y = -y_3 * 40 + 50
    # WsClient.front_right_leg_y = y_3 * 40 - 50
    WsClient.send()

    return line_1, line_2, line_3


# 更新滑块参数的回调函数
def update_sliders(event=None):
    global bpm, wave_mode, positive_ratio
    bpm = bpm_scale.get()
    wave_mode = wave_mode_scale.get()
    positive_ratio = positive_ratio_scale.get()

    global amplitude_1, frequency_1, phase_1
    amplitude_1 = amp_scale_1.get()
    frequency_1 = freq_scale_1.get()
    # phase_1 = phase_scale_1.get()

    global amplitude_2, frequency_2, phase_2
    amplitude_2 = amp_scale_2.get()
    frequency_2 = freq_scale_2.get()
    # phase_2 = phase_scale_2.get()

    global amplitude_3, frequency_3, phase_3
    amplitude_3 = amp_scale_3.get()
    frequency_3 = freq_scale_3.get()
    # phase_3 = phase_scale_3.get()


# 创建主窗口
root = tk.Tk()
root.title("Sine Wave Animation")

# 创建画布
fig, axs = plt.subplots(3, sharex=True)
fig.suptitle('Multiple Line Chart')

axs[0].set_ylim(-10, 10)  # 设置y轴范围
axs[0].set_title('Line 1')
line_1, = axs[0].plot(time_data, y_data_1, 'b-')  # 初始空数据

axs[1].set_ylim(-10, 10)  # 设置y轴范围
axs[1].set_title('Line 2')
line_2, = axs[1].plot(time_data, y_data_2, 'b-')  # 初始空数据

axs[2].set_ylim(-10, 10)  # 设置y轴范围
axs[2].set_title('Line 3')
line_3, = axs[2].plot(time_data, y_data_3, 'b-')  # 初始空数据

# 创建一个画布来放置matplotlib图表
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

global_length = 600
# scl = Scale(self.master,
#             orient=HORIZONTAL,
#             length=200, width=20,
#             from_=1.0, to=5.0,
#             label='请拖动滑块',
#             tickinterval=1, resolution=0.05,
#             variable=scale_value)

# 创建滑块来控制bpm
bpm_scale = tk.Scale(root, label="bpm_scale", length=global_length, width=20, resolution=1, from_=50, to=150,
                     orient='horizontal',
                     command=lambda x: update_sliders())
bpm_scale.set(bpm)
bpm_scale.pack()

# 创建滑块来控制波形类型
wave_mode_scale = tk.Scale(root, label="wave_mode_scale", length=global_length, width=20, resolution=1, from_=1, to=3,
                           orient='horizontal', command=lambda x: update_sliders())
wave_mode_scale.set(wave_mode)
wave_mode_scale.pack()

# 创建滑块来控制波形占空比
positive_ratio_scale = tk.Scale(root, label="positive_ratio_scale", length=global_length, width=20, resolution=0.1,
                                from_=0, to=1,
                                orient='horizontal', command=lambda x: update_sliders())
positive_ratio_scale.set(positive_ratio)
positive_ratio_scale.pack()

########################################################################################################################
# 创建滑块来控制幅度、频率和相位
amp_scale_1 = tk.Scale(root, label="amp_scale_1", length=global_length, width=20, resolution=0.1, from_=0.0, to=1.5,
                       orient='horizontal', command=lambda x: update_sliders())
amp_scale_1.set(amplitude_1)
amp_scale_1.pack()

freq_scale_1 = tk.Scale(root, label="freq_scale_1", length=global_length, width=20, resolution=0.25, from_=0.25, to=4.0,
                        orient='horizontal', command=lambda x: update_sliders())
freq_scale_1.set(frequency_1)
freq_scale_1.pack()

# phase_scale_1 = tk.Scale(root, label="phase_scale_1", length=global_length, resolution=0.1, from_=-2 * np.pi,
#                          to=2 * np.pi, orient='horizontal', command=lambda x: update_sliders())
# phase_scale_1.set(phase_1)
# phase_scale_1.pack()

# 创建滑块来控制幅度、频率和相位
amp_scale_2 = tk.Scale(root, label="amp_scale_2", length=global_length, width=20, resolution=0.1, from_=0.0, to=1.5,
                       orient='horizontal', command=lambda x: update_sliders())
amp_scale_2.set(amplitude_2)
amp_scale_2.pack()

freq_scale_2 = tk.Scale(root, label="freq_scale_2", length=global_length, width=20, resolution=0.25, from_=0.25, to=4.0,
                        orient='horizontal', command=lambda x: update_sliders())
freq_scale_2.set(frequency_2)
freq_scale_2.pack()

# phase_scale_2 = tk.Scale(root, label="phase_scale_2", length=global_length, resolution=0.1, from_=-2 * np.pi,
#                          to=2 * np.pi, orient='horizontal', command=lambda x: update_sliders())
# phase_scale_2.set(phase_2)
# phase_scale_2.pack()

# 创建滑块来控制幅度、频率和相位
amp_scale_3 = tk.Scale(root, label="amp_scale_3", length=global_length, width=20, resolution=0.1, from_=0.0, to=1.5,
                       orient='horizontal', command=lambda x: update_sliders())
amp_scale_3.set(amplitude_3)
amp_scale_3.pack()

freq_scale_3 = tk.Scale(root, label="freq_scale_3", length=global_length, width=20, resolution=0.25, from_=0.25, to=4.0,
                        orient='horizontal', command=lambda x: update_sliders())
freq_scale_3.set(frequency_3)
freq_scale_3.pack()

# phase_scale_3 = tk.Scale(root, label="phase_scale_3", length=global_length, resolution=0.1, from_=-2 * np.pi,
#                          to=2 * np.pi, orient='horizontal', command=lambda x: update_sliders())
# phase_scale_3.set(phase_3)
# phase_scale_3.pack()

# 创建动画
ani = FuncAnimation(fig, update, frames=np.arange(0, 10000, 1),
                    init_func=None, blit=True, interval=1000 / sampling_rate)

# 启动GUI主循环
root.mainloop()

# Path: cos_control.py
