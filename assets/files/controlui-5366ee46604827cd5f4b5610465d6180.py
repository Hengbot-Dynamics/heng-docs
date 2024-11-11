import tkinter as tk
from tkinter import filedialog, simpledialog
import json
import websocket
import cv2
from PIL import Image, ImageTk
import numpy as np
import urllib.request
import threading


class VideoStream:
    def __init__(self, url):
        self.stream = urllib.request.urlopen(url)
        self.running = False
        self.frame = None  # Initialize self.frame
        self.bytes = b''
        self.lock = threading.Lock()  # Create a thread lock

    def start(self):
        self.running = True
        threading.Thread(target=self.update_frame, args=()).start()

    def update_frame(self):
        while self.running:
            self.bytes += self.stream.read(1024)
            a = self.bytes.find(b'\xff\xd8')
            b = self.bytes.find(b'\xff\xd9')
            if a != -1 and b != -1:
                jpg = self.bytes[a:b+2]
                self.bytes = self.bytes[b+2:]
                with self.lock:  # Acquire the lock before updating self.frame
                    self.frame = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                    # 对图片进行左右镜像
                    self.frame = cv2.flip(self.frame, 1)

    def get_frame(self):
        with self.lock:  # Acquire the lock before accessing self.frame
            if self.frame is not None:
                return self.frame
            else:
                return np.zeros((600, 800, 3), dtype=np.uint8)  # Return an empty frame

    def stop(self):
        self.running = False

class App:
    def __init__(self, window, video_source):
        self.photo = None
        self.window = window
        self.window.title("Video Stream from HTTP Server")
        self.video_source = video_source
        self.vid = VideoStream(self.video_source)
        self.vid.start()
        self.canvas = tk.Canvas(window, width = 800, height = 600)
        self.canvas.pack()
        self.update()

    def update(self):
        frame = self.vid.get_frame()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.photo = ImageTk.PhotoImage(image = Image.fromarray(frame))
        self.canvas.create_image(0, 0, image = self.photo, anchor = tk.NW)
        self.window.after(15, self.update)

    def __del__(self):
        self.vid.stop()

class RemoteControl:
    def __init__(self, master):
        self.ws = websocket.WebSocket()
        ip_address = simpledialog.askstring("Input", "Enter the IP address:",
                                            parent=master)
        if ip_address:
            self.ws.connect(f'ws://{ip_address}:10710/getjson')
            self.ws.send('{"cmd":"Mode_Switch","target":"Remote_Control_Mode"}')
        else:
            print("No IP address entered. Cannot connect to websocket.")

        self.movex = 0
        self.movey = 0
        self.movew = 0
        self.moveh = 0
        self.tranx = 0
        self.trany = 0
        self.tranz = 0
        self.roll = 0
        self.pitch = 0
        self.yaw = 0
        self.headpitch = -0.5
        self.headyaw = 0
        self.speed = 'fast'

        self.t = threading.Thread(target=self.send)
        self.t.start()

        self.master = master
        self.master.bind('<KeyPress>', self.on_key_press)
        self.master.bind('<KeyRelease>', self.on_key_release)
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Create an App instance to start the video stream
        self.app = App(master, 'http://' + ip_address + ':8080')

    def on_key_press(self, event):
        if event.char == 'w':
            self.movex = 1.0
        elif event.char == 's':
            self.movex = -0.8
        if event.char == 'a':
            self.movey = 1.0
        elif event.char == 'd':
            self.movey = -1.0
        if event.char == 'q':
            self.movew = -1.0
        elif event.char == 'e':
            self.movew = 1.0
        if event.keysym == 'Up':
            self.pitch = 0.2
        if event.keysym == 'Down':
            self.tranz = -1.0
        # 按下键盘左键，机器人左旋，按下键盘右键，机器人右旋
        if event.keysym == 'Left':
            self.yaw = 0.3
        elif event.keysym == 'Right':
            self.yaw = -0.3

        self.send()

    def on_key_release(self, event):
        if event.char in 'ws':
            self.movex = 0
        if event.char in 'ad':
            self.movey = 0
        if event.char in 'qe':
            self.movew = 0
        if event.keysym in ('Up'):
            self.pitch = 0
        if event.keysym in ('Down'):
            self.tranz = 0
        if event.keysym in ('Left', 'Right'):
            self.yaw = 0
        self.send()

    def send(self):
        data = {
            "cmd": "Control_Move",
            "movex": self.movex,
            "movey": self.movey,
            "movew": self.movew,
            "moveh": self.moveh,
            "tranx": self.tranx,
            "trany": self.trany,
            "tranz": self.tranz,
            "roll": self.roll,
            "pitch": self.pitch,
            "yaw": self.yaw,
            "headpitch": self.headpitch,
            "headyaw": self.headyaw,
            "speed": self.speed
        }
        print(data)
        self.ws.send(json.dumps(data))

    def on_closing(self):
        self.ws.close()
        self.master.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    remote_control = RemoteControl(root)
    root.mainloop()

# 通过键盘控制机器人的运动，按下W键机器人前进，按下S键机器人后退，按下A键机器人左移，按下D键机器人右移
# 按下Q键机器人逆时针旋转，按下E键机器人顺时针旋转
# 按下空格键机器人停止运动
# 按下ESC键退出程序
# 通过WSAD控制机器人的运动，W对应前进，S对应后退，A对应左移，D对应右移，松开键盘停止设置为0
# ws映射到机器人的运动的movex上，W对应1.0，S对应-1.0
# ad映射到机器人的运动的movey上，A对应1.0，D对应-1.0
# qe映射到机器人的运动的movew上，Q对应1.0，E对应-1.0
# 通过键盘控制机器人的运动，按下W键机器人前进，按下S键机器人后退，按下A键机器人左移，按下D键机器人右移
# 按下Q键机器人逆时针旋转，按下E键机器人顺时针旋转
# 按下空格键机器人停止运动
# 按下ESC键退出程序