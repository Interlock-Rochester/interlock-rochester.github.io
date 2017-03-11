EPROMs And a failed project... for now.
=======================================

date
:   2012-11-07 11:52

author
:   BleuLlama

category
:   Hardware

tags
:   arduino, eprom, failure, hardware, retro

slug
:   eproms-and-failure

status
:   published

One of the things that comes with working on a lot of projects is
failure.  Not everything works.  I've had my share of projects that for
one reason or another, just didn't work out.  Tonight, I worked on one
of these.

[![image0](http://2.bp.blogspot.com/-XJGRCMuyj2o/UJoNvgJQuRI/AAAAAAAAB5s/NPDbRYe7WqE/s640/2012-11-07+02.07.52.jpg)](http://2.bp.blogspot.com/-XJGRCMuyj2o/UJoNvgJQuRI/AAAAAAAAB5s/NPDbRYe7WqE/s1600/2012-11-07+02.07.52.jpg)

For a long time now, I've had some ideas that center around EPROMs.
 I've been using EPROMS since I started getting into arcade machine
collecting.  EPROMs are programmable devices where you can store bytes
of memory in a fairly stable method.  They look like any other
microchip, except that they have a transparent window on the top
(usually quartz, even though it looks like glass).  If you look in the
window, you can see the chip die in there, which I usually think looks
like a tiny tennis court.

The above image shows a few different size.  The one on the right is a
2716, 16 kilobit (2 kilobyte) device.  The one in the middle is a
27C256, 256 kilobit (32 kilobyte) device.

[![image1](http://1.bp.blogspot.com/-I98O53ShKxo/UJoNZzepHdI/AAAAAAAAB5c/aEIHuJ1Qt6A/s320/2012-11-07+02.02.53.jpg)](http://1.bp.blogspot.com/-I98O53ShKxo/UJoNZzepHdI/AAAAAAAAB5c/aEIHuJ1Qt6A/s1600/2012-11-07+02.02.53.jpg)To
use an EPROM, you place it in an eraser, which is usually a ultraviolet
light (often a fluorescent, non-filtered black light tube) with a timer,
for about 10-12 minutes or so.  This sets all of the bits in the device
to 1's.  (0xff hex).

[![image2](http://2.bp.blogspot.com/-1kK5sgB9PnU/UJoNkK2lUHI/AAAAAAAAB5k/5D_oMNYxpl4/s400/2012-11-07+02.04.28.jpg)](http://2.bp.blogspot.com/-1kK5sgB9PnU/UJoNkK2lUHI/AAAAAAAAB5k/5D_oMNYxpl4/s1600/2012-11-07+02.04.28.jpg)

Then you take the chip, and plug it into a programmer.  A computer tells
the programmer what zeroes to write and where, and you end up with a
chip that has a program or some data stored in it, so that it can be
read out later.  Often, the window is then covered up so that they are
not accidentally erased over time from ambient UV light. One data sheet
I read said that 1 week in direct sunlight, or 3 years in normal office
lighting will erase a device.  The programmer above is my Needham's
EMP-10.  It has a 30 pin simm-looking slot on the side with 3 snap-in
cards that configure the programmer pins so that it can handle a variety
of different target device EPROMs.

This process has fascinated me since I started burning ROMs for use in
arcade machines.  This is where this project comes in. I've had a few
thoughts about things to explore here...

First of all, it should be possible to determine which bytes are in
which physical locations on the device by casting a shadow or projecting
an image onto the die from the eraser.  It should be possible to
determine this by projecting different patterns on the die with the UV
erasing light.  Obviously, it has to be well focused; this has to be
quite precise.  A project for another day...

Secondly, I thought a fun project might be to read the pattern produced
by erasing the device.  I would program all zeroes to the EPROM.  The
chip would be plugged into an Arduino, to read the data out of it.  The
Arduino would also control a UV LED or two which would illuminate the
window on the EPROM, erasing it.  It would then alternate between
illuminating the window and reading the content out of it.  The data
pulled out would then be displayed as an image with pixels white if the
content is a '1', and black if it is a '0'.  This should show all white
at the start, and all black at the end, with some amount of dithering in
the middle somehow.

[![image3](http://3.bp.blogspot.com/-bLHjaeRhyTs/UJoNH7rnlMI/AAAAAAAAB5I/UdksQ0NSy0U/s320/2012-11-07+01.58.52.jpg)](http://3.bp.blogspot.com/-bLHjaeRhyTs/UJoNH7rnlMI/AAAAAAAAB5I/UdksQ0NSy0U/s1600/2012-11-07+01.58.52.jpg)

I have a bunch of chips pulled from various electronic gadgets over the
years, and the most prevalent of them was this 2732.  It has a nice
small package, small data size (4 kilobytes), so downloading the content
from it should be fairly quick... and I have a whole lot of them, so if
a few get destroyed in the process, it's no big deal.

[![image4](http://2.bp.blogspot.com/-EHaidC5ynzI/UJqCpZJViSI/AAAAAAAAB6Q/hsr864Oeovc/s400/2012-11-07+12.JPG)](http://2.bp.blogspot.com/-EHaidC5ynzI/UJqCpZJViSI/AAAAAAAAB6Q/hsr864Oeovc/s1600/2012-11-07+12.JPG)

At first I considered hooking this EPROM up directly to the Arduino, but
I need 24 lines to control it.  16 for address to the chip, 8 for data
from the chip.  Not to mention a line to drive the LED.  I could go with
an Arduino Mega, or Due, but I do not own either.  I only really needed
12 of those 16 address lines, which would bring it to 20 IO needed,
which is still more than was available.

[![image5](http://1.bp.blogspot.com/--ywYLtULcPk/UJqCoRfi1xI/AAAAAAAAB6E/PmrjTU_-fxE/s400/2012-11-07+11.JPG)](http://1.bp.blogspot.com/--ywYLtULcPk/UJqCoRfi1xI/AAAAAAAAB6E/PmrjTU_-fxE/s1600/2012-11-07+11.JPG)

I do have a spare [Mayhew Labs Mux
Shield](http://mayhewlabs.com/products/arduino-mux-shield), (mine is a
previous version) so I decided to just run with that.  Unfortunately
this is where the story goes south.  I went from idea to making the
board in one day. I really should have spent more time thinking about
it, and less time being impulsive and just creating the thing.  I was
too excited, incorrectly thinking that I had what I needed for the
project.

I should note that I often enjoy when a project fails.  It really helps
me learn what I did wrong, why it didn't work, and then it's like a
puzzle to figure out how to make it work.  Sometimes, things just get
frustrating and I will shelve a project indefinitely, but often I figure
things out.

I wired up a socket, cobbled together from smaller DIP sockets, onto a
piece of strip board.  I also threw a few indicator LEDs onto the board
for various runtime display. After an evening of work, I came up with
the board as seen here:

[![image6](http://1.bp.blogspot.com/-vcDaSPXWoTg/UJoM13i_plI/AAAAAAAAB44/74-H3Fn2ZvA/s400/2012-11-06+22.50.45.jpg)](http://1.bp.blogspot.com/-vcDaSPXWoTg/UJoM13i_plI/AAAAAAAAB44/74-H3Fn2ZvA/s1600/2012-11-06+22.50.45.jpg)

[![image7](http://3.bp.blogspot.com/-loed2kQYnbY/UJoNDHYXfRI/AAAAAAAAB5A/-sgcl3ynaKI/s400/2012-11-06+22.50.58.jpg)](http://3.bp.blogspot.com/-loed2kQYnbY/UJoNDHYXfRI/AAAAAAAAB5A/-sgcl3ynaKI/s1600/2012-11-06+22.50.58.jpg)

It was wired on the circuit side of the board (I do not recommend this)
because then I could easily plug it in to the Mux Shield using the pin
connectors I had.  The three red LEDs are wired to a few unused port
pins on the mux, and the frosted LED on the right is an amber LED which
I scuffed the top of to make it glow more than illuminate.  I have yet
to power this up, because it was at this point, when I was done building
it that I realized the problem.

The Mux Shield is an excellent device. I use it for my Jasper Box to
read inputs.  For inputs, it's awesome.  It'll do 48 IO, even analog
input.  For output, that's where it gets a bit non-intuitive.

The chips used on it are unbuffered.  That is to say that there's no way
to specifically sample or store data out or in on it.  You pick a line,
and then immediately read or write from it.  Think of it as a valve, not
a view.  This is to say that at any one point in time, you're only
setting or reading one bit.  When reading the EPROM, I want to specify a
single address (16 bits of digital output) then read in the data from
the chip (8 bits of digital input).  I can only do one bit at a time, so
it is impossible to set the 16 bits simultaneously.

In order for this to work, I need to add a latch of some kind to the
circuit to store the 16 bit address, so that I can then read in the 8
bits of data for that address in the EPROM.

[![image8](http://3.bp.blogspot.com/-FDgWE5um2xI/UJqCnxDW4YI/AAAAAAAAB6A/b3ycReA1ZTY/s400/2012-11-07+10.JPG)](http://3.bp.blogspot.com/-FDgWE5um2xI/UJqCnxDW4YI/AAAAAAAAB6A/b3ycReA1ZTY/s1600/2012-11-07+10.JPG)

Here's a sketch for the next version of this project.  As you can see,
instead of using the Mux Shield, I'm now using a pair of [74HC595
serial-in, parallel-out shift
registers](https://www.sparkfun.com/products/733) chained together.  The
idea here is that I would shift in the address I want to read through
both of the '595s, then latch in the data on the [74HC165 parallel-in,
serial-out shift register](https://www.sparkfun.com/products/9519). This
is actually taking it one step too far, since the '165 is unnecessary.
 The thing on the left is the UV LED and its resistor.

 

[![image9](http://2.bp.blogspot.com/-ptkXdzVAcIg/UJqOvYeUR5I/AAAAAAAAB6k/R7b3MIyQJVA/s400/2012-11-07+11.35.20.jpg)](http://2.bp.blogspot.com/-ptkXdzVAcIg/UJqOvYeUR5I/AAAAAAAAB6k/R7b3MIyQJVA/s1600/2012-11-07+11.35.20.jpg)

So here's a simplifed version where the data lines of the EPROM are
hooked directly into the Arduino.  It also shows three indicator LEDs on
the top, which will be used to show the state of the device at runtime.

I need to order some parts to build this, and once I get them, I will be
posting further results on the project.

"Failure is always an option." - Adam Savage
