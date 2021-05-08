import threading
import time
from flask import Flask
from flask import request
import RPi.GPIO as GPIO
app=Flask(__name__)

def blink():
    global thread_flag
    while True:
        if thread_flag == 2:
            break
        GPIO.output(25,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(25,GPIO.LOW)
        time.sleep(1)



@app.route('/', methods = ['GET'])
def job():
    global thread_flag
    
    my_led_status = request.args.get('led_status')
    
    if my_led_status == "0":
        thread_flag = 2
        GPIO.output(25,GPIO.LOW)
        return 'LED_off'
    elif my_led_status == "1":
        thread_flag = 2
        GPIO.output(25,GPIO.HIGH)
        return 'LED_on'
    elif my_led_status == "2":
        thread_flag = 1
        t = threading.Thread(target = blink)
        t.start()
        return "start"
    elif my_led_status == "3":
        thread_flag = 2
        return "stop"
    
if __name__=='__main__':
    global thread_flag
    thread_flag = 1
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(25,GPIO.OUT)
    app.run()
