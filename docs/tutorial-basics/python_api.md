---
sidebar_position: 5
---

# 探索系列（二）：Python API

## 一、前言

>上文我们熟悉了遥控的基础用法以及进阶用法，疑问来了：什么原理创造了这些效果呢？  
而今天，我们会在这篇文档会找到想要的答案！

<div className="indent-first-line">
**本篇文档介绍了如何使用 Python sdk 控制哮天的运动状态。您可以按照我们提供的接口和例程，尝试用 Python 来学习机器人控制，完成哮天的二次开发。在阅读本文档前，请先阅读[开箱系列：基础配置使用](./quick_start_guide.md)，对哮天有一定了解。**
</div>

![sparky](./img/app/sparky.jpg)

## 二、准备工作

在正式进入二次开发的学习前，我们先来完成一些准备工作，让后续学习进程更加顺畅。

### 2.1 基础知识

- 有 Python 语言编程基础，了解基本语法，如面向对象、交互解释等概念。
- 熟悉哮天的基础使用等操作，能够使用 Sparky's App 控制哮天。

### 2.2 硬件

- 硬件：一只哮天。
- 环境：整洁的桌面或平整的工作地面。

### 2.3 软件

- 哮天：与电脑连接同一局域网，从屏幕上获取 IP 地址。
- PC端：已安装 Python 环境（包括 pip）git，可以通过以下两种方式获取开发 SDK。

```bash
pip install hengbot-api

git clone https://github.com/Hengbot-Dynamics/hengbot-api.git
```

## 三、基础使用

:::danger[Take care]
以下代码内含相关哮天 IP 地址配置的，请先更改为正确哮天的本机 IP 再进行使用。  
此为一个示例：`IP = '192.168.8.139'` 
:::

### 3.1 获取状态信息

发送指令获取哮天电池信息，硬件错误状态及网络信息

```python
from hengbot import sparky
# set IP
IP = '192.168.8.139'
def test_get_status(ip):
    # connect through ip
    with sparky.robot_control(ip) as robot:
        if robot.isconnected:
            # get information
            data = robot.get_status()
            print(data)
        else:
            print("wait connecting...")
test_get_status(IP)
```

信息会以 `json` 的形式返回，经整理后如下所示:

```json
{
    "Battery_Information": {
        "Battery_Capacity": "2340",
        "Battery_Life": "87",
        "Battery_Percentage": "93.6",
        "Battery_Status_Indicator": "Discharging",
        "Charging_Time": "65535",
        "Current": "-1.62",
        "Instantaneous_Power": "-11.664",
        "Temperature": "36",
        "Voltage": "7.2"
    },
    "Hardware_Error_Status": {
        "AIA": {
            "BackLeftLeg": "Not_in_place",
            "BackRightLeg": "Overheating",
            "FrontLeftLeg": "Overload",
            "FrontRightLeg": "NONE"
        },
        "Robot": {
            "Global": "Low_Power"
        }
    },
    "Network_Information": {
        "Client_IP_Address": "192.168.8.211",
        "Device_IP_Address": "192.168.8.237",
        "SSID": "test"
    },
    "feedback": "Get_Status"
}
```

### 3.2 遥控模式

先使用以下代码进入遥控模式并控制哮天进行转圈，这里运行代码后哮天会开始转圈，请放置在空阔平整的地面或台面上。

```python
from hengbot import sparky
# set IP
IP = '192.168.8.139'
def test_circles(ip, timeout = 10):
    import time
    # connect through ip
    with sparky.robot_control(ip) as robot:
        # switch to control mode and return to control mode operation object
        ctrl = robot.switch_mode(sparky.MODE_CTRL)
        # wait for readiness
        time.sleep(0.5)
        # make it turn in circles
        ctrl.movex = 1
        ctrl.movew = 0.5
        ctrl.headyaw = 1
        ctrl.speed = ctrl.SPEED_NORMAL
        # synchronized to Sparky
        ctrl.sync()
        time.sleep(timeout)
test_circles(IP)
```

### 3.3 编辑模式

进入编辑模式后，我们来编写关键帧实现一系列动作。

#### 3.3.1 身体摇摆

```python
from hengbot import sparky
# set IP
IP = '192.168.8.139'
def test_swing(ip):
    import time
    # connect through ip
    with sparky.robot_control(ip) as robot:
        # switch to edit mode and return to edit mode operation object
        edit = robot.switch_mode(sparky.MODE_EDIT)
        for i in range(5):
            edit.yaw = 0.3
            edit.headyaw = 0.5
            # Waiting to move
            time.sleep(1)
            edit.yaw = -0.3
            edit.headyaw = -0.5
            time.sleep(1)
test_swing(IP)
```

#### 3.3.2 蹲下起立

