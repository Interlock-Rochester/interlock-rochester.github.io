BarCamp Plot-chester
####################
:date: 2011-10-30 20:37
:author: berticus
:category: News
:slug: barcamp-rochester
:status: published

|Interlock's BarCamp Table|

As is usually the case, Interlock managed to cajole/bribe the organizers
of `BarCamp Rochester <http://barcamproc.org/>`__ into giving us a table
in the atrium, upon which we could set up our wares and lure in
unsuspecting geeks. The conference itself was really great, with lots of
interesting talks, and lots of attendees and traffic by our table.
Everybody seemed quite excited about the "Skeletonizing Carcasses with
Flesh-eating Beetles" talk, myself included.

In the past, we've had a slight lack of table-sized projects that moved,
made noise, or otherwise stimulated people to come talk to us and see
what Interlock is all about... but no longer!

|image1|

After becoming a little obsessed with `old pen
plotters </2011/09/13/plottopotamus/>`__ over the
past few months, I decided I'd like to try assembling my own drawing
robot. The main goal, again, was to have something small, cool, and
interactive to attract folks at events where we have a table or booth.
So about a month ago, our journey started with destruction... one
printer and one printer/scanner gave their slightly non-functional lives
to this project. Anything slightly cool was saved, and of course the
precision rods, stepper motors, and timing belts were the main goal. I
wanted this to use pin-feed card stock, so an old dot-matrix printer was
also sacrificed.

I was without camera for most of the month, so documentation is
non-existent. Regardless, the documentation would have been something
like this: "!@#$!@#$ MORE EPOXY! !@#%!#$", along with pictures of me
looking frustrated. Let's just say, this machine is a hack, on top of a
kludge, wrapped in a cob-job. We ended up with the paper-feed mechanism
from the dot-matrix printer acting as the Y axis, and `a small solenoid
from adafruit <https://www.adafruit.com/products/412>`__ riding along on
the X axis with a wobbly pen-holder (and some tape (and epoxy!)). This
was all hooked up to a rickety breadboard (I designed and ordered an
Arduino shield via `Batch PCB <http://batchpcb.com>`__, but it didn't
arrive in time) with two `Polulu stepper
drivers <http://www.pololu.com/catalog/product/1201>`__, an Arduino, and
a simple transistor doohicky for toggling the solenoid. We ran
`grbl <https://github.com/simen/grbl>`__ on the Arduino, and after
tracking down a bug in said code and reflashing the firmware, we were
well on our way. I learned a lot, stressed a bit, and the morning of
BarCamp we barely managed this:

|image2|

But it got better throughout the day, with some live on-the-scene
hacking. I managed to get a toolchain set up to get webcam input traced
and plotted thusly:

|IMG_8267|

That toolchain starts with
`OpenCV <http://opencv.willowgarage.com/wiki/>`__ handling the webcam,
and doing a "trace outlines" sort of procedure. From there, a PNG is
saved, converted to vectors by
`autotrace <http://autotrace.sourceforge.net/>`__, converted from eps to
hpgl (the language of old-timey plotters) by
`pstoedit <http://www.pstoedit.net/>`__, slurped back into Python via
the `Chiplotle HPGL
library <http://music.columbia.edu/cmc/chiplotle/>`__, where I have a
few routines scale and optimize the tool path, and then we output some
ugly gcode and stream it to the Arduino. Phew.

It's a bit roundabout. But it worked, and it made people smile and
wander over to talk to us... and they got some cool robo-portraits out
of it. I'll leave you with another image and video of the bot doing its
thing. A few more can be found in `my flickr
gallery <http://www.flickr.com/photos/bert_m_b/sets/72157628015314436/detail/>`__.

|IMG_8269|

.. |Interlock's BarCamp Table| image:: /wp-uploads/2011/10/DSC_84671-1024x678.jpg
   :class: alignnone size-large wp-image-665
   :width: 600px
   :height: 400px
   :target: /wp-uploads/2011/10/DSC_84671.jpg
.. |image1| image:: /wp-uploads/2011/10/DSC_84971-1024x678.jpg
   :class: alignnone size-large wp-image-666
   :width: 600px
   :height: 400px
   :target: /wp-uploads/2011/10/DSC_84971.jpg
.. |image2| image:: /wp-uploads/2011/10/DSC_8494-1024x678.jpg
   :class: alignnone size-large wp-image-672
   :width: 600px
   :height: 400px
   :target: /wp-uploads/2011/10/DSC_8494.jpg
.. |IMG_8267| image:: http://farm7.static.flickr.com/6039/6294760604_cbcfdc264e_z.jpg
   :width: 600px
   :height: 400px
   :target: http://www.flickr.com/photos/bert_m_b/6294760604/
.. |IMG_8269| image:: http://farm7.static.flickr.com/6100/6294232619_e42b143249_z.jpg
   :width: 600px
   :height: 400px
   :target: http://www.flickr.com/photos/bert_m_b/6294232619/
