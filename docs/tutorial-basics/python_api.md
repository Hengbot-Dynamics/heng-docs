---
sidebar_position: 5
---

# Mid-level (II): Python API

## I.Preface

> In the previous sections, we familiarized ourselves with the basic and advanced usage of remote control. So the question is: What principle creates these effects?  
> From this document, we will find the answer we are looking for!

This section introduces how to use Python SDK to control the movement status of your Sirius. You can try using Python to learn robot control and complete the secondary development of your Sirius by following the interfaces and instances we provide. Before reading this document, please learn the section "Unboxing: Entry-level configuration and usage" for a basic understanding of Sirius.

![Sirius](./img/app/sirius.jpg)

## II.Preparation Work

Before entering the study of secondary development, let's finish some preparatory work to make the follow-up learning process easier.

### 2.1 Basic Knowledge  

- Possess a foundation in Python programming language and understand basic syntax concepts such as object-oriented programming and interactive interpretation.  
- Familiar with the basic operations of Sirius and able to use the App to control Sirius.  

### 2.2 Hardware​

- Hardware: a Sirius.  
- Environment: a clean desktop or flat work surface.  
  
### 2.3 Software  

- Sirius: Connect to the same LAN as the computer and obtain the IP address from the screen.  
- PC: The Python environment (including Git repository with pip) has been installed, and the development SDK can be obtained through the following two methods.

```bash
pip install hengbot-api

git clone https://github.com/Hengbot-Dynamics/hengbot-api.git
```

## III.Basic Usage

:::danger[TAKE CARE]
The following code contains relevant configuration of Sirius's IP address. Please change it to the correct Sirius local IP address before using it.
This is an example:`IP = '192.168.8.139'` 
:::

### 3.1 Get Status Information  

Send commands to obtain information on the battery, hardware error status, and network information of Sirius.

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

The information will be returned in the form of json, which is sorted as follows:

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

### 3.2 Remote Control Mode  

First, use the following code to enter the remote control mode and control Sirius to make a circle. After running the code here, Sirius will start to make a circle. Please place it on an open and flat ground or table.

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
        # synchronized to Sirius
        ctrl.sync()
        time.sleep(timeout)
test_circles(IP)
```

### 3.3 Edit Mode  

After entering editing mode, we will write keyframes to implement a series of actions.

#### 3.3.1 Body Swing

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

#### 3.3.2 Squat Down and Stand Up

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

#### 3.3.3 Nodding and Shaking Head

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

#### 3.3.4 Play Keyframes

```python
from hengbot import sparky
# set IP
IP = '192.168.8.154'
def test_play_frame(ip):
    import time
    # connect through ip
    with sparky.robot_control(ip) as robot:
        # switch to edit mode and return to edit mode operation object
        edit = robot.switch_mode(sparky.MODE_EDIT)
        # play action frame
        edit.play('./20240808_Shaking_your_head.txt')
        input("回车退出")
test_play_frame(IP)
```

### 3.4 Teaching Demonstration Mode

After experiencing the editing mode above, we came to the teaching demonstration mode to record and play the action.

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

## IV.Core API Manual

### 4.1 Module Structure  

There are 5 types of operation objects in the module, namely robot_comtrol, teach_mode，ctrl_mode，edit_mode，wave_mode。  

Create a robot_comtrol connection to Sirius and use robot_comtrol.switch_mode to obtain the corresponding mode operation object.  

### 4.2 Import Module ​

```python
from hengbot import sparky
```

### 4.3 robot_control

#### 4.3.1 Creating Objects

```python
IP = '192.168.8.237'
with sparky.robot_control(IP) as robot_control:
```

#### 4.3.2 Object Properties

- robot_control.battery_percentage（Return battery level）
- robot_control.isconnected （Return whether it is currently connected）

#### 4.3.3 Function

- Callback
  - **robot_control.add_message_callback（oAdd a message callback function）**

```python
def msgCallback(robot_control, message):
    print(message)
robot_control.add_message_callback(msgCallback)
```

  - **robot_control.del_message_callback (Delete a message callback function)**

```pythoon
robot_control.del_message_callback(msgCallback)
```

  - **robot_control.add_error_callback (Add an error callback function)**

```python
def errCallback(robot_control, err_msg):
    print('err')
robot_control.add_error_callback(errCallback)
```

  - **robot_control.del_error_callback (Delete an error callback function)**

```python
robot_control.del_error_callback(errCallback)
```

  - **robot_control.add_connected_callback (Add a connection callback function)**

```python
def openCallback(robot_control):
    print('connected')
