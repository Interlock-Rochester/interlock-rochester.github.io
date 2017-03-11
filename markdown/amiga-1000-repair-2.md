Amiga 1000 Repair
=================

date
:   2012-10-17 10:23

author
:   BleuLlama

category
:   Hardware

tags
:   amiga, repair, retro computing

slug
:   amiga-1000-repair-2

status
:   published

  -------------------------------------------------------------------
  [![image0](http://4.bp.blogspot.com/-_QFAx9A8wgI/UH7Dhk3QsGI/AAAAAA
  AABsU/S9Sr8gFkLq4/s640/IMG_0544.JPG)](http://4.bp.blogspot.com/-_QF
  Ax9A8wgI/UH7Dhk3QsGI/AAAAAAAABsU/S9Sr8gFkLq4/s1600/IMG_0544.JPG)

  Amiga 1000 computer (1985) with an Amiga 3000 "pregnant" mouse.
  -------------------------------------------------------------------

One of the fun things about owning retro computers is that you get to
repair them yourself. (Perhaps this isn't a fun thing for some of you,
but I really enjoy it.)

About 6 years ago, my Amiga 1000 started showing some strange behaviors
but only in the green levels of the video.  If you dragged the green
slider, instead of it stepping up gradually from dark to bright, it
would get brighter, darker, brighter, darker, much brighter, a little
darker than that, and so on.

 

About 5 years ago, I had opened it up and replaced two '244 latches in
the video output section.  I kinda did this blindly by looking at the
schematic...

+--------------------------------------------------------------------------+
| [![image1](http://4.bp.blogspot.com/-8rNHmjvwHLo/UH7HWb-166I/AAAAAAAABtY |
| /AIYo8RwFBsM/s640/Denise-out.gif)](http://4.bp.blogspot.com/-8rNHmjvwHLo |
| /UH7HWb-166I/AAAAAAAABtY/AIYo8RwFBsM/s1600/Denise-out.gif)               |
+--------------------------------------------------------------------------+
| Video output circuit on the A1000 -- Left to right:                      |
|                                                                          |
| Denise coprocessor, '244 latches, resistor ladders, and output           |
| transistors.                                                             |
+--------------------------------------------------------------------------+

...and replacing the two latches, assuming that one of them had gone
bad.  After doing the repair, the problem persisted and I just gave up
on it for a while.

+--------------------------------------------------------------------------+
| [![image2](http://3.bp.blogspot.com/-0xu4SI6DgCw/UH7DiVA7OzI/AAAAAAAABsc |
| /Dqd9vDBDA2E/s400/IMG_0546.JPG)](http://3.bp.blogspot.com/-0xu4SI6DgCw/U |
| H7DiVA7OzI/AAAAAAAABsc/Dqd9vDBDA2E/s1600/IMG_0546.JPG)                   |
+--------------------------------------------------------------------------+
| Green section is at the top.                                             |
|                                                                          |
| The two '244 latches are now socketed and replaced.                      |
+--------------------------------------------------------------------------+

A few days ago, a comment on the above video re-sparked interest in this
project and I decided to bring the Amiga over
to [Interlock](http://interlockroc.org/) and really get to the bottom of
the problem. I hooked it up to a scope and followed the paths according
to the schematics.

  --------------------------------------------------------------
  [![image3](http://3.bp.blogspot.com/-BGRmTKCir9A/UH7Dk_Ln6tI/A
  AAAAAAABs0/CZfwXU_-m0E/s640/IMG_0549.JPG)](http://3.bp.blogspo
  t.com/-BGRmTKCir9A/UH7Dk_Ln6tI/AAAAAAAABs0/CZfwXU_-m0E/s1600/I
  MG_0549.JPG)

  Amiga 1000 apart, hooked up to a scope and a LCD monitor.
  --------------------------------------------------------------

The video circuit is on the left edge of the board, just under the power
cable.

I traced the lines from input on Q2 (where all of the four resistors in
the D-to-A resistor ladder are joined, and back through to the latch,
and then continuing back to the Denise video generation coprocessor.

[![image4](http://4.bp.blogspot.com/-Z9jwp8H9SmI/UH7Dj99trmI/AAAAAAAABss/JmJd8sqc1C0/s400/IMG_0548.JPG)](http://4.bp.blogspot.com/-Z9jwp8H9SmI/UH7Dj99trmI/AAAAAAAABss/JmJd8sqc1C0/s1600/IMG_0548.JPG)

<div>
I tried jumpering across various portions of the resistor ladder to try
to track down exactly where the issue was.  It gave some pretty
interesting results, but really only helped me track down where the
issue is.  I eventually came to the realization that something on the
R55 data path was drawing it down to ground, or at least close to
ground. (Where the left alligator clip is attached in the above
picture.)

</div>
+--------------------------------------------------------------------------+
| [![image5](http://1.bp.blogspot.com/-mcGHDzgkU68/UH7DjXgwZYI/AAAAAAAABsk |
| /aphCXSC7ANY/s400/IMG_0547.JPG)](http://1.bp.blogspot.com/-mcGHDzgkU68/U |
| H7DjXgwZYI/AAAAAAAABsk/aphCXSC7ANY/s1600/IMG_0547.JPG)                   |
+--------------------------------------------------------------------------+
| The "Green" section of the video generation circuit in                   |
|                                                                          |
| the Amiga 1000 with notes                                                |
+--------------------------------------------------------------------------+

<div>
I tried pulling out the pins on the Denise's G1 output (pin 29) and
soldering it directly to pin 15 of U6A, and it didn't change anything.
 I then pretty much realized that the issue was on the other side of U6A
-- the connection between pin 5 of U6A and the left side of R55 (4k
resistor).  I decided to leave the above wire "flying" and pulled the
resistor leg, soldering it directly to pin 5 of U6A.

</div>
[![image6](http://2.bp.blogspot.com/-a3ejuzXFvlE/UH7Dm8-OTcI/AAAAAAAABtE/vTafHBGflXY/s640/IMG_0565.PNG)](http://2.bp.blogspot.com/-a3ejuzXFvlE/UH7Dm8-OTcI/AAAAAAAABtE/vTafHBGflXY/s1600/IMG_0565.PNG)

<div>
This did the trick!  It worked.  I probably could have restored the
flying wire back to the original traces on the board, desoldering the
wire, re-seating the chips, but I had flexed those pins in and out a
lot, and decided to not stress out the pins anymore, and just leave it.
 -- "It works... don't touch it!"

After 5 years of it sitting on a shelf, my trusty 'ol Amiga, my favorite
computer, is finally is working again!

(This post has been cross posted from my personal blog here:[Scott's
Project Blog: Amiga
Repaired!](http://geodesicsphere.blogspot.com/2012/10/amiga-1000-repaired.html))

 

</div>

