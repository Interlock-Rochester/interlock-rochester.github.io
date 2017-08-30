Remote Control Hacking
######################
:date: 2012-07-20 07:00
:author: antitree
:category: Ham, Hardware, Security
:slug: remote-control-hacking
:status: published

A project that I've been spending a lot of time on, is learning about
how this silly little RF remote communicates to its home base. The
remote controls a music playing device and since it's RF, the project
required me to learn about radio frequencies and some hardware hacking.
I've been asking Interlock members for help and they've given me ideas
along the way. JustBill, one of our radio hackers, has jumped on the
project and started analyzing the remote from the RF perspective.
Berticus and Robo Alex have also donated their brains for the hardware
hacking portion. Our goal was to learn how the remote works so that we
can make our own remote.

RF RC
=====

This radio frequency remote control (RF RC) controls  a device that
plays music. For the purpose of this post, that's all we need to care
about it. Our first step was to do recon on the hardware so we
researched the `FCC
documents <http://transition.fcc.gov/oet/ea/fccid/>`__. Taking it apart
we learn that there are two boards we want to worry about. The remote
board that has an integrated circuit (IC) to handle button presses, and
a radio daughter board that takes input and converts it to a a radio
signal.

.. raw:: html

   <div align="center">

|image0|\ |image1|\ `
 </wp-uploads/2012/07/DSC_8664.jpg>`__

.. raw:: html

   </div>

IR IC
=====

After taking apart the remote, we look at the lower portion to find an
IC made by Hynix. Thankfully,
`Hynix <http://www.skhynix.com/en/index.jsp>`__ still sells a similar
chip that's designed for infra-red (IR) and was nice enough to give the
pin outs in the data sheet that looks like this:

|image2|

This tells us most of what we want to know to see what happens during a
button press. We verify this with a `Salae Logic
Analyzer <http://www.saleae.com/logic/>`__ that I love a lot, and we can
make this block diagram.

|image3|

The logic analyzer also gave us a good quality sample of what the signal
looks like before it is sent to the RF daughter board. In the diagram
above, if you look at the thicker line, this represents the
communication going from the Hynix chip, to the RF daughter board. And
that signal looks like this:

|image4|

What's interesting about this is if you look at it closely, it's has 32
transitions from digital HIGH to digital LOW during a single
transmission. If you split them up into bytes, we now see 4 groups of
data being transmitted. The first group is the sync to tell the device
to listen and is always "0 1011101." The second is a PIN that can be set
to make sure the remote only talks to this device and not other ones.
Basically, this is a passcode that can be anywhere from 000 to 255. The
third group is the button ID. This tells which button is being pressed.
The last group is a verification of the button ID which is done by doing
a bit flip of the previous binary. "00000001" turns into "11111110." So
I created a map of the useful button IDs for later: Power is decimal 30,
volume up is 79, pause is 76, and mysterious "P1" is 14. So if we wanted
to transmit a power button with a pin code of "000" it would look like
this:

01011101 00000000 01111000 10000111

RF RF
=====

One of the reasons this project became fun was because the radio doesn't
transmit on IR. It's RF only. This means that all the amateur radio
operators at Interlock could come to my rescue and explain what was
going on. First we needed to find out what carrier frequency it used. It
turns out that we didn't have to look to far because both the carrier
frequency and the modulation type were in the remote's owners manual!

|image5|

In this case 433.92MHz FSK are for new versions of this device and
27.145MHz are for older. 433.92MHz is in the\ `ISM
band <http://en.wikipedia.org/wiki/ISM_band>`__ and used by a lot of
small electronics like a garage door opener. Our first goal was to
capture a sample of the RF so that we could analyze the data in some
kind of `FFT <http://en.wikipedia.org/wiki/Fast_Fourier_transform>`__.
This would tell us the data inside of the transmission as well as
confirm which type of encoding it was using.
(`FSK <http://en.wikipedia.org/wiki/Frequency-shift_keying>`__,
`ASK <http://en.wikipedia.org/wiki/Amplitude-shift_keying>`__,
`PSK <http://en.wikipedia.org/wiki/Phase-shift_keying>`__, etc)

|image6|

The first attempts to use ham radio equipment were a failure. We later
found out that the equipment could listen on 433.92MHz, but the ham
equipment was listening on too narrow of a bandwidth to correctly
capture the entire signal. The company I work for was happy to lend me
their USRP. Yay!

If you've never heard of a
`USRP <http://en.wikipedia.org/wiki/Universal_Software_Radio_Peripheral>`__,
this is what ham guys normally call a software defined radio, or a radio
that can be a range of frequencies depending on what you program it to
be. You can control things like bandwidth and frequency by sending it a
simple command. The USRP was designed by Ettus Labs and sold to National
Instruments and has become a defacto part of the RF hackers' toolkit.