robot_control.add_connected_callback(openCallback)
```

  - **robot_control.del_connected_callback (Delete a connection callback function)**

```python
robot_control.del_connected_callback(openCallback)
```

  - **robot_control.add_close_callback (Add a close callback function)**

```python
def closeCallback(robot_control, close_msg):
    print('close')
robot_control.add_close_callback(closeCallback)
```

  - **robot_control.del_close_callback (Delete a close callback function)**

```python
robot_control.del_close_callback(closeCallback)
```

| Function | Attribute | Remarks |
|----------|-----------|---------|
| robot_control.switch_mode(target, end_reset=True) | Switch Sirius working mode | target:`sparky.MODE_CTRL`、`sparky.MODE_TEACH`、`sparky.MODE_EDIT`、`sparky.MODE_WAVE` can be selected to return the corresponding mode operation object. `end_reset`:Whether to restore sparky mode after the program ends. Only valid in `sparky.MODE_TEACH` and `sparky.MODE_EDIT`. |
| robot_control.reset() | Restore Sirius's posture | |
| robot_control.get_status() | The information will be returned in the form of json, which is sorted as follows |  |

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

#### 4.4.1 Creating Objects

```python
teach_mode = robot_control.switch_mode(sparky.MODE_TEACH)
```

#### 4.4.2 Function

| Function | Attribute | Remarks |
|----|----|----|
| `teach_mode.start_record(save_path=None):` | Start recording  | `save_path`:The storage location for recorded data, which is not saved by default |
| `teach_mode.stop_record()` | Stop recording | |
|`teach_mode.start_play(play_path=None)` | Start playing | play_path:Retrieve data location, default to using recorded data which is not saved.|
| `teach_mode.get_parameter()` | To obtain the torque output configuration of the motor, it is necessary to add a message callback reception in `robot_comtrol` and return it in JSON format as shown below |

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

Set motor torque output

| type(optional) | value(optional) |
|----|----|
|`sparky.PARM_TYPE_HEAD`、`sparky.PARM_TYPE_FRONTLEFT`、`sparky.PARM_TYPE_FRONTRIGHT`、`sparky.PARM_TYPE_BACKLEFT`、`sparky.PARM_TYPE_BACKRIGHT`、`sparky.PARM_TYPE_ALL`|`sparky.PARM_VALUE_ENABLE`、`sparky.PARM_VALUE_DISABLE`、`sparky.PARM_VALUE_LIMIT`、`sparky.PARM_VALUE_UNLIMIT`|

### 4.5 ctrl_mode

#### 4.5.1 Creating Objects

```python
ctrl_mode = robot_control.switch_mode(sparky.MODE_CTRL)
```

#### 4.5.2 Object Properties

| Object | Properties |
|-----|----|
| ctrl_mode.movex | Set the x-axis speed within the range of [1, -1], with a maximum forward and backward speed of 0.28m/s. |
| ctrl_mode.movey | Set the y-axis speed within the range of [1, -1], with a maximum forward and backward speed of 0.28m/s. |
| ctrl_mode.movew | Set the angular velocity of counterclockwise movement on the z-axis within the range of [1, -1], with a maximum rotation speed of 2rad/s.|
| ctrl_mode.headpitch | Range of [1,-1] rad |
| ctrl_mode.headyaw | Range of [1,-1] rad |
| ctrl_mode.pitch | Range of [1,-1] rad|
| ctrl_mode.yaw | Range of [1,-1] rad |
| ctrl_mode.roll | Range of [1,-1] rad|
| ctrl_mode.tranx | Range of [1,-1] The range of motion is 20mm forward and backward |
| ctrl_mode.trany | Range of [1,-1] The range of motion is 20mm left and right|
| ctrl_mode.tranz | Range of [1,-1] The range of motion is 30mm up and down |
| ctrl_mode.speed | Options:`ctrl_mode.SPEED_FAST`、`ctrl_mode.SPEED_NORMAL` |

#### 4.5.3 Function
  
| Function | Purpose |
|----|----|
| ctrl_mode.sync() | Synchronize the settings to Sirius. |

### 4.6 edit_mode

#### 4.6.1 Creating Objects

```python
edit_mode= robot_control.switch_mode(sparky.MODE_EDIT)
```

#### 4.6.2 Object Properties 

| Object | Property |
|--------|----| 
| edit_mode.pitch | Range of [1,-1] rad |
| edit_mode.roll | Range of [1,-1] rad |
| edit_mode.yaw | Range of [1,-1] rad |
| edit_mode.headpitch | Range of [1,-1] rad |
| edit_mode.headyaw | Range of [1,-1] rad |
| edit_mode.tranx | Body displacement in X-axis direction, range [-50,50] |
| edit_mode.trany | Body displacement in Y-axis direction, range [-50,50] |
| edit_mode.tranz | Body displacement in Z-axis direction, range [0,141] |
| edit_mode.front_left_leg_x | X of front left foot, range [-25,175] |
| edit_mode.front_left_leg_y | Y of front left foot, range [-45,155] |
| edit_mode.front_left_leg_z | Z of front left foot, range [-100,100] |
| edit_mode.front_right_leg_x | X of front right foot, range [-25,175] |
| edit_mode.front_right_leg_y | Y of front right foot, range [-155,45] |
| edit_mode.front_right_leg_z | Z of front right foot, range [-100,100] |
| edit_mode.back_left_leg_x | X of rear left foot, range [-175,25] |
| edit_mode.back_left_leg_y | Y of rear left foot, range [-45,155] |
| edit_mode.back_left_leg_z | Z of rear left foot, range [-100,100]|
| edit_mode.back_right_leg_x | X of rear right foot, range [-175,25] |
| edit_mode.back_right_leg_y | Y of rear right foot, range [-155,45] |
| edit_mode.back_right_leg_z | Z of rear right foot, range [-100,100] |
| edit_mode.acc | Options: `edit_mode.SPEED_FASTEST`、`edit_mode.SPEED_FAST`、`edit_mode.SPEED_SLOW`、`edit_mode.SPEED_SLOWEST` |
| speed |Options: `edit_mode.SPEED_FASTEST`、`edit_mode.SPEED_FAST`、`edit_mode.SPEED_SLOW`、`edit_mode.SPEED_SLOWEST` |

#### 4.6.3 Function

- **edit_mode.get_parameter()**
  
To obtain the torque output configuration of the motor, it is necessary to add a message callback reception in robot_comtrol and return it in `JSON` format as shown below:

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
-  **`edit_mode.set_parameter(type, value)`  Set the torque output of the motor**

| type (optional) | value (optional) |
|----|----|
|`sparky.PARM_TYPE_HEAD`、`sparky.PARM_TYPE_FRONTLEFT`、`sparky.PARM_TYPE_FRONTRIGHT`、`sparky.PARM_TYPE_BACKLEFT`、`sparky.PARM_TYPE_BACKRIGHT`、`sparky.PARM_TYPE_ALL`|`sparky.PARM_VALUE_ENABLE`、`sparky.PARM_VALUE_DISABLE`、`sparky.PARM_VALUE_LIMIT`、`sparky.PARM_VALUE_UNLIMIT`|

| Function | Purpose | Remarks |
|----|----|----|
| edit_mode.save(path='keyframe.txt', index=None) | Save the current keyframe settings to a file | `path`: file address， `index`: which line, fill in to overwrite the specified line, and add it backwards by default.|
| edit_mode.read(path='keyframe.txt', index=0) | Read specified line to settings | `path`: file address，`index`: which line, the first line by default. |

### 4.7 wave_mode

#### 4.7.1 Creating Objects

```python
wave_mode= robot_control.switch_mode(sparky.MODE_WAVE)
```

#### 4.7.2 Creating Objects

| 对象 | 属性 | 备注 |
|-----|-----|-----|
| wave_mode.bpm | Control global bpm | By default, there are 60 beats per minute |
| wave_mode.wave_mode | Control waveform type | 1: Sine wave, 2: Square wave, 3: S-shaped curve|
| wave_mode.positive_ratio | The proportion of the positive half cycle to the entire cycle is `0 < ratio <= 1` ||
| wave_mode.amplitude_1 | Amplitude | |
| wave_mode.frequency_1 | Duty cycle | |
| wave_mode.amplitude_2 |||
| wave_mode.frequency_2 |||
| wave_mode.amplitude_3 |||
| wave_mode.frequency_3 |||

## V.Error and exception handling ​  

### 5.1 Disconnect  

If Sirius is disconnected, the error callback function will receive information at this time, and Sirius will automatically enter the recovery operation.  

But if it has disconnected for a long time, please check whether Sirius's own network status is normal? Whether to display the IP address.  

## VI.Version

| Version | Purpose |
|------|------|
| 0.0.1 | Achieve basic functions |