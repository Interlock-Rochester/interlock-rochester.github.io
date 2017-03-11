11 Digit, 7 Segment Display
###########################
:date: 2013-05-17 13:26
:author: BleuLlama
:category: Hardware, Projects
:slug: 11-digit-7-segment-display
:status: published

|image0|

*An early test result, showing text and millseconds since power-on.*

About a year ago, I bought a few 11 digit, 7 segment red LED displays
from Active Surplus up on Queen Street in Toronto. (Excellent store.  If
you're into hacking stuff at all, it's well worth the trip. Look for the
monkey on Queen street to find their entrance.)

This past week, I wasn't sure what to do at Interlock on Tuesday night,
but I had recently re-found these displays, so I figured I would finally
get them working.  I hit Radio Shack to get a Seeed Studio Arduino
Shield ($10 with a mess of components, probably the best deal in all of
Radio Shack.)

|image1|

*The display with a header soldered on, and the shield with its assorted
parts.*

I was all set to figure out how to reverse-engineer the pinout on the
bottom of the display; I googled for the LED module, and found specs on
those, and then on a whim, decided to check on the entire module board,
a Rohm LU-3011, and found the jackpot, \ `this post about figuring out
the
pinout <http://bobdasquirrel.blogspot.com/2011/08/rohm-lu-3011-led-display-module.html>`__.
 It suddenly became very easy to do this project.

The two key things gleaned from that above post, which I have mirrored
here, are this table of enables for each of the 11 digits:

+---------+-----+-----+-----+-----+-----+-----+------+------+------+------+------+
| Digit   | 1   | 2   | 3   | 4   | 5   | 6   | 7    | 8    | 9    | 10   | 11   |
+---------+-----+-----+-----+-----+-----+-----+------+------+------+------+------+
| Pin     | 1   | 2   | 3   | 4   | 6   | 8   | 10   | 12   | 14   | 16   | 18   |
+---------+-----+-----+-----+-----+-----+-----+------+------+------+------+------+

and this image, showing the pin mappings of the segments:

|image2|

*Mapping of the segments to the pins on the header.*

The basic way these displays work is that all of the 7 segments (plus
one decimal point) are all tied together to the pins specified above.
 Then the anodes for each of the displays are broken out to the pins in
the table above.  So to draw a '7', you would set all of the segments to
LOW, except for pins 11, 19, and 7 which you set HIGH.  Then to turn on
a specific digit, let's say digit 11 (rightmost), you set the digit
enable pin 18 to be an output, and set it LOW.  Set all of the other
digit enables to be inputs (tri-state, not low or high), and only
position 11 will show a "7".  You repeat this for all of the 11 digits
in the display, and you can display 11 full digits from just those 19
pins.

In my code (available below) I start at digit 1, and work down to digit
11, enabling each one, in turn, showing its segments, waiting 1
millisecond, then disable that digit, move on to the next one.

I soldered a pin header on the display, and built up a shield to plug it
into.

|image3|

*All of the digit enables wired up.  The top ones are a bit messy. Sorry
about that.*

I wired it up such that the digit enables and segments are wired
directly to IO lines on my Arduino.  This used all of the IO lines,
minus the D13 pin, which has an on-board LED.

The code that I wrote (available below) lets you do arbitrary digits per
character, so that i can do (primitive) alphanumerics, or do animation
patterns, etc.  I also store the decimal point as a separate character
going in to the display code, so "3.141" is five ascii characters going
in, but a flag is set on the '3' position saying that this digit should
also display its decimal point, so it only consumes four digits in the
display.

|image4|

*just testing out all of the segments and digits*

For now, it displays a nice clock and some animations on my desk, but I
plan on changing it around a little in the near future.  I want to use
the D13 line as one of the segment enables (probably decimal point) and
move the segment enables off of the Serial Receive line.  That way i
will be able to control it via serial to display patterns, animations or
text content.  Since the hardware serial port is hardwired to 0 and 1,
and I will be using the TX line for the LED displays, I'll have to
instead use the Software Serial, with only its Receive line mapped to an
IO pin, and its Transmit line mapped to junk. I've done this before and
it works well.

The code for this project is \ `available in my Geodesic Sphere github
repository <https://github.com/BleuLlama/GeodesicSphere/tree/master/Projects/SevenSegment11>`__.

This post is also available on `my personal project blog
thing <http://geodesicsphere.blogspot.com/2013/05/11-digit-7-segment-display.html>`__.

.. |image0| image:: http://1.bp.blogspot.com/-dkD0ogUU58o/UZZwNl-PA-I/AAAAAAAACbg/9s-kiPZUZ8Q/s640/IMG_1468.JPG
   :class: aligncenter
   :width: 640px
   :height: 478px
   :target: http://1.bp.blogspot.com/-dkD0ogUU58o/UZZwNl-PA-I/AAAAAAAACbg/9s-kiPZUZ8Q/s1600/IMG_1468.JPG
.. |image1| image:: http://4.bp.blogspot.com/-gRsOSI_LtfU/UZZz1mwZnpI/AAAAAAAACb4/or8abBr4-TM/s640/IMG_1459.JPG
   :width: 640px
   :height: 478px
   :target: http://4.bp.blogspot.com/-gRsOSI_LtfU/UZZz1mwZnpI/AAAAAAAACb4/or8abBr4-TM/s1600/IMG_1459.JPG
.. |image2| image:: http://2.bp.blogspot.com/-O2_Yz-oWDgE/UZZstuDtijI/AAAAAAAACbQ/eLleHoWirVw/s320/digit.JPG
   :width: 320px
   :height: 300px
   :target: http://2.bp.blogspot.com/-O2_Yz-oWDgE/UZZstuDtijI/AAAAAAAACbQ/eLleHoWirVw/s1600/digit.JPG
.. |image3| image:: http://4.bp.blogspot.com/-bh1tSeeWrGA/UZZ0MK4HVlI/AAAAAAAACcA/cBy-KgCnyfg/s640/IMG_1463.JPG
   :class: aligncenter
   :width: 640px
   :height: 478px
   :target: http://4.bp.blogspot.com/-bh1tSeeWrGA/UZZ0MK4HVlI/AAAAAAAACcA/cBy-KgCnyfg/s1600/IMG_1463.JPG
.. |image4| image:: http://2.bp.blogspot.com/-Iu8GH9eT68o/UZZ0WDS63kI/AAAAAAAACcI/HTfpMMcb3Fg/s640/IMG_1464.JPG
   :class: aligncenter
   :width: 640px
   :height: 478px
   :target: http://2.bp.blogspot.com/-Iu8GH9eT68o/UZZ0WDS63kI/AAAAAAAACcI/HTfpMMcb3Fg/s1600/IMG_1464.JPG
