import json
import RPi.GPIO as gpio
import time

led_path = 'led-select.txt' # may or may not change, in same dir atm

gpio.setmode(gpio.BCM)

# LED port numbers
led1, led2, led3 = 16, 20, 21

# Setting ports to output
gpio.setup(led1, gpio.OUT)
gpio.setup(led2, gpio.OUT)
gpio.setup(led3, gpio.OUT)

# Creating pwm objects
pwm = {'a':gpio.PWM(led1, 1000), 'b':gpio.PWM(led2, 1000), 'c':gpio.PWM(led3, 1000)} # I hate if statements

# main loop

try:
    for x in pwm.values():
        x.start(0)

    while 1:
        with open(led_path, 'r') as f:
            data = json.load(f) # data like {'led':'a', 'value':'69'}
        
        pwm[data['led']].ChangeDutyCycle(int(data['value'])) # hmmm
        time.sleep(0.1) # chill it out yeah?
        print(data)

except KeyboardInterrupt:
    print('\nExiting')

except Exception as e:
    print(f'\nExiting because of {e}')

finally:
    gpio.cleanup()
