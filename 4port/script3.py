#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [2, 3, 4, 17]

# loop through pins and set mode and state to 'high'

for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop

SleepTimeL = 0.2

# main loop

try:
  GPIO.output(2, GPIO.LOW)
  time.sleep(SleepTimeL);

  GPIO.output(3, GPIO.LOW)
  time.sleep(SleepTimeL);

  GPIO.output(4, GPIO.LOW)
  time.sleep(SleepTimeL);

  GPIO.output(17, GPIO.LOW)
  time.sleep(SleepTimeL);

  GPIO.output(3, GPIO.HIGH)
  GPIO.output(4, GPIO.HIGH)
  time.sleep(SleepTimeL);

  GPIO.output(2, GPIO.HIGH)
  GPIO.output(17, GPIO.HIGH)
  GPIO.output(3, GPIO.LOW)
  GPIO.output(4, GPIO.LOW)
  time.sleep(SleepTimeL);

  GPIO.output(2, GPIO.LOW)
  GPIO.output(17, GPIO.LOW)
  GPIO.output(3, GPIO.HIGH)
  GPIO.output(4, GPIO.HIGH)
  time.sleep(SleepTimeL);

  GPIO.output(3, GPIO.LOW)
  GPIO.output(4, GPIO.LOW)
  time.sleep(SleepTimeL);

  GPIO.output(2, GPIO.HIGH)
  time.sleep(SleepTimeL);

  GPIO.output(3, GPIO.HIGH)
  time.sleep(SleepTimeL);

  GPIO.output(4, GPIO.HIGH)
  time.sleep(SleepTimeL);

  GPIO.output(17, GPIO.HIGH)
  time.sleep(SleepTimeL);

  GPIO.cleanup()
  print ("Good bye!")

# End program cleanly with keyboard
except KeyboardInterrupt:
  print ("  Quit")

  # Reset GPIO settings
  GPIO.cleanup()

# find more information on this script at
# http://youtu.be/WpM1aq4B8-A
