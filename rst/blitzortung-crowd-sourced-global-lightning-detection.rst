Blitzortung: Crowd-sourced global lightning detection
#####################################################
:date: 2014-09-23 20:00
:author: rtucker
:category: Uncategorized
:slug: blitzortung-crowd-sourced-global-lightning-detection
:status: published

`Lightning <https://en.wikipedia.org/wiki/Lightning>`__ is one of
nature’s most fascinating phenomena. In less than a millisecond, a
kilometers-long plasma channel sinks an unimaginable electrical current
from a cloud to the ground, unleashing vast amounts of energy in a very
short period of time. Nearby observers will see a brilliant flash of
light and hear (and feel!) a shockwave of thunder from the superheating
of the air surrounding the bolt. However, did you know that the effects
of lightning are also detectable as radio signals across thousands of
kilometers?

A group of researchers led by Prof. Dr. Egon Wanke of
`Düsseldorf <https://www.openstreetmap.org/relation/62539>`__, Germany,
started the `Blitzortung <http://www.blitzortung.org/>`__ project a few
years ago. Blitzortung is a worldwide, non-commercial, crowd-sourced
Time-of-Arrival (TOA) lightning detection and location network. Around
the world, hundreds of stations listen for the tell-tale electromagnetic
signature of a lightning stroke in the
`VLF <https://en.wikipedia.org/wiki/Very_low_frequency>`__ range
(roughly 3 to 30 kHz). When a stroke is detected, each station records
the characteristics of the signal and a precise
`GPS <https://en.wikipedia.org/wiki/Global_Positioning_System>`__
timestamp, and then transmits this information to a central server.

When a probable lightning stroke is detected by multiple stations, the
server uses the timestamps and the speed of light to locate the
lightning strike. If station A detected the stroke at time t\ :sub:`A`,
and station B detected the stroke at time t\ :sub:`B`, then the
lightning stroke had to occur somewhere along a hyperbolic curve, as a
time difference of 100 microseconds corresponds to a distance difference
of 30 kilometers. Compute curves for at least three pairs of stations
and they will hopefully all meet at exactly one point. This is the
essence of
`Time-of-Arrival <https://en.wikipedia.org/wiki/Time_of_arrival>`__
location finding.

Prior to this summer, the nearest station was about 400 km from
Rochester, outside of Philadelphia. This station was still able to
detect a significant number of lightning strokes from Rochester and
beyond! That’s because lightning produces an extremely strong, extremely
low-frequency electromagnetic pulse which bounces between the ground and
the ionosphere for thousands of kilometers, like an atmospheric
waveguide. However, two Rochester-area stations went live in late
summer, providing additional coverage for storms in the Northeastern US.

One of those stations is in Interlock Rochester’s space in the
Hungerford building. It consists of a custom-built magnetic loop
antenna, a Blitzortung amplifier board, and a Blitzortung controller
board. As of this writing, it has been active for two weeks and has
detected 30,282 lightning strokes, the longest of which was 4,350 km
away! This is despite our antenna being located inside of an industrial
building on the outskirts of downtown.

(Props to W2NED and the rest of the crew who built `the other
station <http://rags.rochesterham.org/e-RAGS/RAG_September_2014.pdf>`__,
located in Naples, New York.)

Total costs were approximately:

-  Blitzortung PCB and parts (amplifier, controller): €120
-  Antenna parts from Lowes: $20 (??)
-  STM32F4DISCOVERY ARM board from Mouser: $15

Future improvements include `3D-printing an enclosure for the
amplifier <http://www.thingiverse.com/thing:452968>`__ (and perhaps the
controller) and finding a better location to hang the antenna. While
we’re approaching the winter months and won’t see much lightning until
the spring, we’ve still got
`thundersnow <https://en.wikipedia.org/wiki/Thundersnow>`__ to look
forward to!

For more information on the Blitzortung project, visit `their web site
at blitzortung.org <http://www.blitzortung.org/>`__. You can see
statistics for our station at `the Lightning Maps
site <http://www.lightningmaps.org/blitzortung/region3/?bouser&bo_page=statistics&bo_show=station&bo_sid=1154>`__.
Also, you can see the real-time map of lightning strikes at
http://www.lightningmaps.org/realtime!

--------------

| |image0|
| *The Blitzortung amplifier board (left) and controller board (right)
  fully constructed, awaiting unit testing and integration.*

--------------

| |image1|
| *A magnetic loop antenna hangs in the workshop during initial tune-up.
  This antenna is directly connected to the amplifier, and is tuned to
  receive crisp impulse signals around 10 kHz.*

--------------

| |image2|
| *The controller board is installed in the server room, with power and
  amplifier connection on the top, GPS antenna cable on the top right,
  ground on the bottom right, and Ethernet on the bottom. The
  Blitzortung controller itself is located behind the STM32F4DISCOVERY
  board.*

.. |image0| image:: http://projects.ryantucker.us/Interlock/2014/Blitzortung/2014-08-29%2018.30.37.jpg?variant=small
.. |image1| image:: http://projects.ryantucker.us/Interlock/2014/Blitzortung/2014-08-31%2018.18.40.jpg?variant=small
.. |image2| image:: http://projects.ryantucker.us/Interlock/2014/Blitzortung/2014-09-06%2018.20.06.jpg?variant=small

