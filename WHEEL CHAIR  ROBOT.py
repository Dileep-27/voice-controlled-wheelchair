# Example showing how functions, that accept tuples of rgb values,
# simplify working with gradients
from machine import Pin, UART,PWM, ADC
import time,utime
buz = Pin(9, Pin.OUT)
trigger = Pin(14, Pin.OUT)
echo = Pin(15, Pin.IN)
def ultra():
   trigger.low()
   utime.sleep_us(2)
   trigger.high()
   utime.sleep_us(5)
   trigger.low()
   while echo.value() == 0:
       signaloff = utime.ticks_us()
   while echo.value() == 1:
       signalon = utime.ticks_us()
   timepassed = signalon - signaloff
   distance = (timepassed * 0.0343) / 2
   return distance

rcv = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))
buff = bytearray(255)
TIMEOUT = False

m1=Pin(10,Pin.OUT)
m2=Pin(11,Pin.OUT)
m3=Pin(12,Pin.OUT)
m4=Pin(13,Pin.OUT)


xac = ADC(27)
yac = ADC(28)
stp=Pin(26,Pin.IN)

while(1):
        time.sleep(0.3)
        dist=ultra()
        print('DIST:'+str(dist))
        if(dist<20):
                buz.value(1)
                print('STOP')
                m1.value(0)
                m2.value(0)
                m3.value(0)
                m4.value(0)
                time.sleep(3)
                buz.value(0)
                
            
        xval = xac.read_u16()
        print('X:'+str(xval))
    
        yval = yac.read_u16()
        print('Y:'+str(yval))
        
        sval=stp.value()
        print('S:'+str(sval))
 
        if(yval>60000):
                print('Front')
                m1.value(1)
                m2.value(0)
                m3.value(1)
                m4.value(0)
                
                
        if(yval<20000):
                print('BACK')
                m1.value(0)
                m2.value(1)
                m3.value(0)
                m4.value(1)
                
        if(xval<20000):
                print('LEFT')
                m1.value(0)
                m2.value(1)
                m3.value(1)
                m4.value(0)
                
        if(xval>60000):
                print('RIGHT')
                m1.value(1)
                m2.value(0)
                m3.value(0)
                m4.value(1)
                
        if((xval>60000 and yval>60000) or (xval>60000 and yval<20000) or (xval<20000 and yval>60000) or (xval<20000 and yval<20000)):
                print('STOP')
                m1.value(0)
                m2.value(0)
                m3.value(0)
                m4.value(0)
 
 
 
        x=rcv.read()
        
        if x is not None:
            x=(x.decode()).strip()
            #x=input('ENTER:')
            print(x)
            if(x=='1'):
                print('Front')
                m1.value(1)
                m2.value(0)
                m3.value(1)
                m4.value(0)
                
                
            if(x=='2'):
                print('BACK')
                m1.value(0)
                m2.value(1)
                m3.value(0)
                m4.value(1)
                
            if(x=='3'):
                print('LEFT')
                m1.value(1)
                m2.value(0)
                m3.value(0)
                m4.value(1)
                
            if(x=='4'):
                print('RIGHT')
                m1.value(0)
                m2.value(1)
                m3.value(1)
                m4.value(0)
                
            if(x=='5'):
                print('STOP')
                m1.value(0)
                m2.value(0)
                m3.value(0)
                m4.value(0)
                
  