```python
from hengbot import sparky
# set IP
IP = '192.168.8.139'
def test_crouch(ip, timeout = 5):
    import time
    # connect through ip
    with sparky.robot_control(ip) as robot:
        # switch to edit mode and return to edit mode operation object
        edit = robot.switch_mode(sparky.MODE_EDIT)
        # set speed
        edit.acc = edit.SPEED_SLOWEST
        edit.speed = edit.SPEED_SLOWEST
        # set the position of the legs
        edit.back_left_leg_z = 50
        edit.back_right_leg_z = 50
        time.sleep(timeout)
test_crouch(IP)
```

#### 3.3.3 点头摇头

```python
from hengbot import sparky
# set IP
IP = '192.168.8.139'
def test_shake_head(ip, timeout = 3):
    import time
    # connect through ip
    with sparky.robot_control(ip) as robot:
        # switch to edit mode and return to edit mode operation object
        edit = robot.switch_mode(sparky.MODE_EDIT)
        # set speed
        edit.acc = edit.SPEED_SLOWEST
        edit.speed = edit.SPEED_SLOWEST
        # nodded
        for i in range(3):
            edit.headpitch = 0.5
            time.sleep(0.5)
            edit.headpitch = -0.5
            time.sleep(0.5)
        edit.headpitch = 0
        # Shake head
        for i in range(3):
            edit.headyaw = 0.5
            time.sleep(0.5)
            edit.headyaw = -0.5
            time.sleep(0.5)
        edit.headyaw = 0
        time.sleep(timeout)
test_shake_head(IP)
```

### 3.4 示教模式

体验完上文的编辑模式后，我们来到示教模式来录制动作并播放动作。

```python
from hengbot import sparky
# set IP
IP = '192.168.8.139'
def test_play(ip, timeout = 10):
    import time
    # connect through ip
    with sparky.robot_control(ip) as robot:
        # switch to teach mode and return to edit teach operation object
        teach = robot.switch_mode(sparky.MODE_TEACH)
        print('start record')
        teach.start_record()
        time.sleep(timeout)
        print('stop record')
        teach.stop_record()
        # time.sleep(timeout)
        print('start play')
        teach.start_play()
        time.sleep(timeout)
        print('stop play')
test_play(IP)
```

## 四、核心 API 手册

### 4.1 模块结构

模块共有 5 种操作对象，分别是 `robot_control`，`teach_mode`，`ctrl_mode`，`edit_mode`，`wave_mode`。

创建 `robot_control` 连接上哮天，使用 `robot_control.switch_mode` 获取对应模式操作对象。

### 4.2 导入模块

```python
from hengbot import sparky
```

### 4.3 robot_control

#### 4.3.1 对象创建

```python
IP = '192.168.8.237'
with sparky.robot_control(IP) as robot_control:
```

#### 4.3.2 对象属性

- robot_control.battery_percentage 返回电池电量
- robot_control.isconnected 返回当前是否连接

#### 4.3.3 函数

- Callback
  - **robot_control.add_message_callback  添加消息回调函数**


```python
def msgCallback(robot_control, message):
    print(message)
robot_control.add_message_callback(msgCallback)
```

  - **robot_control.del_message_callback 删除消息回调函数**

```pythoon
robot_control.del_message_callback(msgCallback)
```

  - **robot_control.add_error_callback 添加错误回调函数**

```python
def errCallback(robot_control, err_msg):
    print('err')
robot_control.add_error_callback(errCallback)
```

  - **robot_control.del_error_callback 删除错误回调函数**

```python
robot_control.del_error_callback(errCallback)
```

  - **robot_control.add_connected_callback 添加连接回调函数**

```python
def openCallback(robot_control):
    print('connected')
robot_control.add_connected_callback(openCallback)
```

  - **robot_control.del_connected_callback 删除连接回调函数**

```python
robot_control.del_connected_callback(openCallback)
```

  - **robot_control.add_close_callback 添加关闭回调函数**

```python
def closeCallback(robot_control, close_msg):
    print('close')
robot_control.add_close_callback(closeCallback)
```

  - **robot_control.del_close_callback 删除错误回调函数**

```python
robot_control.del_close_callback(closeCallback)
```

| 函数 | 属性 | 备注|
|----|----|----|
| robot_control.switch_mode(target) | 切换哮天工作模式 | target:可选 `sparky.MODE_CTRL`、`sparky.MODE_TEACH`、`sparky.MODE_EDIT`、`sparky.MODE_WAVE`  返回对应模式操作对象|
| robot_control.reset() | 恢复哮天姿态 | |
| robot_control.get_status() | 以 Json 的形式返回哮天状态信息，整理后如下所示 |  |

