from picamera import PiCamera
from time import sleep

camera = PiCamera()

"""You can alter the transparency of the camera preview
by setting an alpha level between 0 and 255: """
camera.start_preview(alpha=200)
sleep(10)
camera.stop_preview()

"""rotate the camera if necessary for a better preview
camera.rotation = 180
camera.start_preview()
sleep(10)
camera.stop_preview()
"""

"""taking still pictures"""
camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()

"""take a loop of 5 pictures
camera.start_preview()
for i in range(5):
    sleep(5)
    camera.capture('/home/pi/Desktop/image%s.jpg' % i)
camera.stop_preview()
"""

"""Recording video"""
camera.start_preview()
camera.start_recording('/home/pi/video.h264')
sleep(10)
camera.stop_recording()
camera.stop_preview()

"""to play the video : pi@raspberrypi:~ $ omxplayer video.h264"""

"""Add effects"""

"""maximum resolution is 2592 x 1944 for still photos and
1920 x 1080 for video recording."""
camera.resolution = (2592, 1944)
camera.framerate = 15
camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/max.jpg')
camera.stop_preview()


"""Add some text to your image with annotate_text"""
camera.start_preview()
camera.annotate_text = "Hello world!"
sleep(5)
camera.capture('/home/pi/Desktop/text.jpg')
camera.stop_preview()


"""Alter the brightness setting, which can be set from 0 to 100. The default is 50.
Try setting it to another value"""
camera.start_preview()
camera.brightness = 70
sleep(5)
camera.capture('/home/pi/Desktop/bright.jpg')
camera.stop_preview()


"""Try adjusting the brightness in a loop, and annotating the display with
the current brightness level:"""
camera.start_preview()
for i in range(100):
    camera.annotate_text = "Brightness: %s" % i
    camera.brightness = i
    sleep(0.1)
camera.stop_preview()

"""Adjust the contrast:"""
camera.start_preview()
for i in range(100):
    camera.annotate_text = "Contrast: %s" % i
    camera.contrast = i
    sleep(0.1)
camera.stop_preview()

"""Set the annotation text size"""
camera.annotate_text_size = 50
Valid sizes are 6 to 160. The default is 32.

"""Alter the annotation colours. First of all, ensure that Color is imported
from picamera import PiCamera, Color
"""
camera.start_preview()
camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')
camera.annotate_text = " Hello world "
sleep(5)
camera.stop_preview()

"""Apply a particular image effect. The options are: none, negative, solarize,
sketch, denoise, emboss, oilpaint, hatch, gpen, pastel, watercolor, film, blur,
saturation, colorswap, washedout, posterise, colorpoint, colorbalance, cartoon,
deinterlace1, and deinterlace2. The default is none. Pick one and try it out:"""
camera.start_preview()
camera.image_effect = 'colorswap'
sleep(5)
camera.capture('/home/pi/Desktop/colorswap.jpg')
camera.stop_preview()

"""Loop over the various image effects in a preview to test them out:"""
camera.start_preview()
for effect in camera.IMAGE_EFFECTS:
    camera.image_effect = effect
    camera.annotate_text = "Effect: %s" % effect
    sleep(5)
camera.stop_preview()
