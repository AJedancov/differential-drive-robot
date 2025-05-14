

# Differential Drive Robot

This project provides software for controlling a robot with a differential drive.   
It supports teleoperation and go-to-goal behavior, making it suitable for educational robotics applications.

## Repository structure
```shell
.
├── lib
│   ├── AS5600
│   ├── Encoder
│   ├── InitData
│   ├── Motor
│   ├── PID
│   ├── Position
│   ├── TwoWheeledRobot
│   └── Velocity
├── scripts
│   ├── SocketClient.py
│   └── SocketServer.py
└── src
    └── main.cpp
```

<!-- Classes structure:  
<img src="img/classes.png" width="400"> -->

## Hardware components

<div align="center">
  <img src="img/differential-drive-robot.jpg" width="500">
</div>

The robot includes the following components:

|      **Component**     |        **Description**           |
| ---------------------- | -------------------------------- |
| **Raspberry pi 4 8gb** | Single-board computer            |
| **Arduino Mega 2560**  | Microcontroller board            |
| **TB6612FNG**          | Motor driver                     |
| **AS5600**             | Hall-Effect magnetic encoder     |
| **CJMCU-9548**         | I2C Multiplexer                  |
| **XL4015 5A**          | DC/DC converter                  |
| **4S 40A 18650**       | BMS Protection Board with balance|
| **NCR18650B**          | Rechargeable Li-ion Batteries    |

<!-- Below is the connection of all elements -->

## Prerequisites

- [AS5600](https://github.com/RobTillaart/AS5600)  
  This code uses a third party library AS5600 licensed under the MIT License.

- [PlatformIO](https://platformio.org/)

  For more convenient work with the microcontroller board Arduino Mega 2560 PlatformIO is used.  
  It provides a cross-platform build system, library manager, and integrated development environment (IDE) support

  You can download [PlatformIO Core](https://docs.platformio.org/en/latest/core/installation.html#piocore-install-shell-commands) separately OR use the [Visual Studio Code IDE Extension](https://platformio.org/install/ide?install=vscode).

  > `Note`   
  > You don't need to install PlatformIO Core separately if you're using the PlatformIO IDE.   
  > The IDE already includes PlatformIO Core, and you can access it directly through the PlatformIO IDE Terminal.

## Installation
Clone the repository:
```shell
git clone https://github.com/AZhed/differential-drive-robot.git &&
cd differential-drive-robot
```
## Usage

Connect remotely to Raspberry Pi using SSH.

### Remote control
Remote control requires that the Raspberry Pi and PC are connected to the same Wi-Fi network.

1. Find out the IP address of Raspberry Pi.   
  This can be done with the following command:
  ```shell
  ip address show
  ```

2. Check local IP address: `inet <IP-adress>`  
  This IP address must be specified in the scripts [SocketServer.py](/scripts/SocketServer.py) and [SocketClient.py](/scripts/SocketClient.py) as a `HOST` variable.

3. Start the Server on Raspberry Pi:
  ```shell
  python3 scripts/SocketServer.py
  ```

4. Start the Client on PC:
  ```shell
  python3 scripts/SocketClient.py
  ```

Use the following keys on your keyboard to control the robot:

| **Key** | **Command**                    |
|---------|--------------------------------|
| w       | Move forward                   |
| x       | Move backward                  |
| a       | Turn left                      |
| d       | Turn right                     |
| s       | Stop moving                    |
| e       | Increase the speed             |
| q       | Decrease the speed             |
| Ctrl+С  | Terminate the Сlient or Server |



## License

This project is licensed under the [MIT](./LICENSE) license.
