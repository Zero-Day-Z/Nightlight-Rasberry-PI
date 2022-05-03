import RPi.GPIO as GPIO
import time
from ADCDevice import *
import smtplib

#Initialize Email
SMTP_SERVER = 'smtp.gmail.com' #Email Server (don't change!)
SMTP_PORT = 587 #Server Port (don't change!)
GMAIL_USERNAME = #email
GMAIL_PASSWORD = #password

#Email CLass
class Emailer:
    def sendmail(self, recipient,  subject, content):
        #Creating the headers
        headers = ["From: " + GMAIL_USERNAME, "Subject: " +subject, 
            "To: " + recipient, "MIME-Version 1.0", "Content-Type: text/html"]
        headers = "\r\n".join(headers)

        #Connect to Gmail Server
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()

        #Login to Gmail
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

        #Send Email & Exit
        session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
        session.quit

ledPin = 11 # define ledPin
adc = ADCDevice() # Define an ADCDevice class object
def setup():
    global adc
    if(adc.detectI2C(0x48)): # Detect the pcf8591.
        adc = PCF8591()
    elif(adc.detectI2C(0x4b)): # Detect the ads7830
        adc = ADS7830()
    else:
        print("No correct I2C address found, \n"
        "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
        "Program Exit. \n")
        exit(-1)
    global p
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin,GPIO.OUT) # set ledPin to OUTPUT mode
    GPIO.output(ledPin,GPIO.LOW)
 
    p = GPIO.PWM(ledPin,1000) # set PWM Frequence to 1kHz
    p.start(0)

def loop():
    while True:
        value = adc.analogRead(0) # read the ADC value of channel 0
        p.ChangeDutyCycle(value*100/255)
        voltage = value / 255.0 * 3.3
        print ('ADC Value : %d, Voltage : %.2f'%(value,voltage))
        if voltage >= 2.0:
            print("Nightlight on!")
            sender = Emailer()
            sendTo = #recipient email
            emailSubject = "IOT Research: Nightlight "
            emailContent = "This is the Pi in the lab.\n The nightlight has been turned on!"
            sender.sendmail(sendTo, emailSubject, emailContent)
        time.sleep(1)
def destroy():
    adc.close()
    GPIO.cleanup()
 
if __name__ == '__main__': # Program entrance
    print ('Program is starting ... ')
    setup()
    try:
        loop()
    except KeyboardInterrupt: # Press ctrl-c to end the program.
        destroy()
