Eproms and SUCCESS!
===================

date
:   2012-11-14 23:59

author
:   BleuLlama

category
:   Projects

slug
:   eproms-and-success

status
:   published

This is a continuation of a [previous
article](http://interlockroc.org/2012/11/07/eproms-and-failure/).  Quick
summary: I tried to build a device for dumping an EPROM via Arduino, and
I constructed a device that had no chance of working.  Oops.

This post will continue where that one left off.  I'll walk through some
of the process to hopefully get to a solution that works...

[![image0](http://4.bp.blogspot.com/-yjVkgyfT8Ao/UKHVQYVDczI/AAAAAAAAB78/5ApnGVPQ5Z8/s320/2012-11-12+23.56.10.jpg)](http://4.bp.blogspot.com/-yjVkgyfT8Ao/UKHVQYVDczI/AAAAAAAAB78/5ApnGVPQ5Z8/s1600/2012-11-12+23.56.10.jpg)

To summarize the overall project;  I want to build a device that will
illuminate an UV light-erasable ROM (EPROM) device, and also dump out
its contents. I will then take the contents, display them as a graphic,
and animate them over time as the bits fade away into an erased
oblivion.

[![image1](http://2.bp.blogspot.com/-ptkXdzVAcIg/UJqOvYeUR5I/AAAAAAAAB6k/R7b3MIyQJVA/s400/2012-11-07+11.35.20.jpg)](http://2.bp.blogspot.com/-ptkXdzVAcIg/UJqOvYeUR5I/AAAAAAAAB6k/R7b3MIyQJVA/s1600/2012-11-07+11.35.20.jpg) When
we last left this, the above circuit was what I was going to work with.
 The Arduino would shift out a 16 bit address, which will be stored in
the 74HC595 serial-in, parallel-out shift registers.  Those would out I
was all set to place the order, but then I started thinking about other
ways to sample the data, and then it hit me...

In the late 1980s, I had an Amiga 1000 computer (see previous post about
restoring it).  We used Macintosh SE computers in High School, and as a
result, we bought the ["AMAX" Macintosh emulation system for the
Amiga](http://crossconnect.tripod.com/AMAXHIST.HTML).  It was a lot
easier to carry a floppy or two, rather than a SE or SE/30 in a plastic
milk crate, not to mention that MacWrite was a substantially better word
processor than TextCraft. ;)

AMAX consisted of software you run that emulated the Mac's hardware, as
well as a "cartridge" that plugged into the floppy drive port of the
Amiga.  I remember hearing that they went with the floppy drive port
because it was the only appropriate port identical on all Amigas that
were available at the time. (Amiga 1000, 500, 2000).

The cartridge served two functions. First, it let you plug in a Mac
floppy drive right into the Amiga so that you could read and write 800k
Mac floppies directly.  There was something about Amiga drives and Mac
drives supporting a different number of drive speeds, so full
Mac compatibility on the Amiga's drives was directly impossible.  Future
versions of AMAX that used an internal card on the Amiga 2000 worked
around this issue.  It was possible to make a floppy that supported just
the sectors/speeds that were the same on both, but they only stored 272k
of content.  But I digress...

The other function of the cartridge was that you needed to plug in Mac
roms into it, which the software would read in as it starts.  Rather
than storing the ROM on the Amiga, this protected the copyrights or
whatever.  But the important thing here is the function.  I had picked
up a few AMAX cartridges for \$2 apiece at the awesome [Active Surplus
on Queen Street in Toronto](http://www.activesurplus.ca/en/) a bunch of
years back, so I dug one out.

[![image2](http://2.bp.blogspot.com/-7Q7anY45dnM/UJyUgpiEVAI/AAAAAAAAB7M/U3p_sw6izzM/s640/2012-11-08+22.59.34.jpg)](http://2.bp.blogspot.com/-7Q7anY45dnM/UJyUgpiEVAI/AAAAAAAAB7M/U3p_sw6izzM/s1600/2012-11-08+22.59.34.jpg)

Left-to-Right, you see: Amiga D23 floppy connector, for connecting it to
your Amiga, two 28 pin rom sockets, two 74LS393s, one 74LS165, a
resistor, some diodes, a 74LS139, the Mac D19 floppy connector on the
bottom, then the Amiga D23 floppy connector for adding additional Amiga
floppy drives.

[![image3](http://4.bp.blogspot.com/-18w4vJIID1g/UJyU1jLxhdI/AAAAAAAAB7c/kg4tRl3TVUk/s640/2012-11-08+23.53.05.jpg)](http://4.bp.blogspot.com/-18w4vJIID1g/UJyU1jLxhdI/AAAAAAAAB7c/kg4tRl3TVUk/s1600/2012-11-08+23.53.05.jpg)

I've started to trace out the circuit, but it became obvious quickly
that it was optimized for board layout rather than what I would consider
to be a sane arrangements of data lines.  For example the 8 data output
lines of the ROMs go into the 74LS165 PISO shift register out of order,
so they need to be reshuffled once captured in the host computer.

Instead I decided to desolder the chips!  My guess at the original
function is something like: the Amiga issues a clear to the 74LS393
binary counter chips, ganged together to yeield a 16 bit output, rather
than two dual-4 bit outputs.  This will reset their 16 bit output value
to 0.  The 74LS165 parallel-in, serial-out register then latches the 8
bit output from the ROM, and provides it through shifting to the Amiga
via the floppy port.  From there, you need to simply pulse the clock on
the '393, and it will increment through every address. Then you just
latch and shift in the data. There's also a 74LS139 demultiplexer, which
might be responsible for sequencing through those events, or perhaps
something to do with the Mac floppy drive. I had a slight mishap and
lost the 74LS165, which is okay since I didn't need it for this project
anyway.  Regardless, \$2 plus some time -- I'm already ahead and I
haven't even removed the D23s yet (which are the same size as Amiga RGB
Video connectors! Perfect for another project...)

[![image4](http://1.bp.blogspot.com/-yKqJsMVndpk/UJyU-0ld6vI/AAAAAAAAB7k/ytWr1Yz9T1A/s640/2012-11-08+23.54.08.jpg)](http://1.bp.blogspot.com/-yKqJsMVndpk/UJyU-0ld6vI/AAAAAAAAB7k/ytWr1Yz9T1A/s1600/2012-11-08+23.54.08.jpg)

For fun, here's the board with no components on it.

[![image5](http://2.bp.blogspot.com/-yPhGkww2fo0/UJx-TvHFDFI/AAAAAAAAB64/ZW5j5cNhgYY/s320/2012-11-08+21.56.26.jpg)](http://2.bp.blogspot.com/-yPhGkww2fo0/UJx-TvHFDFI/AAAAAAAAB64/ZW5j5cNhgYY/s1600/2012-11-08+21.56.26.jpg) With
a slight change in gears I can adapt my design to use the parts I now
have in my toolbox thanks to my desoldering tools.  Instead of the
Arduino shifting out an address, it will instead do the process
described above.  It will first clear the 393s, then alternately cycle
between clocking out a pulse to increment their values, and reading in
the value directly. Since I'm accessing the ROM data from start to
finish, sequentially anyway, this solution works out perfectly.  I also
show four LEDs in the above diagram. Three for various status, one for
UV illumination.

[![image6](http://3.bp.blogspot.com/-cWIzW2S6maY/UKPpxw8t2JI/AAAAAAAAB9I/0FMuEhfRqEg/s640/2012-11-13+22.30.40.png)](http://3.bp.blogspot.com/-cWIzW2S6maY/UKPpxw8t2JI/AAAAAAAAB9I/0FMuEhfRqEg/s1600/2012-11-13+22.30.40.png)

Here is a close up of a 27C128 part. This one has Pac-Man programmed
onto it... of course.  You can see through the quartz window, and down
onto the EPROM silicon itself.

[![image7](http://4.bp.blogspot.com/-Nkxzmx4wLjA/UKRyi43rfVI/AAAAAAAAB9g/KBX-JvT5krk/s400/2012-11-14+23.16.29.jpg)](http://4.bp.blogspot.com/-Nkxzmx4wLjA/UKRyi43rfVI/AAAAAAAAB9g/KBX-JvT5krk/s1600/2012-11-14+23.16.29.jpg)

Here we see the pins on the Arduino, and how the connect to the shield's
bus connections, along with the LEDs.  I could draw this up in a
computerey drawing program, but sketching it out in Sharpie on graph
paper is just quicker... and more Mimsian. ;)

[![image8](http://1.bp.blogspot.com/-A1qXIZxizuU/UKRyoHy1G0I/AAAAAAAAB9o/y9jV7rs69_0/s400/2012-11-14+23.16.36.jpg)](http://1.bp.blogspot.com/-A1qXIZxizuU/UKRyoHy1G0I/AAAAAAAAB9o/y9jV7rs69_0/s1600/2012-11-14+23.16.36.jpg)

Here are the  two 74LS393's.   You can see their connection to the
address lines on the ROM, as well as the cascading of the counter, e.g.
from 1QD to 2A, and from 2QD to 1A on the second chip.

[![image9](http://4.bp.blogspot.com/-ouX_QPqw_mU/UKRyskKJwEI/AAAAAAAAB9w/LgIR8UIhkcc/s400/2012-11-14+23.16.44.jpg)](http://4.bp.blogspot.com/-ouX_QPqw_mU/UKRyskKJwEI/AAAAAAAAB9w/LgIR8UIhkcc/s1600/2012-11-14+23.16.44.jpg)

And the wiring for the 28 pin socket, including the 3 pin (two-way)
jumper so that i can use smaller 24 pin parts as well.

 

About the UV illumination...  The data sheets for the EPROMs show that
they should be erased with 253.7 nanometer light, at 15-20 minutes,
2.5cm distance at 15 Watt/seconds per cm\^2.  I dont know how to measure
this with respect to LEDs, but I'm going to just wing it and see what
happens.  The sheet also says that 253.7nm is the optimal wavelength for
erasing them, but anything below 400nm should work.  I believe the UV
LEDs I have are somewhere between 350nm and 400nm, so it should work.
 The other issue is that the LEDs are substantially less powerful,
probably a tenth to a hundredth the power. We'll see once we get this
going, but I expect it will take on the order of weeks to erase a rom,
rather than minutes.

 

The good thing about this project, in comparison to using EPROMs
functionally, is that you want speed of erasure for functional use.  I
personally found that my eraser worked on most of the devices I own in
about 10 minutes.  I would often have a chip or two in the eraser, while
programming and debugging others.  It worked out fairly well.  For this
project, it's completely okay if it takes on the order of hours to erase
a device.  I'll find out how well it works once I get it going.  I may
use more than one LED just to speed it up a little, in case it takes on
the order of days instead of minutes or hours.

[![image10](http://2.bp.blogspot.com/-7pdS0XmtszQ/UKPeqW1OBtI/AAAAAAAAB8Q/s9vl4QBZE_U/s400/2012-11-10+00.56.30.jpg)](http://2.bp.blogspot.com/-7pdS0XmtszQ/UKPeqW1OBtI/AAAAAAAAB8Q/s9vl4QBZE_U/s1600/2012-11-10+00.56.30.jpg)

I started laying out the board at home, wiring in just the LEDs, and
figuring out the best layout for the chips.  I used the[ DIY shield for
Arduino from AdaFruit.com](https://www.adafruit.com/products/187) as the
foundation to build this upon.  I wanted to leave space for possibly
using larger chips in the future, so what is the bottom of the board
here has space for a few extra data lines if i re-route that red power
line.  The '393's are layed out so that the one on the right, which
addresses bits A0-A7 has four of its lines directly lined up.  This was
to try to make it a little easier to wire up.

 

[![image11](http://2.bp.blogspot.com/-6xhutFXwlfI/UKPfE_04XSI/AAAAAAAAB8g/h03Dg45PIk0/s320/2012-11-14+02.07.22.jpg)](http://2.bp.blogspot.com/-6xhutFXwlfI/UKPfE_04XSI/AAAAAAAAB8g/h03Dg45PIk0/s1600/2012-11-14+02.07.22.jpg)[![image12](http://3.bp.blogspot.com/-3Ob_H7OLtbM/UKPfD_4KspI/AAAAAAAAB8Y/IVNUHdtJAkk/s320/2012-11-14+00.00.38.jpg)](http://3.bp.blogspot.com/-3Ob_H7OLtbM/UKPfD_4KspI/AAAAAAAAB8Y/IVNUHdtJAkk/s1600/2012-11-14+00.00.38.jpg) I
bought some wire wrap wire for address, data, and control lines, and did
most of the work of wiring those up [one evening at
Interlock](http://interlockroc.org/).  I used red for control (counter
clear, clock data cascade lines) as well as eprom address lines.  I used
blue for data lines.  In the above pictures you can see how the wires
were routed around (there was some more writing on the bottom,
obviously.) You can also see how the UV LEDs are mounted with some stiff
solid core wire.  I reduced the number of LEDs to two plus the UV LEDs
for no real reason at all.  (There is an Arduino underneath there
somewhere...)

On the two images above, you can see a jumper on the left of the first
image, bottom of the second image... this changes what one pin is used
for.  For smaller EPROMs, pin 26 of the 28 pin footprint is used for
VCC, powering the chip.  In the larger packages, VCC is moved to pin 28,
and pin 26 is used for Address line 13.  It's confusing.  [A table that
shows all of the
pinouts](https://docs.google.com/spreadsheet/ccc?key=0Ah_ZDi13ZcngdFlfcDJHWERpNUVGMlBYR0dvdE1kdnc) doesn't
really help too much, but it was necessary so that I could figure things
out for wiring it up.

[![image13](http://2.bp.blogspot.com/-YTbYoRlJDnQ/UKPfF034T1I/AAAAAAAAB8s/NsEVhDXgH9M/s400/2012-11-14+02.17.32.png)](http://2.bp.blogspot.com/-YTbYoRlJDnQ/UKPfF034T1I/AAAAAAAAB8s/NsEVhDXgH9M/s1600/2012-11-14+02.17.32.png) Next
is firmware. I wrote a [pretty simple program for the
Arduino](http://www.umlautllama.com/rand/ROM-Project-Arduino.txt) that
simply enables the EPROM, resets the counters, then clocks through the
addresses, reads them in and sends that data down through the serial
link.  After getting the enable lines wrong (active low, rather than
active high), I managed to get it spitting out actual accurate ROM
contents.  As you can see in the above, it read out of the ROM (right
half) 0xf3, 0x3e, 0x00, and so on.  In a disassembly of Ms PacMan on the
left, you can see these bytes in cyan, just to the right of the red
numbers 0000, 0001, and so on.

The other half is a simple program that runs on a host computer that
simply reads in serial data and logs it out to a file.  That content
looks like this:

> f33e00ed47c30b23772310fcc9c30e07060708090a0b0c0d0e0f101114f532c038002a804c702c712c20022ec022804c3aaf4e324a503aec4ea73aef4e20033ae187d75f2356ebe9e146234e23e51812
>
> f33e00ed47c30b23772310fcc9c30e07060708090a0b0c0d0e0f101114f532c038002a804c702c712c20022ec022804c3aaf4e324a503aec4ea73aef4e20033ae187d75f2356ebe9e146234e23e51812
>
> f33e00ed47c30b23772310fcc9c30e07060708090a0b0c0d0e0f101114f532c038002a804c702c712c20022ec022804c3aaf4e324a503aec4ea73aef4e20033ae187d75f2356ebe9e146234e23e51812

[![image14](http://2.bp.blogspot.com/-OYirbnzlXVU/UKPfFdG641I/AAAAAAAAB8o/O49VdePngmo/s400/2012-11-14+02.08.15.jpg)](http://2.bp.blogspot.com/-OYirbnzlXVU/UKPfFdG641I/AAAAAAAAB8o/O49VdePngmo/s1600/2012-11-14+02.08.15.jpg)

<div>
I've now had this running for 12 hours with no change in the bits at
all.  I'm thinking that it will require running for upwards of a week or
two to have any affect on bits.  I may need to just drop the Arduino and
ROM shield into my eraser to get the results I'm looking for... or at
least a "control" to prove that the idea has a chance of working from
here.

</div>
<div>
If nothing else, I now have a way to read EPROMS from an Arduino.
 Awesome!

</div>

