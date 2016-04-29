import serial
import pygame
import time

#serialPort = '/dev/tty.usbserial-A7004Jg4' # Arduino Mega
# serialPort = '/dev/tty.usbmodemfd121'       # Arduino Uno
# baudRate = 9600

# Open Serial Connection to Arduino Board
# ser = serial.Serial(serialPort, baudRate, timeout=1);

'''
Gets joystick data and prints it
'''

pygame.init()
j = pygame.joystick.Joystick(0)
j.init()
print 'Initialized Joystick : %s' % j.get_name()

try:
    while True:
        pygame.event.pump()

        for i in range(0, j.get_numaxes()):
            if j.get_axis(i) != 0.00:
                print 'Axis %i reads %.2f' % (i, j.get_axis(i))
                exit()

        for i in range(0, j.get_numbuttons()):
            if j.get_button(i) != 0:
                print 'Button %i reads %i' % (i, j.get_button(i))
                exit()

except KeyboardInterrupt:
    j.quit()
except Exception, e:
    print e