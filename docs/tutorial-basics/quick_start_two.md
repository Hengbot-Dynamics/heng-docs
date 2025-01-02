---
sidebar_position: 8

---
# Advanced-level (I): UI Usage

## I.Preface  

We will introduce Sirius's head User Interface (UI) here. Its head is not only the core of its vision and interaction, but also integrates a rich User Interface (UI) and surprises from R&D personnel of HENGBOT.

## II.User Interface (UI)  

### 2.1 Usage Skills  

Firstly, let's introduce some common gameplay skills to help everyone quickly get started.

| **Items** | **Skills** | **Reference picture** |
|----|----|---|
| **All operations after entering the interactive page** | Simply select "Exit" or "Enter" through the buttons on the left and right ears of Sirius, and confirm by tapping the area on the head. | ![head](./img/head.jpg) |

### 2.2 Color Recognition

> Color recognition usually involves image processing and machine learning techniques. Color recognition is like giving Sirius a "Color palette" that not only allows it to see the colors in the image, but also recognizes specific colors and marks the colors that the user is interested in.

<iframe width="780" height="400" src="https://www.youtube.com/embed/D72uZHluP_s?si=ZFdCK-wyzF8Mfkao" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe> 

Follow the steps below to experience the color recognition function:  

| Steps | Reference picture |
|---------|------|
| **Step 1: Select Color Recognition** In the "More Features" menu, use the button to select the "Color Recognition". And activate the function by touching the top of the head.。| ![ui_rgb](./img/Quick_use_img/ui_rgb.jpg) |
| **Step 2: Prepare the recognition object**：After the function is activated, prepare a red ball or red paper box. Ensure that the object is completely within the field of view of the head camera, so that Sirius can automatically perform color recognition and tracking.| |

If you need to recognize other colors, you may need to modify the backend script to meet the requirement of different color recognition.

### 2.3 Self-Balancing

> Self-Balancing refers to the ability of a system or device to automatically adjust its posture or position to maintain a stable state; Imagine it's like Sirius having its own "Sense of Balance"; When it stands, whether it is lightly pushed or fine tuned in position, its internal system quickly senses these changes and restores balance by finely adjusting leg movements.

<iframe width="780" height="400" src="https://www.youtube.com/embed/6p6EiA26qwU?si=88CYzRoqmllL6nZl" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

To observe how Sirius achieves self-balancing posture under different movements, please follow the steps below:

| Steps | Reference picture |
|---------|------|
| **Step 1: Select the "Self-balancing" function** In the "More Features" menu, use the button to select the "Self-balancing" and activate this function by touching the top of the head.| ![ui_demo](./img/Quick_use_img/ui_demo.png) |
| **Step 2: Single-leg Lifting Test** Gently lift Sirius's single leg and observe how its other three legs slowly and steadily adjust its position to maintain the balance of the entire body.| |
| **Step 3: Dual-leg Lifting Test** Try to lift both the front left and right legs of Sirius at the same time, observe how its hind legs cleverly lower the height and lift the buttocks to maintain overall balance.||
|**Step 4: Customize Balance Actions** Now, you can freely try the actions you want to keep Sirius balanced. ||

These steps not only help you understand the self-balancing ability of Sirius, but also allow you to explore more creative gameplay. But remember to ensure that Sirius is in a safe environment during testing to avoid injury caused by losing balance.

### 2.4 Freedom Mode  

You can activate the Freedom Mode by following steps:  

| Steps | Reference picture |
|---------|------|
| **Step 1: Select Freedom Mode** In the "More Features" menu, use the left and right ear buttons to select the "Freedom Mode". After confirming the selection, activate this feature by touching the top of the head.| ![ui_free_mode](./img/Quick_use_img/ui_free_mode.jpg) |
| **Step 2: Experience Freedom Mode** After activating Freedom Mode, Sirius will stare at you like an observer, and its head will move along with your facial movements. At the same time, its legs will be in a semi-unloaded force of self-balancing state, so there is no need to worry about any impact on the robot dog even if there is a slight collision or compression. | |


### 2.5 Remote Control Mode  

Remote control mode is one of the core features of the UI on the Sirius's head, designed specifically for remote control of Sirius. In this mode, users can perform network settings to connect with Sirius's App, and use WebSocket API interface for deeper development.  

| Steps | Reference picture |
|-------|------|
| Select **"Remote Control Mode"** directly from the main menu. After confirming the selection, activate this feature by touching the top of the head. | ![ui_app](./img/Quick_use_img/ui_app.png) |



### 2.6 Developer Mode  

| Introduction | Reference picture |
|---------|------|
| The developer mode is designed for developers who want deep programming and secondary development. Once enabled, Sirius's UI will be suspended, so that developers can use the API interface documents provided by HENGBOT and realize their innovative ideas through programming languages such as Python. | ![ui_api](./img/Quick_use_img/ui_api.jpg)|

> [Mid-level (II): Python API](./python_api.md)  

> [Mid-level (III): WebSocket API](./deploy_your_site.md)

### 2.7 More Settings on the Head  

| Introduction | Reference picture | Video |
|---------|------|------|
| Five options are preset in the settings, such as Wi-Fi, Volume, System Self-check, System Information, and Return to Previous menu for users to operate. | ![ui_settings](./img/Quick_use_img/ui_settings.jpg) | <iframe width="580" height="380" src="https://www.youtube.com/embed/rsfhIzw3UIE?si=i7me8lW9ld3sJfWN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe> |

| Function | Introduction | Reference picture |
|---------|------|------|
| **How to connect to Wi-Fi network?** | In addition to automatic networking upon startup, Wi-Fi connection can also be manually enabled with the same operation.| ![ui_wifi](./img/Quick_use_img/ui_wifi.jpg) |
| **How to adjust the volume?** | We can control Sirius's barking by adjusting the volume.| ![ui_volume](./img/Quick_use_img/ui_volume.jpg) |
| **How to perform system self-checking?** | After activation, it will automatically perform self-checking on the hardware IMU, KEY, Battery, Wi-Fi Driver, and Motor Servo to ensure that there are no issues with any hardware before experiencing the software function.| ![app_check](./img/Quick_use_img/app_check.jpg) |
| **Check system information** | After activation, Sirius will automatically read system information | ![ui_system](./img/Quick_use_img/ui_system.jpg) |

So far, you have already learned and understood your Sirius on a basic level. It's the end of guidance. It's time for you to explore more interesting gameplay!