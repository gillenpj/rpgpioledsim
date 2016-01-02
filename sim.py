from rpgpioled import *
rp = rpgpioled()

rp.setmode(BCM)
pins = [4, 17, 18, 27, 22, 23, 24, 25 ]

for pin in pins:
    rp.setup(pin, OUT)

i = 0
while True:
    i = i % 8
    rp.output(pins[i], HIGH)
    sleep(0.25)
    rp.output(pins[i], LOW)
    i = i + 1
