Repairing the audio on a Pac-Man arcade board
#############################################
:date: 2014-02-12 11:06
:author: BleuLlama
:category: Hardware, Projects
:slug: repairing-the-audio-on-a-pac-man-arcade-board
:status: published

I got this knockoff JAMMA Ms Pac-Man arcade board many years back.  It's
got two ROMs instead of the authentic board's 6 (9 for Ms Pac), and is
substantially smaller than the "real thing".  The only issue is that the
audio is poor... REALLY poor.  It makes sounds but they're... wrong and
noisy.

|image0|

I took over some desk space at Interlock and got to work.  (I should
note that the beverages you can see here are other people's, not mine.
;)

I traced the audio circuit on a real Pac-Man schematic (seen on my
laptop's monitor), and buzzed it out on the Yenox board to try to
corrolate the two.

|image1|

I had to trace four similar paths from a quad flip-flop, through a quad
bidirecional switch, to the audio output.  It got really confusing at
times, and took me probably a bit longer than it should have.  For the
most part, they were pin-for-pin correct as far as how they were wired.
 These chips have the same device (eg, a flip flop, or a logic gate)
repeated 4 or 6 times.  In some cases here, the Yenox board had a
different one of these devices hooked up, which added to the confusion.

This portion of the circuit uses 8 resistors to make a digital-to-analog
converter. These generally work by having different resistance levels,
usually something like multiples of eachother, eg,  10k ohm, 22k ohm,
47k ohm then 100kohm.  I traced out all of the lines on the Yenox board
and I found out that not only were the resistors in the wrong order on
the board, but they were also wildly wrong (47 ohm instead of 4.7k ohm),
which you can see in this table I made:

|image2| 

|image3|

You can see these resistors here on the Yenox board, right next to the
JAMMA connector.  They start from the left with R1 (my notation.)  The
printing on the board completely matched the resistance values that sat
on them, so it's obvious that the engineer who made this board seriously
screwed it up in the design stage.

|image4|

I replaced resistors R3 - R7.  I put them in with the gold band closer
to the JAMMA connector, rather than the other way around.

And now it sounds near-perfect.  There's a little bit of popping left,
but I was getting tired and decided to head home for the night.  I'll
hook it up to an oscilloscope at some point and see if i can figure out
which line is causing problems.

For what it's worth, I also did the same as this on the video path DAC,
seen in the above picture as the next three groups of resistors.  In the
above, the group of four and then the group of five are for audio, then
the next group of three is for the "red", next three for "green", next
two for "blue", and the remaining two are for the sync.  Again, there
were some 47 ohm resistors mixed in, and notice two of the three in the
"green" section are identical (red-red-brown)... which is surely wrong.
 Color is now perfect on the board too!

.. |image0| image:: https://images-blogger-opensocial.googleusercontent.com/gadgets/proxy?url=http%3A%2F%2F2.bp.blogspot.com%2F-s8GO4HSgKUU%2FUuqe6gx2UoI%2FAAAAAAAACp8%2F8kG4H9-mZYo%2Fs1600%2F2014-01-28%2B22.59.08.jpg&container=blogger&gadget=a&rewriteMime=image%2F*
   :class: aligncenter
   :width: 640px
   :height: 480px
   :target: http://2.bp.blogspot.com/-s8GO4HSgKUU/Uuqe6gx2UoI/AAAAAAAACp8/8kG4H9-mZYo/s1600/2014-01-28+22.59.08.jpg
.. |image1| image:: https://images-blogger-opensocial.googleusercontent.com/gadgets/proxy?url=http%3A%2F%2F3.bp.blogspot.com%2F-9SZwuigjePY%2FUuqihQhaOqI%2FAAAAAAAACqc%2FlyX0wtzBBfg%2Fs1600%2F2014-01-30%2B14.05.06.jpg&container=blogger&gadget=a&rewriteMime=image%2F*
   :class: aligncenter
   :width: 480px
   :height: 640px
   :target: http://3.bp.blogspot.com/-9SZwuigjePY/UuqihQhaOqI/AAAAAAAACqc/lyX0wtzBBfg/s1600/2014-01-30+14.05.06.jpg
.. |image2| image:: https://images-blogger-opensocial.googleusercontent.com/gadgets/proxy?url=http%3A%2F%2F3.bp.blogspot.com%2F-Nnjo_5_2VUc%2FUuqe6k2NJxI%2FAAAAAAAACp4%2FFf-1Iqri6Bo%2Fs1600%2F2014-01-28%2B23.07.43.jpg&container=blogger&gadget=a&rewriteMime=image%2F*
   :class: aligncenter
   :width: 480px
   :height: 640px
   :target: http://3.bp.blogspot.com/-Nnjo_5_2VUc/Uuqe6k2NJxI/AAAAAAAACp4/Ff-1Iqri6Bo/s1600/2014-01-28+23.07.43.jpg
.. |image3| image:: https://images-blogger-opensocial.googleusercontent.com/gadgets/proxy?url=http%3A%2F%2F2.bp.blogspot.com%2F-zeQMG0ohkqA%2FUuqe8kFdqkI%2FAAAAAAAACqQ%2FSZjMuEWZ7aI%2Fs1600%2F2014-01-28%2B23.07.59.jpg&container=blogger&gadget=a&rewriteMime=image%2F*
   :class: aligncenter
   :width: 640px
   :height: 480px
   :target: http://2.bp.blogspot.com/-zeQMG0ohkqA/Uuqe8kFdqkI/AAAAAAAACqQ/SZjMuEWZ7aI/s1600/2014-01-28+23.07.59.jpg
.. |image4| image:: https://images-blogger-opensocial.googleusercontent.com/gadgets/proxy?url=http%3A%2F%2F4.bp.blogspot.com%2F-MRXGr6YFnAI%2FUuqe7IEuznI%2FAAAAAAAACqA%2FCEcTI-WDWrg%2Fs1600%2F2014-01-29%2B00.00.35.jpg&container=blogger&gadget=a&rewriteMime=image%2F*
   :class: aligncenter
   :width: 640px
   :height: 480px
   :target: http://4.bp.blogspot.com/-MRXGr6YFnAI/Uuqe7IEuznI/AAAAAAAACqA/CEcTI-WDWrg/s1600/2014-01-29+00.00.35.jpg
