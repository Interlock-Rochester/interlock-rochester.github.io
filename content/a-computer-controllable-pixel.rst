A Computer Controllable Pixel
#############################
:date: 2012-09-26 11:58
:author: BleuLlama
:category: Projects
:slug: a-computer-controllable-pixel
:status: published

A few years ago, I put in an order at Sparkfun, which included 8 1-Watt
Luxeon LEDs.  My original thought was that I would rebuild an lightshow
device that I had built many years ago, but instead of it driving 110V
spot lights through solid state relays, it would instead be more
self-contained, and use high power LEDs instead.  This project never
happened, since I never figured out how to power the LEDs properly.

I've recently been getting into doing more little projects, especially
since I want to have *something* to do on Tuesday nights at Interlock.
 I saw the box of these things on the shelf, and decided to try driving
them directly from an Arduino.   I know that I could have used one of
the BlinkM modules, or the strand of RGB Pixels or whatever for this,
but I had these, and I wanted to see what I could do / how bright I
could make them without frying the Arduino.

|image0|

The project I decided to work on with them is to make a single
high-brightness RGB pixel, and drive it from a Processing sketch on my
computer.  Eventually, the thought might be to sample a TV's color,
30fps for a few hours, then just store those brightness/color levels.
 Then, play them back on the pixel to light a room.  From outside of the
room, it *should* look like a television is on, showing some kind of TV
show.  The way I went with testing this was to take a movie trailer, and
crunch it down to a few pixels, and then average the colors in it while
it plays back, live via Processing, then send the RGB values over
USB-Serial to be displayed on the pixel.

|image1|

I started out by soldering up a Red, Green, and Blue LED to a small
piece of perf board.  I tied them together for a common ground on one
side, and through a 220 ohm resistor on the other side, and all of this
out to the Arduino.  I use PWM pins on the Arduino to adjust their
brightness, since that's simple to do.

|image2|

The Processing sketch sends down 0..255 for red, green, and blue
intensities, then those values are plugged directly into the PWM pins
via AnalogWrite() calls, which displays a reasonable facsimile of the
color requested.

|image3|

The project worked out pretty darn well.  Without current drivers for
the LEDs, I can't make them too bright, but in an hour of sitting down
at Interlock, I had this working.  I wrote up two processing sketches.
 One with a RGB color wheel - click to send that color to the LEDs, and
another playing the video as described above.  (Arduino and Processing
sketches available upon request. :D )

.. |image0| image:: http://interlockroc.wpengine.com/wp-content/uploads/2012/09/2012-09-26-09.10.10-e1348677126508-300x271.jpg
   :class: aligncenter size-medium wp-image-994
   :width: 300px
   :height: 271px
   :target: http://interlockroc.wpengine.com/wp-content/uploads/2012/09/2012-09-26-09.10.10-e1348677126508.jpg
.. |image1| image:: http://interlockroc.wpengine.com/wp-content/uploads/2012/09/2012-09-26-09.13.51-300x224.jpg
   :class: aligncenter size-medium wp-image-997
   :width: 300px
   :height: 224px
   :target: http://interlockroc.wpengine.com/wp-content/uploads/2012/09/2012-09-26-09.13.51.jpg
.. |image2| image:: http://interlockroc.wpengine.com/wp-content/uploads/2012/09/2012-09-26-09.11.51-300x224.jpg
   :class: aligncenter size-medium wp-image-995
   :width: 300px
   :height: 224px
   :target: http://interlockroc.wpengine.com/wp-content/uploads/2012/09/2012-09-26-09.11.51.jpg
.. |image3| image:: http://interlockroc.wpengine.com/wp-content/uploads/2012/09/2012-09-26-09.12.31-300x224.jpg
   :class: aligncenter size-medium wp-image-996
   :width: 300px
   :height: 224px
   :target: http://interlockroc.wpengine.com/wp-content/uploads/2012/09/2012-09-26-09.12.31.jpg
