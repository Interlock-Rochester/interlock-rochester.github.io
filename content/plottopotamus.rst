Plottopotamus 
##############
:date: 2011-09-13 22:20
:author: berticus
:category: Uncategorized
:slug: plottopotamus
:status: published

I've been taking up quite a bit of space at Interlock lately with my new
toy, a Roland DPX-3300 pen plotter... delivered via ebay from the
magical futurepast of the early nineties. For those that are out of the
loop with the past century, pen plotters are two axis robo-thingamajigs
that basically pick up pens and draw on paper with them. They've been
replaced by wide-format inkjet printers, but they used to be quite
popular with anybody who wanted to plot out maps, blueprints, and other
large diagrams.

|Interlock Plotty Pictures 1|

Anyways, somehow I caught the plotter bug, even going so far as to learn
a bit of python after finding this neat library called
`Chiplotle <http://music.columbia.edu/cmc/chiplotle/>`__ that handles
the basics of creating and streaming artwork to plotters using their
native language of HPGL. They have a mailing list where they often point
out good plotter deals on ebay, and I foolishly/accidentally purchased
perhaps the biggest flatbed plotter out there. 3x2 feet of plotting
goodness, 100 pounds of steel and stepper motors delivered to my door by
a grumpy UPS driver.

|Interlock Plotty Pictures 2|

After realizing it doesn't fit anywhere in my house, I brought it to
Interlock and have been tinkering with it since. The first step was to
convert old dried out plotter pens into pen holders that would allow me
to use Sharpies or other art pens with the device. That involved a quick
trip to the lathe, which I hope to document more fully in the future.

|Interlock Plotty Pictures 3|

Having figured out an inexpensive pen solution, I really wanted to make
drawings based on webcam input... so I trawled around the internet and
mailing lists until I could piece together a passable solution using
OpenCV's python bindings, and a series of nerdy unixy commands (convert,
autotrace, and pstoedit) to trace, mush, and output the data. You can
find the relevant code up on my `Ronald
Toys <https://github.com/beardicus/ronald_toys%20>`__ Github repository.

|RoboPortraits|

Having conquered such menial tasks, I decided that the default route the
plotter was taking was quite inefficient, with lots of time spent
seeking back and forth between lines. My precious robot was spending
half its time flailing due to a poorly composed hpgl file. Surely there
was a better way.

`Tada! <https://github.com/beardicus/ronald_tools%20>`__ I wrote a
really dumb sort routine that attempts to minimize seeking between
lines, instead of blindly accepting the order that autotrace wrote them
in. You can see the difference in the following two time-lapse videos.
The first shows the default route that autotrace produces, and the
second is my optimized version.

Next step for this project: some more sophisticated drawing routines,
including some cross-hatched shading, color, and maybe even some 3D
input from a Kinect. Stop in for a Tuesday Open Night and maybe you can
be a robo-portrait guinea pig!

.. |Interlock Plotty Pictures 1| image:: http://farm7.static.flickr.com/6125/5937490274_0b95dfca21.jpg
   :width: 500px
   :height: 333px
   :target: http://www.flickr.com/photos/bert_m_b/5937490274/
.. |Interlock Plotty Pictures 2| image:: http://farm7.static.flickr.com/6009/5936937271_0e87fb9250.jpg
   :width: 500px
   :height: 333px
   :target: http://www.flickr.com/photos/bert_m_b/5936937271/
.. |Interlock Plotty Pictures 3| image:: http://farm7.static.flickr.com/6006/5936918129_7d4e1d4a2e.jpg
   :width: 500px
   :height: 333px
   :target: http://www.flickr.com/photos/bert_m_b/5936918129/
.. |RoboPortraits| image:: http://farm7.static.flickr.com/6125/5937423454_df75c66a42.jpg
   :width: 500px
   :height: 333px
   :target: http://www.flickr.com/photos/bert_m_b/5937423454/
