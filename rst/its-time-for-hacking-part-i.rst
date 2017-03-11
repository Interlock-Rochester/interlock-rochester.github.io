It's time for hacking, part I
#############################
:date: 2011-03-05 21:22
:author: steve
:category: Projects
:slug: its-time-for-hacking-part-i
:status: published

*One of our members, `Steven L Smith <http://stevenlsmith.com/>`__, has
recently been bitten by the clock bug. This post is part I of a
multi-part series on some of his builds.*

*|image0|*\ I’ve been interested in building kits for some time now,
having previously built the
`Theremax <http://www.paia.com/theremax.asp>`__, various small things
from
`Velleman <http://www.vellemanusa.com/us/enu/product/list/?id=523008>`__,
and, most recently, a `morse code practice
oscillator <http://www.morsex.com/ameco/oscs.htm>`__. And, I remember a
place near the central Rochester, NY post office called “\ `Rogers
Pianos and Clocks <https://rocwiki.org/Rogers_Pianos_and_Clocks>`__\ ”
that I have fond memories of visiting and gawking at cool looking
timepieces. So, when I saw the “\ `Ice
Tube <http://www.ladyada.net/make/icetube/index.html>`__\ ” clock kit
from `Adafruit <http://www.adafruit.com/>`__, I knew it would be a great
next project. This ATmega-powered clock features a Russian-made IV-18
`vacuum fluorescent
display <http://en.wikipedia.org/wiki/Vacuum_fluorescent_display>`__
(VFD) tube, which, despite being blue, like modern, `annoying
LEDs <http://www.codinghorror.com/blog/2005/07/blue-led-backlash.html>`__,
is actually really really cool.

 

| 
| |image1|\ After checking to make sure I had all of the components, I
  began the assembly. The first part of the build should be fairly
  standard for anyone who has some electronics experience. All you have
  to do is assemble a simple regulated 5v power supply. Using the
  provided regulator IC, and capacitors to smooth everything out, my 5v
  power supply clocked in at 4.99 volts. Not too shabby.

I continued assembly by adding a single resistor, the piezo speaker, and
finally the ATmega itself (thankfully, Adafruit provided a socket for
all of the ICs, which made the soldering process a lot less stressful!).
At this point, plugging in the power supply resulted in a beep. All is
well.

The kit, in addition to the ATmega, is driven by a 32.768 khz crystal.
The crystal really does the bulk of the timekeeping by generating a
steady reference frequency for the “ticks”. It was good to see Adafruit
use a crystal for this clock; I think it’s going to stay accurate for a
long time as a result.

Now it’s time for the fun stuff. Unlike, say, an LCD screen, or some
LEDs, this clock needs around 60 volts to run its vacuum tube properly.
But we’ve only got 5. So, we build a boost converter. After assembly, I
used the multimeter to measure 55.7 vdc across the zener diode. The
kit’s instructions say that anywhere from 40 - 70 is okay, with 60 being
optimal. I’m not thrilled with that number, but it seems like it’s close
enough. We’re working with high voltages here. Since I don’t feel like
taking advantage of Interlock’s insurance policy, I give the capacitors
time to drain, and, as the instructions suggest, do not work on the
circuit until we’re below 15 volts.

Th\ |image2|\ e VFD goes on a smaller PCB, and coaxing it down into
place was a frustrating experience, not unlike wiring an 8P8C ethernet
cable, except bigger, and with a lot more leads. After about 20 minutes
of carefully walking the leads through the holes, I was able to get the
tube in place. I soldered it in, plugged in the other microcontroller
(MAX6921) which actually drives the VFD segments. And... it passed the
smoke test.

The remainder of the build consisted of putting in a battery backup (in
case mains power is lost), adding a few control switches, and building a
simple, clear case. All in all, it was a fun build, and I feel like my
patience was rewarded.

 

 

 

In the coming weeks, I plan on building two more clocks of various
types. Check back here for updates!

 

Additional pictures of the build:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

[caption id="attachment_382" align="alignnone" width="300" caption="All
components, before starting assembly. Note that the blackened spot on
the tube is normal."]\ |image3|\ [/caption]

[caption id="attachment_386" align="alignnone" width="300" caption="VFD
Tube, as shipped."]\ |image4|\ [/caption]

[caption id="attachment_379" align="alignnone" width="300"
caption="Vacuum Tube fed through PCB"]\ |image5|\ [/caption]

[caption id="attachment_387" align="alignnone" width="300"
caption="Timing circuitry, including the ATmega and
crystal"]\ |image6|\ [/caption]

[caption id="attachment_381" align="alignnone" width="300"
caption="Bare Clock, without Case"]\ |image7|\ [/caption]

[caption id="attachment_383" align="alignnone" width="300" caption="The
assembled clock. Yay!"]\ |image8|\ [/caption]

.. |image0| image:: {filename}wp-uploads/2011/03/dark-adjusted-300x224.jpg
   :class: alignright size-medium wp-image-392
   :width: 240px
   :height: 179px
   :target: {filename}wp-uploads/2011/03/dark-adjusted.jpg
.. |image1| image:: {filename}wp-uploads/2011/03/2011-03-05_16-55-00_706-300x224.jpg
   :class: size-medium wp-image-378 alignright
   :width: 300px
   :height: 224px
   :target: {filename}wp-uploads/2011/03/2011-03-05_16-55-00_706.jpg
.. |image2| image:: {filename}wp-uploads/2011/03/2011-03-05_19-20-52_474-300x224.jpg
   :class: alignleft size-medium wp-image-379
   :width: 300px
   :height: 224px
   :target: {filename}wp-uploads/2011/03/2011-03-05_19-20-52_474.jpg
.. |image3| image:: {filename}wp-uploads/2011/03/components-300x224.jpg
   :class: size-medium wp-image-382
   :width: 300px
   :height: 224px
   :target: {filename}wp-uploads/2011/03/components.jpg
.. |image4| image:: {filename}wp-uploads/2011/03/bare_tube-300x224.jpg
   :class: size-medium wp-image-386
   :width: 300px
   :height: 224px
   :target: {filename}wp-uploads/2011/03/bare_tube.jpg
.. |image5| image:: {filename}wp-uploads/2011/03/2011-03-05_19-20-52_474-300x224.jpg
   :class: size-medium wp-image-379
   :width: 300px
   :height: 224px
   :target: {filename}wp-uploads/2011/03/2011-03-05_19-20-52_474.jpg
.. |image6| image:: {filename}wp-uploads/2011/03/timing-300x224.jpg
   :class: size-medium wp-image-387
   :width: 300px
   :height: 224px
   :target: {filename}wp-uploads/2011/03/timing.jpg
.. |image7| image:: {filename}wp-uploads/2011/03/bare_clock-300x224.jpg
   :class: size-medium wp-image-381
   :width: 300px
   :height: 224px
   :target: {filename}wp-uploads/2011/03/bare_clock.jpg
.. |image8| image:: {filename}wp-uploads/2011/03/assembled-300x224.jpg
   :class: size-medium wp-image-383
   :width: 300px
   :height: 224px
   :target: {filename}wp-uploads/2011/03/assembled.jpg