With this, we were able to get a good sampling of the transmission from
the remote that looked like this:

|image7|

Signal Processing
=================

Putting the RF signal and the data collected from the logic analyzer, we
can now make some conclusions. Namely, that this is an extremely simple
circuit that isn't doing much encoding or modulation when its being
converted to RF. Basically the RF signal that you see above, is the
exact same as the data being sent by the Hynix chip. This will be
important later.

Results
=======

To review we have:

-  reversed the hardware that handles pressing the button
-  captured a sample of the RF signal
-  discovered what data is being transmitted and how

.. raw:: html

   <div>

The next step was to create my own remote from scratch. I did this using
an Arduino and an RF chip designed to transmit on 433.92MHz. Thanks to
Robo Alex for setting this thing up for me. It turns out I don't need
the ground plane which is that giant piece of copper in the picture, but
it doesn't hurt.

.. raw:: html

   </div>

.. raw:: html

   <div>

|image8|

.. raw:: html

   </div>

What this does right now, is transmit on 433.92MHz, whatever button that
I'd like, supplying whatever PIN code that I'd like. When I capture the
data using the USRP, I find that my Arduino kit transmits perfectly at
433.92MHz while the remote has an offset of about 60 hertz so that it
transmits at 433.98Mhz. That's kind of a deal breaker for me right now
and I'm looking for a replacement IC or something else so that I can
transmit on the correct carrier freq. Until then, enjoy this random
data.

|image9|

Defcon
======

If you want to hear more about this (I don't know why you would),
JustBill and I will be presenting this information (and some other
things) at `Defcon <http://www.defcon.org>`__'s
`Skytalks <https://skytalks.info/>`__ next week. If you're going to be
in Vegas for Defcon/Blackhat, look me up. :) For more information,
follow me on `twitter <http://twitter.com/antitree/>`__.

 

.. |image0| image:: /wp-uploads/2012/07/DSC_8657-300x198.jpg
   :class: size-medium wp-image-969 alignnone
   :width: 300px
   :height: 198px
   :target: /wp-uploads/2012/07/DSC_8657.jpg
.. |image1| image:: /wp-uploads/2012/07/DSC_8664-198x300.jpg
   :class: alignnone
   :width: 198px
   :height: 300px
   :target: /wp-uploads/2012/07/DSC_8664.jpg
.. |image2| image:: /wp-uploads/2012/07/hynix_circuit-300x192.png
   :class: aligncenter size-medium wp-image-973
   :width: 300px
   :height: 192px
   :target: /wp-uploads/2012/07/hynix_circuit.png
.. |image3| image:: /wp-uploads/2012/07/HYNIX_chiplayout-246x300.png
   :class: aligncenter size-medium wp-image-964
   :width: 246px
   :height: 300px
   :target: /wp-uploads/2012/07/HYNIX_chiplayout.png
.. |image4| image:: /wp-uploads/2012/07/logic_comparison_IR_DECODE-e1342714104358-300x40.png
   :class: aligncenter size-medium wp-image-975
   :width: 300px
   :height: 40px
   :target: /wp-uploads/2012/07/logic_comparison_IR_DECODE-e1342714104358.png
.. |image5| image:: /wp-uploads/2012/07/CF_manual.png
   :class: aligncenter size-full wp-image-984
   :width: 334px
   :height: 49px
   :target: /wp-uploads/2012/07/CF_manual.png
.. |image6| image:: /wp-uploads/2012/07/DSC_8664-198x300.jpg
   :class: aligncenter size-medium wp-image-972
   :width: 198px
   :height: 300px
   :target: /wp-uploads/2012/07/DSC_8664.jpg
.. |image7| image:: /wp-uploads/2012/07/omfg_iv_had_this_the_whole_time-e1342715544473-300x56.png
   :class: aligncenter size-medium wp-image-963
   :width: 300px
   :height: 56px
   :target: /wp-uploads/2012/07/omfg_iv_had_this_the_whole_time-e1342715544473.png
.. |image8| image:: /wp-uploads/2012/07/IMG_20120707_150902-e1342717151722-300x152.jpg
   :class: aligncenter size-medium wp-image-978
   :width: 300px
   :height: 152px
   :target: /wp-uploads/2012/07/IMG_20120707_150902-e1342717151722.jpg
.. |image9| image:: /wp-uploads/2012/07/usrp-1024x678.jpg
   :class: aligncenter
   :width: 614px
   :height: 407px
   :target: /wp-uploads/2012/07/usrp.jpg
