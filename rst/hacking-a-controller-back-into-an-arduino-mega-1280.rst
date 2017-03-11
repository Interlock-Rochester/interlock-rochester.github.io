Hacking a controller back into an Arduino Mega 1280
###################################################
:date: 2016-02-22 14:55
:author: BleuLlama
:category: Hardware, Projects
:slug: hacking-a-controller-back-into-an-arduino-mega-1280
:status: published

|image0|

At `Interlock <http://interlockroc.org/>`__, JustBill handed me the old
controller board for a gutted 3D printer that he was rebuilding. "Do
whatever you want with this." A close inspection of the board showed
that it had a main microcontroller of the ATmega 1280, which is the chip
used in older Arduino Megas.  The interface to USB however was an ATmega
8u2, which is the chip used in newer Arduino Megas, and you may also
know it from older Arduino Unos... modern Uno R3s use a 32u4.

This board had custom firmware on it so that it didn't look like an
Arduino, or any sort of serial connection to the host computer it's
plugged into... so as-is, it was useless for general use as an Arduino;
taking advantage of the GUI and clicky-clicky programmer interface.

So my thought was, it might be nice to have my own 'Mega for testing and
such.  Could this board be set up in a way that might make this process
and outcome easy?  Turns out it mostly was.

The original board got its power from a power terminls on the board,
24V.  It needed to power the stepper motors, and such so it needed to be
beefy.  This was dropped down to 5 and 3.3 on the board itself.

There is a USB B jack for connecting this to a host computer, which did
not have its 5V connected, so my thought was, what if i hooked up this
5V to the USB jack.  would that be enough to power the chips?

|image1|

I added this jumper, which connects the +5 on the USB jack to the 5v bus
on the board, and plugged it in, and sure enough, it beeped and came to
life without its host power supply.

Next up would be reprogramming the micros to have the arduino bootloader
and code on them.

|image2|

I hooked up my fairly cheesy Arduino D-15 (hacked stepper motor
controller) ISP to the 6 pin header, which thankfully was already
populated and labelled on the board!  I plugged it into the port
labelled "1280 ISP", selected the Arduino Mega, with 1280 micro from the
Arduino 1.6.6 menus, selected Arduino ISP for the programmer, then
selected "load bootlader".  In about a minute, it seemed to have
completed successfully.... if something didn't jive, it would have
spewed out sync or device errors to the screen...  Seemed good so far!

Next, was hooking it up to the jack labelled 8u2 ISP.  This was a little
trickier because I wasn't installing the bootloader (which the Arduino
IDE makes REALLY easy to do), but rather the secondary micro's firmware,
which basically was just a USB-Serial interface driver.

Long story short, I grabbed the `8u2 code from github,
"MEGA-dfu_and_usbserial_combined.hex" <https://github.com/arduino/Arduino/tree/master/hardware/arduino/avr/firmwares/atmegaxxu2>`__,
and used the following command line (using a mixture of the code on that
page, with the parameters that my system used via the arduino IDE on my
Mac:

  ./avrdude -p at90usb82 -F -cstk500v1 -P/dev/cu.usbserial-A800czia
-b19200 -U flash:w:8u2.hex  -U lfuse:w:0xFF:m -U hfuse:w:0xD9:m -U
efuse:w:0xF4:m -U lock:w:0x0F:m
-C/Users/me/Library/Arduino15/packages/arduino/tools/avrdude/6.0.1-arduino5/etc/avrdude.conf

In short, it sets the CPU to at90usb82, uses the stk500v1 communications
protocol over the /dev/cu.usbserial driver, at 19200 baud.... it
programs the file 8u2.hex, sets fuses and sets other avrdude
configuration stuff.

After lots of text scrolling by from running that, I was able to drop a
program I was working on, onto it via the Arduino IDE directly, without
any problems at all! I set the port to the serial Mega, set the board to
"Arduino Mega", cpu set at "Mega 1280", clicked 'upload' and bam, fully
functional serial communications from the serial montior down through to
the '1280 on the board.

|image3|

Whoo! Free Arduino Mega for me!

Edit: Here's the pinouts of stuff I beeped out. The number is the
digital (or Analog where applicable) pin on an Arduino Mega board.  So
digital 24 from Arduino corrolates to the "A Dir" pad on the board.

-   \* 4 - Piezo +
-   \* 6 - heat
-   \* 7 - fan
-   \* 24 - A Dir
-   \* 25 - A Step
-   \* 26 - A Enable
-   \* 27 - A Pot
-   \* 28 - B Dir
-   \* 29 - B Step
-   \* 36 - debug 2
-   \* 37 - debug 3
-   \* 38 - (nc)
-   \* 39 - B Enable
-   \* 40 - debug 4
-   \* 41 - PG0
-   \* 42 - TP33 / Z-MAX
-   \* 43 - TP32 / Z-MIN
-   \* 44 - Extra +/R85
-   \* 45 - bp heat
-   \* 46 - TP31 / Y-MAX
-   \* 47 - TP30 / Y-MIN
-   \* 48 - TP29 / X-MAX
-   \* 49 - TP28 / X-Min
-   \* A0 - X Dir
-   \* A1 - X Step
-   \* A2 - X Enable
-   \* A3 - X Pot
-   \* A4 - Y Dir
-   \* A5 - Y Step
-   \* A6 - Y Enable
-   \* A7 - Y Pot
-   \* A8  - Z Dir
-   \* A9  - Z Step
-   \* A10 - Z Enable
-   \* A11 - Z Pot
-   \* A12 - PK4 / JP7
-   \* A13 - PK5 / JP7
-   \* A14 - PK6 / JP6
-   \* A15 - TP27 / HBP Therm

The molex switch connectors seem to have the pinout: (signal) (ground)
(ground) (+5v)

.. |image0| image:: https://1.bp.blogspot.com/-edLQSlCXI9w/VslDiFt8WPI/AAAAAAAADdU/AfRVH7ND3Fo/s640/FullSizeRender_1.jpg
   :class: aligncenter
   :width: 640px
   :height: 480px
   :target: https://1.bp.blogspot.com/-edLQSlCXI9w/VslDiFt8WPI/AAAAAAAADdU/AfRVH7ND3Fo/s1600/FullSizeRender_1.jpg
.. |image1| image:: https://3.bp.blogspot.com/-PBreWXxPx_U/VslDf1YJClI/AAAAAAAADdM/_a0TAusuQvk/s640/FullSizeRender.jpg
   :class: aligncenter
   :width: 640px
   :height: 480px
   :target: https://3.bp.blogspot.com/-PBreWXxPx_U/VslDf1YJClI/AAAAAAAADdM/_a0TAusuQvk/s1600/FullSizeRender.jpg
.. |image2| image:: https://2.bp.blogspot.com/-gPvnDEyf8aY/VslDp2zR3mI/AAAAAAAADdY/H0kpGhzhA98/s640/IMG_0702.JPG
   :class: aligncenter
   :width: 640px
   :height: 480px
   :target: https://2.bp.blogspot.com/-gPvnDEyf8aY/VslDp2zR3mI/AAAAAAAADdY/H0kpGhzhA98/s1600/IMG_0702.JPG
.. |image3| image:: https://4.bp.blogspot.com/-qazqVuRpJJo/VslDhbqR7WI/AAAAAAAADdc/_wIVTC-xUHA/s640/IMG_0700.JPG
   :class: aligncenter
   :width: 640px
   :height: 480px
   :target: https://4.bp.blogspot.com/-qazqVuRpJJo/VslDhbqR7WI/AAAAAAAADdc/_wIVTC-xUHA/s1600/IMG_0700.JPG
