from PiicoDev_LIS3DH import PiicoDev_LIS3DH
import machine

from machine import Pin
from utime import sleep_ms


bus = 0
scl = machine.Pin(1)
sda = machine.Pin(0)
freq=400_000


motion = PiicoDev_LIS3DH(bus=bus, scl=scl, sda=sda, freq=freq)

while True:
    
    motion_shake = motion.shake()
    
    if motion_shake > 20:
        print("Big shake!")
    
    elif motion_shake > 15:
        print("Medium shake!")
        
    elif motion_shake > 10:
        print("Small shake!")