```json
{
    "Battery_Information": {
        "Battery_Capacity": "2340",
        "Battery_Life": "87",
        "Battery_Percentage": "93.6",
        "Battery_Status_Indicator": "Discharging",
        "Charging_Time": "65535",
        "Current": "-1.62",
        "Instantaneous_Power": "-11.664",
        "Temperature": "36",
        "Voltage": "7.2"
    },
    "Hardware_Error_Status": {
        "AIA": {
            "BackLeftLeg": "Not_in_place",
            "BackRightLeg": "Overheating",
            "FrontLeftLeg": "Overload",
            "FrontRightLeg": "NONE"
        },
        "Robot": {
            "Global": "Low_Power"
        }
    },
    "Network_Information": {
        "Client_IP_Address": "192.168.8.211",
        "Device_IP_Addres": "192.168.8.237",
        "SSID": "test"
    },
    "feedback": "Get_Status"
}
```

### 4.4 teach_mode

#### 4.4.1 对象创建

```python
teach_mode = robot_control.switch_mode(sparky.MODE_TEACH)
```

#### 4.4.2 函数

| 函数 | 属性 | 备注 |
|----|----|----|
| `teach_mode.start_record(save_path=None):` | 开始录制  | `save_path`:录制数据保存位置，默认不保存. |
| `teach_mode.stop_record()` | 停止录制 | |
|`teach_mode.start_play(play_path=None)` | 开始播放 | play_path:获取数据位置，默认使用不保存录制的数据。|
| `teach_mode.get_parameter()` | 获取电机扭力输出配置，需要在 `robot_control` 中添加消息回调接收，以 Json 的形式返回整理后如下所示 |

```json
{
    "feedback": "Get_Parameter",
    "list": [{
        "type": "AIA_HEAD",
        "value": "Limit"
    }, {
        "type": "AIA_FrontLeft",
        "value": "Limit"
    }, {
        "type": "AIA_FrontRight",
        "value": "Limit"
    }, {
        "type": "AIA_BackLeft",
        "value": "Limit"
    }, {
        "type": "AIA_BackRight",
        "value": "Limit"
    }],
    "parameter": "Output_Torque"
}
```

- teach_mode.set_parameter(type, value)

设置电机扭力输出

| type 可选 | value 可选 |
|----|----|
|`sparky.PARM_TYPE_HEAD`、`sparky.PARM_TYPE_FRONTLEFT`、`sparky.PARM_TYPE_FRONTRIGHT`、`sparky.PARM_TYPE_BACKLEFT`、`sparky.PARM_TYPE_BACKRIGHT`、`sparky.PARM_TYPE_ALL`|`sparky.PARM_VALUE_ENABLE`、`sparky.PARM_VALUE_DISABLE`、`sparky.PARM_VALUE_LIMIT`、`sparky.PARM_VALUE_UNLIMIT`|

### 4.5 ctrl_mode

#### 4.5.1 对象创建

```python
ctrl_mode = robot_control.switch_mode(sparky.MODE_CTRL)
```

#### 4.5.2 对象属性

| 对象 | 属性 |
|-----|----|
| ctrl_mode.movex | 设置 x 轴速度，范围为 [1,-1] 最大前进、后退速率为 0.28m/s。|
| ctrl_mode.movey | 设置 y 轴速度，范围为 [1,-1] 最大前进、后退速率为 0.28m/s。|
| ctrl_mode.movew | 设置 z 轴逆时针运动的角速度，范围为 [1,-1] 最大旋转速度为 2rad/s。|
| ctrl_mode.headpitch | 范围为 [1,-1] rad |
| ctrl_mode.headyaw | 范围为 [1,-1] rad |
| ctrl_mode.pitch | 范围为 [1,-1] rad |
| ctrl_mode.yaw | 范围为 [1,-1] rad |
| ctrl_mode.roll | 范围为 [1,-1] rad |
| ctrl_mode.tranx | 范围为 [1,-1] 活动范围为前后20mm |
| ctrl_mode.trany | 范围为 [1,-1] 活动范围为左右20mm |
| ctrl_mode.tranz | 范围为 [1,-1] 活动范围为上下30mm |
| ctrl_mode.speed | 可选 `ctrl_mode.SPEED_FAST`、`ctrl_mode.SPEED_NORMAL` |

#### 4.5.3 函数
  
| 函数 | 功能 |
|----|----|
| ctrl_mode.sync() | 将设置的信息同步到哮天 |

### 4.6 edit_mode

#### 4.6.1 对象创建

```python
edit_mode= robot_control.switch_mode(sparky.MODE_EDIT)
```

#### 4.6.2 对象属性

