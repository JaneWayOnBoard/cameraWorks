from picamera import PiCamera
from time import sleep

camera = PiCamera()

"""Make a preview"""
camera.start_preview()
sleep(5)
camera.capture('image.jpg')
camera.stop_preview()

"""The line before the loop begins sets the image_number variable to be 0.
Within the loop, image_number is used to create a string called image_name.
The name is made up of the strings image and .jpg but in between those
strings is the image number, padded so it’s 4 digits long ({0:04d}).
You could alter {0:04d} to {0:02d} for instance, if you only wanted filename
numbers that were two digits long."""

image_number = 0

while True:
    sleep(5)
    image_name = 'image{0:04d}.jpg'.format(image_number)
    camera.capture(image_name)
    image_number += 1
