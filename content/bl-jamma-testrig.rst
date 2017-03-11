Updating my JAMMA test rig
##########################
:date: 2014-01-30 19:57
:author: BleuLlama
:category: Hardware, Projects
:slug: bl-jamma-testrig
:status: published

|image0|

Many years back, I hooked up a spare JAMMA harness to an old PC power
supply, a monitor and some repurposed joystick pads.  (JAMMA is a
standard connector size and pinout to hook up arcade game boards into
arcade cabinets.  Most of my arcade game boards are either natively
Jamma (Mortal Kombat, Klax, Block-out) or I have adapters to hook them
up using JAMMA.  (Dig-Dug, Pac-Man, etc)).  One board that I've been
using with it recently is a knockoff Ms. Pac-Man board, seen in these
photos.

Being that I've been wanting to work on arcadey projects recently at
Interlock, I decided to make this thing a lot less janky.

|image1|

The harness/rig I have was always kind of a hack.  The video and audio
wires terminated in a small box with some knobs which were meant to
attenuate the signal but never really worked right.  The power switch
was on this cord that came out and was weirdly fastened to the side of
the power supply.  I decided to clean this up while
at \ `Interlock <http://interlockroc.org/>`__ for open night.

|image2| 

It turns out that I happened to have the right 6 pin DIN
connector for this old RGB monitor (basically a Commodore Amiga 1084
clone).   So I wired up Red, Green, Blue, and Ground directly to the
correct pins on it.  JAMMA spits out composite video, but this monitor
takes in Horizontal and Vertical sync.  I knew that some monitors would
take in composite sync on their Vertical Sync line, so I tried that...
and it worked! Huzzah.

The only video issue now is that the game boards put out video that's
slightly too hot/too high a voltage, so I should put attenuation
resistors inside the din connector or something...

Even though the JAMMA interface spits out amplified audio, I decided to
hook up an RCA plug on the audio lines anyway, to plug it into the
line-level in on the monitor.  As long as I'm careful it will be fine.

|image3|

And here it is being driven by my Yenox Ms Pac-Man board with the
"`Horizontal Ms
Pac <http://umlautllama.com/projects/gamehacks/#horiz>`__" rom hack.
 You can see the power switch sticking out of the side of the power
supply there.  It's not the most optimal thing ever, but it's
substantially cleaner than before.  Perhaps I'll replace that switch
with a nice carling switch in the future.  I'll need this test rig for
the next task, which is fixing the audio on this board.  It sounds
horrid...

.. |image0| image:: https://images-blogger-opensocial.googleusercontent.com/gadgets/proxy?url=http%3A%2F%2F2.bp.blogspot.com%2F-cPL0_rfcnYY%2FUuqchrVN_XI%2FAAAAAAAACp0%2FNQdzATrpsS4%2Fs1600%2F2014-01-28%2B21.16.43.jpg&container=blogger&gadget=a&rewriteMime=image%2F*
   :class: aligncenter
   :width: 640px
   :height: 480px
   :target: http://2.bp.blogspot.com/-cPL0_rfcnYY/UuqchrVN_XI/AAAAAAAACp0/NQdzATrpsS4/s1600/2014-01-28+21.16.43.jpg
.. |image1| image:: https://images-blogger-opensocial.googleusercontent.com/gadgets/proxy?url=http%3A%2F%2F1.bp.blogspot.com%2F-dXu8idF4Gos%2FUuqcgxrHTTI%2FAAAAAAAACpw%2FkglKFQAxKSQ%2Fs1600%2F2014-01-28%2B21.15.52.jpg&container=blogger&gadget=a&rewriteMime=image%2F*
   :class: aligncenter
   :width: 640px
   :height: 480px
   :target: http://1.bp.blogspot.com/-dXu8idF4Gos/UuqcgxrHTTI/AAAAAAAACpw/kglKFQAxKSQ/s1600/2014-01-28+21.15.52.jpg
.. |image2| image:: https://images-blogger-opensocial.googleusercontent.com/gadgets/proxy?url=http%3A%2F%2F3.bp.blogspot.com%2F-ZsVc0fKDW7I%2FUuqcg9U7owI%2FAAAAAAAACpk%2FHtINUUqLkOk%2Fs1600%2F2014-01-28%2B21.14.07.jpg&container=blogger&gadget=a&rewriteMime=image%2F*
   :class: aligncenter
   :width: 640px
   :height: 480px
   :target: http://3.bp.blogspot.com/-ZsVc0fKDW7I/Uuqcg9U7owI/AAAAAAAACpk/HtINUUqLkOk/s1600/2014-01-28+21.14.07.jpg
.. |image3| image:: https://images-blogger-opensocial.googleusercontent.com/gadgets/proxy?url=http%3A%2F%2F4.bp.blogspot.com%2F-ACC-6mHPO68%2FUuqcg43SeQI%2FAAAAAAAACps%2FIk2i8_69l8U%2Fs1600%2F2014-01-28%2B21.13.46.jpg&container=blogger&gadget=a&rewriteMime=image%2F*
   :class: aligncenter
   :width: 640px
   :height: 480px
   :target: http://4.bp.blogspot.com/-ACC-6mHPO68/Uuqcg43SeQI/AAAAAAAACps/Ik2i8_69l8U/s1600/2014-01-28+21.13.46.jpg