| 对象| 含义属性 |
|----|----| 
| edit_mode.pitch | 范围为 [1,-1] rad |
| edit_mode.roll | 范围为 [1,-1] rad |
| edit_mode.yaw | 范围为 [1,-1] rad |
| edit_mode.headpitch | 范围为 [1,-1] rad |
| edit_mode.headyaw | 范围为 [1,-1] rad |
| edit_mode.tranx | 身体 x 轴方向位移，范围 [-50,50] |
| edit_mode.trany | 身体 y 轴方向位移，范围 [-50,50] |
| edit_mode.tranz | 身体 z 轴方向位移，范围 [0,141] |
| edit_mode.front_left_leg_x | 前左脚的 x ，范围 [-25,175] |
| edit_mode.front_left_leg_y | 前左脚的 y ，范围 [-45,155] |
| edit_mode.front_left_leg_z | 前左脚的 z ，范围 [-100,100] |
| edit_mode.front_right_leg_x | 前右脚的 x ，范围 [-25,175] |
| edit_mode.front_right_leg_y | 前右脚的 y ，范围 [-155,45] |
| edit_mode.front_right_leg_z | 前右脚的 z ，范围 [-100,100] |
| edit_mode.back_left_leg_x | 后左脚的 x ，范围 [-175,25] |
| edit_mode.back_left_leg_y | 后左脚的 y ，范围 [-45,155] |
| edit_mode.back_left_leg_z | 后左脚的 z ，范围 [-100,100] |
| edit_mode.back_right_leg_x | 后右脚的 x ，范围 [-175,25] |
| edit_mode.back_right_leg_y | 后右脚的 y ，范围 [-155,45] |
| edit_mode.back_right_leg_z | 后右脚的 z ，范围 [-100,100] |
| edit_mode.acc | 可选 `edit_mode.SPEED_FASTEST`、`edit_mode.SPEED_FAST`、`edit_mode.SPEED_SLOW`、`edit_mode.SPEED_SLOWEST` |
| speed | 可选 `edit_mode.SPEED_FASTEST`、`edit_mode.SPEED_FAST`、`edit_mode.SPEED_SLOW`、`edit_mode.SPEED_SLOWEST` |

#### 4.6.3 函数

- **edit_mode.get_parameter()**
  
获取电机扭力输出配置，需要在 robot_control 中添加消息回调接收，以 `Json` 的形式返回整理后如下所示  

```json
{
    "feedback": "Get_Parameter",
    "list": [{
        "type": "AIA_HEAD",
        "value": "Limit"
    }, {
        "type": "AIA_FrontLeft",
        "value": "Limit"
    }, {
        "type": "AIA_FrontRight",
        "value": "Limit"
    }, {
        "type": "AIA_BackLeft",
        "value": "Limit"
    }, {
        "type": "AIA_BackRight",
        "value": "Limit"
    }],
    "parameter": "Output_Torque"
}
```
-  **`edit_mode.set_parameter(type, value)` 置电机扭力输出**

| type 可选 | value 可选 |
|----|----|
|`sparky.PARM_TYPE_HEAD`、`sparky.PARM_TYPE_FRONTLEFT`、`sparky.PARM_TYPE_FRONTRIGHT`、`sparky.PARM_TYPE_BACKLEFT`、`sparky.PARM_TYPE_BACKRIGHT`、`sparky.PARM_TYPE_ALL`|`sparky.PARM_VALUE_ENABLE`、`sparky.PARM_VALUE_DISABLE`、`sparky.PARM_VALUE_LIMIT`、`sparky.PARM_VALUE_UNLIMIT`|

| 函数 | 作用 | 备注 |
|----|----|----|
| edit_mode.save(path='keyframe.txt', index=None) | 保存当前设置关键帧到文件 | `path:文件地址`、`index:第几行，填写为覆盖指定行，默认向后加入`。|
| edit_mode.read(path='keyframe.txt', index=0) | 读取指定行到设置 |  `path:文件地址`、`index:第几行，默认首行` |

### 4.7 wave_mode

#### 4.7.1 对象创建

```python
wave_mode= robot_control.switch_mode(sparky.MODE_WAVE)
```

#### 4.7.2 对象属性

| 对象 | 属性 | 备注 |
|-----|-----|-----|
| wave_mode.bpm | 控制全局bpm | 默认下每分钟60个节拍 |
| wave_mode.wave_mode | 控制波形类型 | 1: 正弦波、2: 方波、3: S型曲线 |
| wave_mode.positive_ratio | 正半周期占整个周期的比例 `0 < ratio <= 1` ||
| wave_mode.amplitude_1 | 振幅 | |
| wave_mode.frequency_1 | 占空比 | |
| wave_mode.amplitude_2 |||
| wave_mode.frequency_2 |||
| wave_mode.amplitude_3 |||
| wave_mode.frequency_3 |||

## 五、错误和异常处理

### 5.1 断开连接

如果出现哮天断开连接的现象，此时错误的回调函数会收到信息，哮天会自动进入恢复连接操作。  
但如果出现长时间连接不上，请检查哮天本身的网络状态是否正常？是否显示 IP 地址。

## 六、版本信息

| 版本 | 功能 |
|------|------|
| 0.0.1 | 实现基本功能 |