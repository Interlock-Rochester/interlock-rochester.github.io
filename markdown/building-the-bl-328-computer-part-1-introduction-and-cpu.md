Building the BL-328 Computer: Part 1: Introduction and CPU
==========================================================

date
:   2012-10-16 11:41

author
:   BleuLlama

category
:   Hardware, Projects

slug
:   building-the-bl-328-computer-part-1-introduction-and-cpu

status
:   published

I recently decided to work on a physically small project. I decided to
take the sort of ethics of the classic computer systems from the 1970s,
which by design were considered what we now woud call "homebrew" and
apply them to modern computing. I tried to keep things as stock and
off-the-shelf as possible, so that this was easily reproducible by
others.

To me, building a standard x86 PC from boards is not really in the same
neighborhood of what I wanted to do here.  I want to do something with
the feel of the Apple I for example.  Buying components, making wiring
harnesses, writing firmware to control it, and having the primary user
interface for it be a BASIC environment, much like the home computers of
the 1970s and 1980s.

The name "BL-328" is taken in the same way that the TRS-80 got its name
(**T**andy/**R**adio **S**hack Z**80** based computer.) For this, I went
with "BL" signifying "BleuLlama", the nickname I use for IRC, and "328"
signifying the ATMega 328 AVR microcontroller in the form of an
[Arduino](http://arduino.cc).

I should note that[Ben Heckendorn](http://benheck.com/) recently did a
similar project, which you can [watch his project on The Ben Heck
Show](http://www.element14.com/community/docs/DOC-49215/l/episode-49-see-ben-hecks-pocket-computer-episode).

To follow along with this first step, all you will need for the first
step is an Arduino board, available from
[Adafruit](http://adafruit.com/category/17),
[Sparkfun](https://www.sparkfun.com/categories/103), [Radio
Shack](http://www.radioshack.com/search/index.jsp?kwCatId=&kw=arduino&origkw=arduino&sr=1),
homemade, etc.   The one I'm using is one I bought a few years ago from
Sparkfun, the Arduino
Pro.[![image0](http://interlockroc.wpengine.com/wp-content/uploads/2012/10/2012-09-30-14.38.02-300x224.jpg)](http://interlockroc.wpengine.com/wp-content/uploads/2012/10/2012-09-30-14.38.02.jpg)

This one has the pin header on the right side there which connects to an
FTDI cable to a host computer.  I will also be using this connector to
power the entire system through the use of the FTDI-USB cable, AA
Battery holder, or rechargable battery pack.

To start off, I took "TinyBasic" which had been ported for use on the
Arduino by Michael Field, and I have [since expanded
upon](https://github.com/BleuLlama/TinyBasicPlus)(github project link).
 I have added SD card support with loading and saving, data pin IO, as
well as graphic functions specific to this project, but I'm getting
ahead of myself.

Downloading that project's TinyBasicPlus.ino to the Arduino will give
you a Basic interface with few hundred bytes of program space free.  You
can use the "Serial Monitor" which is bundled with the Arduino IDE to
interact with it.

The Arduino has 13 digital IO pins, some of which can be used for
pseudo-analog output through the use of
[PWM](http://en.wikipedia.org/wiki/Pulse-width_modulation),  as well as
6 analog Input pins, which can also be used for Digital IO.  A simple
program to print out 10 results from Analog input 3, and turn on digital
output 5 is as follows: (Note, that this assumes a new feature of
TinyBasicPlus, "autoconfigure" is enabled)

    10 REM example program

    20 DWRITE 5, HIGH

    30 FOR A = 0 TO 10

    40 b = AREAD 3

    50 PRINT B

    60 NEXT A

You can write programs that will read port pins, write to port pins, and
then load and save to an SD card, if you have FileIO enabled.  The SD
interface I went with from this was the [SeeedStudio SD Card
Shield](http://www.seeedstudio.com/depot/sd-card-shield-p-492.html?cPath=109) which
was reasonably priced at Radio Shack.  It is hard-configured for its
"select" to be on pin 10, which is shown in the TinyBasicPlus.ino file.
 You will need to comment out the \#undef for fileio and SD card
support, and remove the comment for the related \#define.  In its
current state, it uses the SD library included with the Arduino package,
this uses 9k bytes of program space, which is a lot.  I need to find a
smaller SD library.

[![image1](http://interlockroc.wpengine.com/wp-content/uploads/2012/10/2012-09-30-14.38.15-300x224.jpg)](http://interlockroc.wpengine.com/wp-content/uploads/2012/10/2012-09-30-14.38.15.jpg)

Now that this is enabled, the above program could be saved out to the SD
card like so:

    SAVE example1.bas

And then re-loaded later like so:

    LOAD example1.bas

Recently, a feature was added to TinyBasicPlus that lets programs be
autoloaded when you power on.  This is especially useful if you want to
write your program (or programs) in BASIC on the device itself, rather
than through the Arduino IDE in C.  This is accomplished by enabling the
AUTORUN feature in TinyBasicPlus.ino, and by saving your startup program
as "autorun.bas".

You can go a step further and have the end of your program "CHAIN" to
another program.  That is to say, you could have it load and run another
program. eg:

the file "autorun.bas":

    10 PRINT "Hello"

    20 CHAIN "two.bas"

the file "two.bas":

    10 PRINT "World!"

    20 CHAIN "autorun.bas"

This will start up, run the "autorun.bas", which will then load the
"two.bas" program, which will chain to the "autorun.bas" program,
forever.

Enough with the software though.  I'll now get into a bit of the
hardware, namely the power system.

As mentioned before, there are a few ways we can power the system.
 Currently, since the only interaction you have with it is through the
serial port/FTDI interface, you'll have it powered through that, but
once we bring this thing into a standalone configuration, we'll want
battery power.

The first power pack is a 4AA battery pack with a switch that I picked
up from Adafruit. This has the power lines wired to a 6-pin interface
like the FTDI interface has.  This lets me use standard AA batteries
(rechargable or not) to power the device.

[![image2](http://interlockroc.wpengine.com/wp-content/uploads/2012/10/2012-09-30-14.39.24-300x224.jpg)](http://interlockroc.wpengine.com/wp-content/uploads/2012/10/2012-09-30-14.39.24.jpg)

Next up is a USB-based rechargable battery I picked up at the local
supermarket for \$20.  It's a rechargable (Lithium Ion, perhaps?)
battery with Mini USB input for charging, then standard USB for output.
 I could use the FTDI cable off of this, but instead, I decided to make
a tiny adapter so that I can plug it directly in through the same 6 pin
interface:

[![image3](http://interlockroc.wpengine.com/wp-content/uploads/2012/10/2012-09-30-14.38.45-300x224.jpg)](http://interlockroc.wpengine.com/wp-content/uploads/2012/10/2012-09-30-14.38.45.jpg)

I have no idea how long either of these will power the system for.  I'm
guessing a substantial number of hours.  I've also since made a cable
that connects between the battery pack and that header, rather than that
little widget pictured above, which is essentially a USB cord whose
power lines are wired directly to the FTDI connector.

Using the above, you can [hook up an LED to digital pin
5](http://www.ladyada.net/learn/arduino/lesson3.html), and do a version
of the "Blink" program included with Arduino:

the file "autorun.bas":

    10 REM Basic Blinker

    20 DWRITE 5, HIGH

    30 DELAY 500

    40 DWRITE 5, LOW

    50 DELAY 500

    60 GOTO 30

Then, disconnect the FTDI cable, hook up the battery, and it should
blink the LED forever.

That's it for this time.  Soon, we'll convert an old Commodore 64
keyboard into an input device for the computer, add LCD modules for
output, and other goodies so that we'll be able to go standalone and not
need a host computer at all!

 
