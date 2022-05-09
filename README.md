# Nightlight-Rasberry-PI

# Description
This project uses a light sensor to turn on an LED light when it is dark on Raspberry Pi. This code also uses an email class with smtplib to send a notication via email when the voltage reading is high. This project assumes that you have already setup your Raspberry Pi and have the Freenove Starter kit directory. If you do not you will need to setup Raspberry Pi and Freenove before you start this project. 

# Materials Needed
## Hardware
1. Raspberry Pi x1
2. GPIO Extension Board & Ribbon Cable x1
3. Breadboard x1
4. Photoresistor sensor x1
5. ADC Module x1
6. Resistors x4
7. LED Light x1
8. Male-to-Male Jumper Wires x15

## Software
1. nightLight.py from this repository

# Setup and Configuration
## Hardware
Below is the following pinout for this project:
![photoresistor](https://user-images.githubusercontent.com/66813474/167410935-00c00fca-9147-4de0-9189-6ed4b1c2920c.PNG)

_Note: please plug in your cables BEFORE turning on your Raspberry Pi to prevent shorting out your parts._

# Code Setup
1. Download nightLight.py
2. Open nightLight.py and change the following lines to correspond with the email notication:
    1. line 9: enter the email that you want to send the notification from
    2. line 10: enter the password to the email from line 10
    3. line 63: enter the recipient email
    4. line 64(optional): you can change the email subject
    5. line 65(optional): you can change the contents of the email
4. Run nightLight.py and move an object in front of the sensor to measure speed and velocity.
